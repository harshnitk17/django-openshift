from django import forms


class FilterForm(forms.Form):
    CHOICES_initial = [('Bd', 'Bd'), ('Bu', 'Bu'), ('B', 'B'), ('Bs', 'Bs'),
                       ('Bc', 'Bc'), ('Lambdab', 'Lambdab'), ('Xib', 'Xib'), ('Omegab', 'Omegab')]
    initial = forms.ChoiceField(required=False, label='Initial Particles',
                                choices=CHOICES_initial, widget=forms.RadioSelect(attrs={'class': 'formbtn'}))
    CHOICES_observable = [('BR', 'BR'), ('ACP', 'ACP'),
                          ('polarization', 'polarization')]
    observable = forms.ChoiceField(required=False, label='Type of observable',
                                   choices=CHOICES_observable, widget=forms.RadioSelect(attrs={'class': 'formbtn'}))
    other_particles = ['D0', 'D+', 'Ds', 'D*0', 'D*+', 'Ds*', 'D**', 'Ds**', 'Jpsi', 'psi2S', 'etac', 'chic', 'ccbar', 'X3872', 'Pc', 'XYZ',
                       'p', 'n', 'Lambda', 'Sigma', 'Xi', 'Omega', 'baryon', 'Lambdac', 'Sigmac', 'Xic', 'cbaryon',
                       'K', 'K0', 'K*+', 'K*0', 'phi', 'kaon', 'pi', 'pi0', 'rho+', 'rho0', 'eta', 'omega', 'light', 'lepton', 'photon']
    D0 = forms.IntegerField(required=False, label="D0")
    Dplus = forms.IntegerField(required=False, label="D+")
    Ds = forms.IntegerField(required=False, label="Ds")
    Ds0 = forms.IntegerField(required=False, label="D*0")
    Dsplus = forms.IntegerField(required=False, label="D*+")
    Dss = forms.IntegerField(required=False, label="Ds*")
    Dsss = forms.IntegerField(required=False, label="D**")
    Dssss = forms.IntegerField(required=False, label="Ds**")