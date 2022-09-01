from django import forms


class HeartDiseaseForm(forms.Form):

    age = forms.FloatField(label='Age', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    sex = forms.FloatField(label='Sex', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cp = forms.FloatField(label='CP', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    trestbps = forms.FloatField(label='TRESTBPS', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    chol = forms.FloatField(label='CHOL', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fbs = forms.FloatField(label='FBS', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    restecg = forms.FloatField(label='RESTECG', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    thalach = forms.FloatField(label='THALACH', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    exang = forms.FloatField(label='EXANG', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    oldpeak = forms.FloatField(label='OLDPEAK', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    slope = forms.FloatField(label='SLOPE', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ca = forms.FloatField(label='CA', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    thal = forms.FloatField(label='THAL', min_value=0, max_value=100, widget=forms.NumberInput(attrs={'class': 'form-control'}))