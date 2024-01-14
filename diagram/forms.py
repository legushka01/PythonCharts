from django import forms

from diagram.models import QalaData


class QalaDataFrom(forms.ModelForm):
    class Meta:
        model = QalaData
        fields = '__all__'