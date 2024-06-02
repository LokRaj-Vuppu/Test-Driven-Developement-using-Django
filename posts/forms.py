from django import forms
from posts.models import Post


class PostCreationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["title", "body", "post_file"]


class PostUpdationForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
