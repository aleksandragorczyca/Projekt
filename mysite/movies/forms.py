from django import forms

VOTE_SELECT= [
    ('one', '1'),
    ('two', '2'),
    ('Three', '3'),
    ('Four', '4'),
    ('Five', '5'),
    ]

class UserForm(forms.Form):
    voting= forms.CharField(label='Your mark on this movie:', widget=forms.RadioSelect(choices=VOTE_SELECT))