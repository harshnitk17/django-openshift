from django import forms


class FilterForm(forms.Form):
    CHOICES_initial = [('Bd', '$B^0$'), ('Bu', '$B^+$'), ('B', '$B^0+B^+$'), ('Bs', '$B_s^0$'),
                       ('Bc', '$B_c^+$'), ('Lambdab', '$\\Lambda_b$'), ('Xib', '$\\Xi_b$'), ('Omegab', '$\\Omega_b$')]
    initial = forms.ChoiceField(required=False, label='Initial Particles',
                                choices=CHOICES_initial, widget=forms.RadioSelect(attrs={'class': 'formbtn'}))
    CHOICES_observable = [('BR', 'Branching fraction'), ('ACP', 'CP asymmetry'),
                          ('polarization', 'Polarization')]
    observable = forms.ChoiceField(required=False, label='Type of observable',
                                   choices=CHOICES_observable, widget=forms.RadioSelect(attrs={'class': 'formbtn'}))
    other_particles = ['D0', 'D+', 'Ds', 'D*0', 'D*+', 'Ds*', 'D**', 'Ds**', 'Jpsi', 'psi2S', 'etac', 'chic', 'ccbar', 'X3872', 'Pc', 'XYZ',
                       'p', 'n', 'Lambda', 'Sigma', 'Xi', 'Omega', 'baryon', 'Lambdac', 'Sigmac', 'Xic', 'cbaryon',
                       'K', 'K0', 'K*+', 'K*0', 'phi', 'kaon', 'pi', 'pi0', 'rho+', 'rho0', 'eta', 'omega', 'light', 'lepton', 'photon']
    D0 = forms.IntegerField(required=False, label="D0",widget=forms.TextInput(attrs={'class': 'charminput', 'value': 0}))
    Dplus = forms.IntegerField(required=False, label="D+",widget=forms.TextInput(attrs={'class': 'charminput', 'value': 0}))
    Ds = forms.IntegerField(required=False, label="Ds",widget=forms.TextInput(attrs={'class': 'charminput', 'value': 0}))
    Ds0 = forms.IntegerField(required=False, label="D*0",widget=forms.TextInput(attrs={'class': 'charminput', 'value': 0}))
    Dsplus = forms.IntegerField(required=False, label="D*+",widget=forms.TextInput(attrs={'class': 'charminput', 'value': 0}))
    Dss = forms.IntegerField(required=False, label="Ds*",widget=forms.TextInput(attrs={'class': 'charminput', 'value': 0}))
    Dsss = forms.IntegerField(required=False, label="D**",widget=forms.TextInput(attrs={'class': 'charminput', 'value': 0}))
    Dssss = forms.IntegerField(required=False, label="Ds**",widget=forms.TextInput(attrs={'class': 'charminput', 'value': 0}))