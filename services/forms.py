# from django import forms
# from .models import Symptom

# class SymptomSelectionForm(forms.Form):
#     symptoms = forms.ModelMultipleChoiceField(
#         queryset=Symptom.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#         required=True,
#         label="Select your symptoms"
#     )

# services/forms.py

# from django import forms

# class SymptomSelectionForm(forms.Form):
#     symptoms = forms.MultipleChoiceField(
#         choices=[
#             ('s_21', 'Dureri de cap'),
#             ('s_98', 'Probleme urinare'),
#             ('s_107', 'Probleme respiratorii'),
#             ('s_12', 'Probleme digestive'),
#         ],
#         widget=forms.CheckboxSelectMultiple,
#         required=True,
#         label="Select your symptoms"
#     )

from django import forms

SYMPTOMS_CHOICES = [
    ('s_5', 'Oboseală'),
    ('s_8', 'Tuse'),
    ('s_10', 'Erupții cutanate'),
    ('s_12', 'Probleme digestive'),
    ('s_15', 'Febră'),
    ('s_21', 'Dureri de cap'),
    ('s_22', 'Vărsături'),
    ('s_23', 'Amețeli'),
    ('s_31', 'Dureri abdominale'),
    ('s_38', 'Dureri în gât'),
    ('s_41', 'Constipație'),
    ('s_55', 'Dureri musculare'),
    ('s_60', 'Palpitații'),
    ('s_65', 'Durere la urinare'),
    ('s_70', 'Transpirații nocturne'),
    ('s_85', 'Pierderea poftei de mâncare'),
    ('s_90', 'Durere toracică'),
    ('s_96', 'Greață'),
    ('s_98', 'Probleme urinare'),
    ('s_101', 'Erupție pe piele'),
    ('s_107', 'Probleme respiratorii'),
    ('s_110', 'Durere în piept'),
    ('s_130', 'Pierderea în greutate'),
    ('s_150', 'Umflare glezne'),
    ('s_170', 'Tulburări de somn'),
    ('s_180', 'Dureri articulare'),
]

class SymptomSelectionForm(forms.Form):
    symptoms = forms.MultipleChoiceField(
        choices=SYMPTOMS_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
    )