
from django import forms
from artical.models  import Article
class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    email = forms.EmailField()
    
class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','content')
        #fields = '__all__' #for all fields that are used in the models
        
        