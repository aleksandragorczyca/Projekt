
from django import forms

#fomularz

VOTE = [('1', 'So bad'),('2', 'Bad'),('3','Ok'),('4','Cool'),('5','Super Cool')]

class Form(forms.Form):
 vote = forms.CharField(widget=forms.RadioSelect(choices=VOTE))
        
        



  
