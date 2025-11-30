from django import forms
from .models import Article


class ArticleFilterForm(forms.Form):
    articles = forms.ModelMultipleChoiceField(
        queryset=Article.objects.all(),
        required=False,
        label="Články",
        widget=forms.SelectMultiple,  # alebo CheckboxSelectMultiple
    )

    only_published = forms.BooleanField(
        required=False,
        label="Len publikované",
    )
