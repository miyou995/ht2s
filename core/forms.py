from django import forms
from django.forms import ModelForm
from .models import Contact,  Quote, Hiring
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError


CHOICES = (
    ('S1' ,'Cycle Moyen'),
    ('S2' ,'Niveau Secondaire'),
    ('S3' ,'Niveau Terminal'),
    ('S4' ,'Formation Professionnelle '),
    ('S5' ,'Baccalauréat'),
    ('S6' ,'Niveau Universitaire'),
)
CHOICES_YES = (
    ('1' ,'YES'),
    ('2' ,'NO '),

)

class ContactForm(ModelForm) :
    username = forms.CharField(required=False)
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    entreprise = forms.CharField(required=False)

    class Meta: 
        model = Contact 
        fields = (
                'name',
                'email',
                'phone',
                'entreprise',
                # 'service',
                'subject',
                'message',)
        
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if username:
            raise ValidationError(
                    "BAD BOT"
                )
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Full name *"
        self.fields['email'].label = "Email *"
        self.fields['phone'].label = "Phone *"
        self.fields['entreprise'].label = "Company "
        self.fields['subject'].label = "subject "
        self.fields['message'].label = "message "
        self.fields['username'].widget = forms.HiddenInput()
        # self.fields['service'].widget.attrs.update({
        #         "class": "select-form select-contact", 
        #         "placeholder" : "Select service"
        #     }) 
        self.fields['message'].widget.attrs.update({
                "class": "subject", 
            }) 
        
class QuoteForm(ModelForm) :
    username = forms.CharField(required=False)
    entreprise = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    service = forms.CharField(required=False)
    class Meta: 
        model = Quote 
        fields = (
            'email',
            'phone',
            'entreprise', 
            'service'
            )
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if username:
            raise ValidationError(
                    "BAD BOT"
                )
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields['entreprise'].label = "Company *"
        self.fields['email'].label = "Email *"
        self.fields['phone'].label = "Phone *"
        self.fields['service'].label = "service "
        self.fields['username'].widget = forms.HiddenInput()
        self.fields['service'].widget.attrs.update({
                "class": "select-form select-contact", 
                "placeholder" : "Select service"
            }) 
     

class HiringForm(ModelForm) :
    username = forms.CharField(required=False)
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    birth_date = forms.DateField(required=True, widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}), input_formats=["%Y-%m-%d"])
    birth_place = forms.CharField(required=False)
    niveau = forms.ChoiceField(required=False, choices=CHOICES)
    # permis = forms.BooleanField(required=False, initial=False)
    # passeport = forms.BooleanField(required=False, initial=False)
    # army = forms.BooleanField(required=False, initial=False)
    cv_file = forms.FileField(required=False)
    # message = forms.CharField(required=False)

    class Meta: 
        model = Hiring 
        fields = (
                'name',
                'email',
                'phone',
                'niveau',
                'birth_date',
                'birth_place',
                # 'permis',
                # 'passeport',
                # 'army',
                'cv_file',
                'message',

                )
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        if username:
            raise ValidationError(
                    "BAD BOT"
                )   
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Full name *"
        self.fields['email'].label = "Email *"
        self.fields['phone'].label = "Phone *"
        self.fields['birth_date'].label = "Birth date *"
        self.fields['birth_place'].label = "Birth place "
        self.fields['niveau'].label = "niveau "
        # self.fields['permis'].label = "driving licence "
        # self.fields['passeport'].label = "passeport "
        # self.fields['army'].label = "Carte jaune "
        self.fields['cv_file'].label = "cv_file "
        self.fields['message'].label = "message "

        self.fields['username'].widget = forms.HiddenInput()
        self.fields['niveau'].widget.attrs.update({
                "class": "select-form select-contact", 
                "placeholder" : "Select service"
            }) 
        # self.fields['permis'].widget.attrs.update({
        #         # "class": "checkbox", 
        #         "type":"radio",
        #         "placeholder" : "driving licence"
        #     }) 


