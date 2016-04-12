from django import forms
class HashtagForm(forms.Form):
    search_box = forms.CharField(label='Type the Hashtag Here: ', max_length=50)
