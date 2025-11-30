from django import forms
from .models import Article


class ArticleFilterForm(forms.ModelForm):
    articles = forms.ModelMultipleChoiceField(
        queryset=Article,
        required=False,
        label="Článok",
    )
    only_published = forms.BooleanField(
        required=False,
        label="Len publikované",
    )
