from django import forms
from .models import Athlete, PDFFile

class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['name', 'bio', 'photo']


from django import forms
from .models import PDFFile

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFFile
        fields = ['title', 'file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'accept': 'application/pdf'}),
        }
