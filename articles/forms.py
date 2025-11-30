from django import forms
from .models import Article, NewSource


class ArticleFilterForm(forms.Form):
    q = forms.CharField(
        required=False,
        label="Hľadať v názve",
    )

    source = forms.ModelChoiceField(
        queryset=NewSource.objects.all(),
        required=False,
        label="Zdroj",
        empty_label="Všetky zdroje",
    )

    date_from = forms.DateField(
        required=False,
        label="Publikované od",
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    date_to = forms.DateField(
        required=False,
        label="Publikované do",
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    only_recent = forms.BooleanField(
        required=False,
        label="Len články za posledných 7 dní",
    )
