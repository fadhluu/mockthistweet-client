from django import forms


class NewTweet(forms.Form):
    new_tweet = forms.CharField(
        label="New Tweet", label_suffix="", max_length=160, widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'border-color: #007bff;'}))
