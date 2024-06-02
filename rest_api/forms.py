from django import forms


class RegistrationForm(forms.Form):
    pass


class CommentForm(forms.Form):
    name = forms.CharField(label="Your name")
    url = forms.URLField(label="Your website", required=False)
    comment = forms.CharField()


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
