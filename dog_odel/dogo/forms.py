from django import forms

class Subscribe(forms.Form):
    mail = forms.EmailField(label='Your e-mail', max_length=100)
    name = forms.CharField(label='Your name', max_length=100)
    first_name = forms.CharField(label='Your first name', max_length=100)
    choix = (
        ('Male', 'M'),
        ('Femelle', 'F'),
    )
    sexe = forms.ChoiceField(label='Your civility', choices=choix)
    birth = forms.DateField()