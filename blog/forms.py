from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["body"].required=False

    body = forms.CharField(widget=CKEditor5Widget(config_name='extends'))

    class Meta:
        model = Post
        fields = ["title","thumbnail","body","category","status"]
        
class PostUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["body"].required=False

    body = forms.CharField(widget=CKEditor5Widget(config_name='extends'))

    class Meta:
        model = Post
        fields = ["title","thumbnail","body","category","status"]
        