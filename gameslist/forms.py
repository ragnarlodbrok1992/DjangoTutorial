import re
from datetime import date, time
from django.core.exceptions import ValidationError
from django.forms import (
    ModelForm, CharField, ModelChoiceField, IntegerField,
    DateField, Textarea
)

from gameslist.models import Genre, Game


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized')


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates are allowed here')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = '__all__'

    # title = CharField(max_length=128, validators=[capitalized_validator])
    # genre = ModelChoiceField(queryset=Genre.objects)
    # rating = IntegerField(min_value=1, max_value=10)
    # released = DateField(required=False)
    # description = CharField(widget=Textarea, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'FPS' and result['rating'] > 5:
            self.add_error('genre', '')
            self.add_error('rating', '')
            raise ValidationError(
                'FPS games cannot have a rating above 5, since they are all terrible.'
            )
        return result
