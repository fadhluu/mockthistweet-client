from django import forms


class NewTweet(forms.Form):
    new_tweet = forms.CharField(
        label="Tweet", max_length=160, widget=forms.TextInput(attrs={'class': 'form-control'}))
