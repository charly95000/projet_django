from django import forms
from articles.models import Author
from articles.models import Article

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'