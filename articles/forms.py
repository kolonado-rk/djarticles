from django import forms
from .models import Article


class ArticleFilterForm(forms.Form):
    article = forms.ModelChoiceField(
        queryset=Article.objects.all(),
        required=False,
        label="Článok",
    )

    only_recent = forms.BooleanField(
        required=False,
        label="Len články za posledných 7 dní",
    )