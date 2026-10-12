from django import forms
from .models import Visit

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['visitor_name', 'phone_number', 'email', 'company', 'host_person', 'purpose', 'status']
        widgets = {
            # On ajoute des classes Tailwind pour le design
            field: forms.TextInput(attrs={'class': 'w-full p-2 border rounded-lg focus:ring-2 focus:ring-blue-500 outline-none'})
            for field in ['visitor_name', 'phone_number', 'company', 'host_person']
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['purpose'].widget.attrs.update({'class': 'w-full p-2 border rounded-lg'})
        self.fields['status'].widget.attrs.update({'class': 'w-full p-2 border rounded-lg'})
        self.fields['email'].widget.attrs.update({'class': 'w-full p-2 border rounded-lg'})