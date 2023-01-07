from django import forms
from .models import TodoModel


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class TodoForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Title Name"}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "Enter Descrition", "rows": 3}))
    finish_by_date = forms.DateField(widget=DateInput(attrs={
        'class': 'form-control'
    }))
    finish_by_time = forms.TimeField(widget=TimeInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = TodoModel
        fields = ['title', 'description',
                  'finish_by_date', 'finish_by_time', 'is_done']
