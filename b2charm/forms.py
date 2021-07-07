from django import forms

class FilterForm(forms.Form):
    CHOICES=[('Bd','Bd'),('Bu','Bu'),('B','B'),('Bs','Bs'),('Bc','Bc'),('Lambdab','Lambdab'),('Xib','Xib'),('Omegab','Omegab')]
    #CHOICES2=[('D','single charm mesons'),('DD','two charm mesons'),('cc','charmonium'),('baryon','charm baryon'),('other','charm like states'),('B','beauty meson')]
    initial = forms.ChoiceField(label='Initial Particles',choices=CHOICES, widget=forms.RadioSelect)
    #final = forms.ChoiceField(label='Final State',choices=CHOICES2, widget=forms.RadioSelect)

