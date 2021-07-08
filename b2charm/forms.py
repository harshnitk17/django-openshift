from django import forms

class FilterFormInitial(forms.Form):
    CHOICES=[('Bd','Bd'),('Bu','Bu'),('B','B'),('Bs','Bs'),('Bc','Bc'),('Lambdab','Lambdab'),('Xib','Xib'),('Omegab','Omegab')]
    initial = forms.ChoiceField(label='Initial Particles',choices=CHOICES, widget=forms.RadioSelect(attrs={'class': 'initialform'}))

class FilterFormObservable(forms.Form):
    CHOICES=[('BR','BR'), ('ACP','ACP'), ('polarization','polarization')]
    observable = forms.ChoiceField(label='Type of observable',choices=CHOICES, widget=forms.RadioSelect)




