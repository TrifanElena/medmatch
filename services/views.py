# from django.shortcuts import render
# from .forms import SymptomSelectionForm
# from clinics.models import Clinic
# from services.api import get_specialty_from_symptoms  # <-- importă funcția centralizată

# def symptom_checker(request):
#     if request.method == 'POST':
#         form = SymptomSelectionForm(request.POST)
#         if form.is_valid():
#             selected_symptoms = form.cleaned_data['symptoms']

#             # 🔍 Debug - Afișăm ce simptome au fost selectate
#             print("📋 Simptome selectate:", selected_symptoms)

#             recommended_specialty = get_specialty_from_symptoms(selected_symptoms)

#             # 🔍 Debug - Ce specialitate a fost returnată
#             print("✅ Specialitate recomandată:", recommended_specialty)

#             clinics = Clinic.objects.filter(specialties__name=recommended_specialty) if recommended_specialty else []

#             return render(request, 'services/recommend_specialty.html', {
#                 'specialty': recommended_specialty,
#                 'clinics': clinics,
#             })
#     else:
#         form = SymptomSelectionForm()

#     return render(request, 'services/symptom_checker.html', {'form': form})


# def recommend_specialty(request):
#     return render(request, 'services/recommend_specialty.html')

# def home(request):
#     return render(request, 'services/home.html')


# VARIANTA BUNA
# from django.shortcuts import render
# from .forms import SymptomSelectionForm
# from clinics.models import Clinic
# from services.api import get_specialty_from_symptoms

# def symptom_checker(request):
#     if request.method == 'POST':
#         form = SymptomSelectionForm(request.POST)
#         if form.is_valid():
#             selected_symptoms = form.cleaned_data['symptoms']
#             print("📋 Simptome selectate:", selected_symptoms)

#             diagnosis, recommended_specialty = get_specialty_from_symptoms(selected_symptoms)

#             print("✅ Diagnosticul returnat:", diagnosis)
#             print("✅ Specialitate recomandată:", recommended_specialty)

#             clinics = Clinic.objects.filter(specialties__name__iexact=recommended_specialty) if recommended_specialty else []

#             return render(request, 'services/recommend_specialty.html', {
#                 'diagnosis': diagnosis,
#                 'specialty': recommended_specialty,
#                 'clinics': clinics,
#             })
#     else:
#         form = SymptomSelectionForm()

#     # Doar formularul când e GET
#     return render(request, 'services/symptom_checker.html', {'form': form})

# def recommend_specialty(request):
#     return render(request, 'services/recommend_specialty.html')

# def home(request):
#     return render(request, 'services/home.html')


# from django.shortcuts import render
# from .forms import SymptomSelectionForm
# from clinics.models import Clinic
# from services.api import get_specialty_from_symptoms

# def symptom_checker(request):
#     recommended_specialty = None
#     diagnosis = None
#     clinics = []

#     if request.method == 'POST':
#         form = SymptomSelectionForm(request.POST)
#         if form.is_valid():
#             selected_symptoms = form.cleaned_data['symptoms']
#             print("📋 Simptome selectate:", selected_symptoms)

#             # Obține diagnosticul și specialitatea
#             diagnosis, recommended_specialty = get_specialty_from_symptoms(selected_symptoms)

#             print("✅ Diagnosticul returnat:", diagnosis)
#             print("✅ Specialitate recomandată:", recommended_specialty)

#             if recommended_specialty:
#                 clinics = Clinic.objects.filter(specialties__name__iexact=recommended_specialty)
#     else:
#         form = SymptomSelectionForm()

#     return render(request, 'services/recommend_specialty.html', {
#         'form': form,
#         'specialty': recommended_specialty,
#         'diagnosis': diagnosis,
#         'clinics': clinics,
#     })


# def symptom_checker(request):
#     if request.method == 'POST':
#         form = SymptomSelectionForm(request.POST)
#         if form.is_valid():
#             selected_symptoms = form.cleaned_data['symptoms']
#             print("📋 Simptome selectate:", selected_symptoms)

#             # ✅ Obținem atât diagnosticul cât și specialitatea
#             diagnosis, recommended_specialty = get_specialty_from_symptoms(selected_symptoms)

#             print("✅ Diagnosticul returnat:", diagnosis)
#             print("✅ Specialitate recomandată:", recommended_specialty)

#             clinics = Clinic.objects.filter(specialties__name=recommended_specialty) if recommended_specialty else []

#             return render(request, 'services/recommend_specialty.html', {
#                 'diagnosis': diagnosis,
#                 'specialty': recommended_specialty,
#                 'clinics': clinics,
#             })
#     else:
#         form = SymptomSelectionForm()

#     return render(request, 'services/symptom_checker.html', {
#         # 'form': form
#         'specialty': recommended_specialty,
#     'clinics': clinics,
#     'diagnosis': translated_diagnosis,
#         })

# from django.shortcuts import render
# from .forms import SymptomSelectionForm
# from clinics.models import Clinic
# from services.api import get_specialty_from_symptoms

# def symptom_checker(request):
#     if request.method == 'POST':
#         form = SymptomSelectionForm(request.POST)
#         if form.is_valid():
#             selected_symptoms = form.cleaned_data['symptoms']
#             print("📋 Simptome selectate:", selected_symptoms)

#             diagnosis, recommended_specialty = get_specialty_from_symptoms(selected_symptoms)
#             print("✅ Diagnosticul returnat:", diagnosis)
#             print("✅ Specialitate recomandată:", recommended_specialty)

#             clinics = Clinic.objects.filter(specialties__name__iexact=recommended_specialty) if recommended_specialty else []

#             return render(request, 'services/recommend_specialty.html', {
#                 'diagnosis': diagnosis,
#                 'specialty': recommended_specialty,
#                 'clinics': clinics,
#             })
#     else:
#         form = SymptomSelectionForm()

#     return render(request, 'services/symptom_checker.html', {'form': form})

# def recommend_specialty(request):
#     return render(request, 'services/recommend_specialty.html')

# def home(request):
#     return render(request, 'services/home.html')

























# VARIANTA BUNAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
# from django.shortcuts import render
# from .forms import SymptomSelectionForm
# from clinics.models import Clinic
# from services.api import get_specialty_from_symptoms

# def symptom_checker(request):
#     diagnosis = None
#     recommended_specialty = None
#     clinics = []

#     if request.method == 'POST':
#         form = SymptomSelectionForm(request.POST)
#         if form.is_valid():
#             selected_symptoms = form.cleaned_data['symptoms']
#             print("📋 Simptome selectate:", selected_symptoms)

#             # Obținem diagnosticul și specialitatea
#             diagnosis, recommended_specialty = get_specialty_from_symptoms(selected_symptoms)
#             print("✅ Diagnosticul returnat:", diagnosis)
#             print("✅ Specialitate recomandată:", recommended_specialty)

#             # Filtrăm clinicile doar dacă avem utilizator logat și specialitate
#             if request.user.is_authenticated and recommended_specialty:
#                 user_city = getattr(request.user, 'city', None)
#                 print(f"📍 Orașul utilizatorului: {user_city}")

#                 if user_city:
#                     clinics = Clinic.objects.filter(
#                         specialties__name__iexact=recommended_specialty,
#                         city__iexact=user_city
#                     )
#                 else:
#                     # Dacă nu are oraș, fallback pe toate clinicile cu acea specialitate
#                     clinics = Clinic.objects.filter(specialties__name__iexact=recommended_specialty)
#             elif recommended_specialty:
#                 clinics = Clinic.objects.filter(specialties__name__iexact=recommended_specialty)
#     else:
#         form = SymptomSelectionForm()

#     return render(request, 'services/recommend_specialty.html', {
#         'form': form,
#         'diagnosis': diagnosis,
#         'specialty': recommended_specialty,
#         'clinics': clinics,
#     })

# def recommend_specialty(request):
#     return render(request, 'services/recommend_specialty.html')

# def home(request):
#     return render(request, 'services/home.html')























from django.shortcuts import render
from .forms import SymptomSelectionForm
from clinics.models import Clinic
from services.api import get_specialty_from_symptoms
from django.contrib.auth.decorators import login_required

@login_required
def symptom_checker(request):
    diagnosis = None
    recommended_specialty = None
    clinics = []

    if request.method == 'POST':
        form = SymptomSelectionForm(request.POST)
        if form.is_valid():
            selected_symptoms = form.cleaned_data['symptoms']
            print("📋 Simptome selectate:", selected_symptoms)

            # Obținem diagnosticul și specialitatea
            diagnosis, recommended_specialty = get_specialty_from_symptoms(selected_symptoms)
            print("✅ Diagnosticul returnat:", diagnosis)
            print("✅ Specialitate recomandată:", recommended_specialty)

            if request.user.is_authenticated and recommended_specialty:
                user_city = getattr(request.user, 'city', None)
                print(f"📍 Orașul utilizatorului: {user_city}")

                if user_city:
                    clinics = Clinic.objects.filter(
                        specialties__name__iexact=recommended_specialty,
                        city__iexact=user_city
                    )
                else:
                    clinics = Clinic.objects.filter(
                        specialties__name__iexact=recommended_specialty
                    )
            elif recommended_specialty:
                clinics = Clinic.objects.filter(specialties__name__iexact=recommended_specialty)
    else:
        form = SymptomSelectionForm()

    return render(request, 'services/recommend_specialty.html', {
        'form': form,
        'diagnosis': diagnosis,
        'specialty': recommended_specialty,
        'clinics': clinics,
    })

def recommend_specialty(request):
    return render(request, 'services/recommend_specialty.html')

def home(request):
    return render(request, 'services/home.html')
