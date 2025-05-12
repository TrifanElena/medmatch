# import os
# import requests
# from dotenv import load_dotenv

# # Încarcă variabilele din .env
# load_dotenv()

# # Fallback local în caz de eroare
# SYMPTOM_TO_SPECIALTY = {
#     'durere de cap': 'Neurologie',
#     'amețeală': 'Neurologie',
#     'durere abdominală': 'Gastroenterologie',
#     'dureri la urinare': 'Urologie',
#     'probleme digestive': 'Gastroenterologie',
# }

# # Traduceri din engleză în română pentru diagnostice
# DIAGNOSIS_TRANSLATIONS = {
#     "Common cold": "Răceală comună",
#     "Migraine": "Migrenă",
#     "Urinary tract infection": "Infecție urinară",
#     "Gastroenteritis": "Gastroenterită",
# }

# # Asociere diagnostic → specialitate
# CONDITION_TO_SPECIALTY = {
#     "Common cold": "Pneumologie",
#     "Migraine": "Neurologie",
#     "Urinary tract infection": "Urologie",
#     "Gastroenteritis": "Gastroenterologie",
# }



# # services/api.py
# def get_specialty_from_symptoms(symptoms):
#     app_id = os.getenv("INFERMEDICA_APP_ID")
#     app_key = os.getenv("INFERMEDICA_APP_KEY")

#     if not app_id or not app_key:
#         print("⚠️ Cheile API Infermedica nu sunt setate, folosim fallback local.")
#         specialty = fallback_specialty(symptoms)
#         return None, specialty  # diagnostic=None

#     headers = {
#         "App-Id": app_id,
#         "App-Key": app_key,
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#     }

#     evidence = [{"id": symptom, "choice_id": "present"} for symptom in symptoms]

#     body = {
#         "sex": "female",
#         "age": { "value": 30 },
#         "evidence": evidence
#     }

#     try:
#         response = requests.post("https://api.infermedica.com/v3/diagnosis", headers=headers, json=body)
#         if response.status_code == 200:
#             data = response.json()
#             conditions = data.get("conditions", [])
#             if conditions:
#                 diagnosis = conditions[0]["name"]
#                 print("✅ Recomandare API:", diagnosis)

#                 translation_map = {
#                     "Common cold": "Răceală comună",
#                     "Migraine": "Migrenă",
#                     # adaugă aici și altele după caz
#                 }

#                 translated = translation_map.get(diagnosis, diagnosis)
#                 specialty_map = {
#                     "Răceală comună": "Pneumologie",
#                     "Migrenă": "Neurologie",
#                 }

#                 recommended_specialty = specialty_map.get(translated)
#                 print("✅ Diagnosticul tradus:", translated)
#                 print("✅ Specialitate recomandată:", recommended_specialty)
#                 return translated, recommended_specialty
#     except Exception as e:
#         print("❌ Eroare API:", str(e))

#     return None, fallback_specialty(symptoms)


# def fallback_specialty(symptoms):
#     """Fallback local dacă API-ul eșuează"""
#     for symptom in symptoms:
#         normalized = symptom.strip().lower()
#         if normalized in SYMPTOM_TO_SPECIALTY:
#             return SYMPTOM_TO_SPECIALTY[normalized]
#     return None

# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# # Fallback local dacă API-ul nu merge sau nu există un diagnostic clar
# SYMPTOM_TO_SPECIALTY = {
#     's_21': 'Neurologie',        # Dureri de cap
#     's_98': 'Urologie',          # Probleme urinare
#     's_107': 'Pneumologie',      # Probleme respiratorii
#     's_12': 'Gastroenterologie', # Probleme digestive
#     's_9': 'Gastroenterologie',  # Greață
#     's_10': 'Gastroenterologie', # Vărsături
#     's_45': 'Pneumologie',       # Tuse
#     's_7': 'Medic de familie',   # Febră
#     's_33': 'Medicină internă',  # Oboseală
#     's_188': 'ORL',              # Durere în gât
#     's_56': 'Gastroenterologie', # Durere abdominală
#     's_65': 'Reumatologie',      # Dureri musculare
#     's_76': 'Reumatologie',      # Dureri articulare
#     's_14': 'Neurologie',        # Amețeală
#     's_86': 'Dermatologie',      # Erupție cutanată
#     's_96': 'Urologie',          # Durere la urinare
#     's_122': 'Pneumologie',      # Dificultăți de respirație
#     's_87': 'ORL',               # Nas înfundat
#     's_89': 'ORL',               # Secreții nazale
#     's_233': 'ORL',              # Pierdere miros/gust
# }

# # Diagnostic în EN -> RO + recomandare specialitate
# DIAGNOSIS_TRANSLATIONS = {
#     "Common cold": ("Răceală comună", "Pneumologie"),
#     "Migraine": ("Migrenă", "Neurologie"),
#     "Gastritis": ("Gastrită", "Gastroenterologie"),
#     "Sinusitis": ("Sinuzită", "ORL"),
#     "Urinary tract infection": ("Infecție urinară", "Urologie"),
#     "Asthma": ("Astm", "Pneumologie"),
#     "Flu": ("Gripă", "Pneumologie"),
#     "COVID-19": ("COVID-19", "Pneumologie"),
#     # adaugă după caz
# }

# def get_specialty_from_symptoms(symptoms):
#     app_id = os.getenv("INFERMEDICA_APP_ID")
#     app_key = os.getenv("INFERMEDICA_APP_KEY")

#     if not app_id or not app_key:
#         print("⚠️ Cheile API lipsesc — folosim fallback local.")
#         specialty = fallback_specialty(symptoms)
#         return None, specialty

#     headers = {
#         "App-Id": app_id,
#         "App-Key": app_key,
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#     }

#     evidence = [{"id": symptom, "choice_id": "present"} for symptom in symptoms]

#     body = {
#         "sex": "female",  # temporar hardcodat
#         "age": {"value": 30},
#         "evidence": evidence
#     }

#     try:
#         response = requests.post("https://api.infermedica.com/v3/diagnosis", headers=headers, json=body)
#         if response.status_code == 200:
#             data = response.json()
#             conditions = data.get("conditions", [])
#             if conditions:
#                 diagnosis_en = conditions[0]["name"]
#                 print("✅ Recomandare API:", diagnosis_en)

#                 translated, specialty = DIAGNOSIS_TRANSLATIONS.get(diagnosis_en, (diagnosis_en, None))

#                 print("✅ Traducere diagnostic:", translated)
#                 print("✅ Specialitate:", specialty)

#                 return translated, specialty
#             else:
#                 print("⚠️ Niciun diagnostic returnat de API.")
#     except Exception as e:
#         print("❌ Eroare API:", str(e))

#     return None, fallback_specialty(symptoms)

# def fallback_specialty(symptoms):
#     """Folosește maparea locală dacă API-ul eșuează"""
#     for symptom in symptoms:
#         specialty = SYMPTOM_TO_SPECIALTY.get(symptom)
#         if specialty:
#             print("🔁 Fallback specialty:", specialty)
#             return specialty
#     return None

# import os 
# import requests
# from dotenv import load_dotenv

# # Încarcă cheile din fișierul .env
# load_dotenv()

# Harta locală: simptom -> diagnostic și specialitate recomandată
# SYMPTOM_DIAGNOSIS_SPECIALTY_MAP = {
#     's_21': ("Migrenă", "Neurologie"),
#     's_98': ("Infecție urinară", "Urologie"),
#     's_107': ("Răceală comună", "Pneumologie"),
#     's_12': ("Gastrită", "Gastroenterologie"),
#     's_37': ("Greață", "Gastroenterologie"),
#     's_119': ("Fotosensibilitate", "Neurologie"),
#     's_15': ("Durere toracică", "Cardiologie"),
#     's_56': ("Tuse", "Pneumologie"),
#     's_80': ("Febră", "Boli infecțioase"),
#     's_109': ("Amețeală", "Neurologie"),
#     's_70': ("Durere lombară", "Reumatologie"),
#     's_92': ("Dureri musculare", "Medicină internă"),
#     's_10': ("Balonare", "Gastroenterologie"),
#     's_61': ("Vărsături", "Gastroenterologie"),
#     's_47': ("Palpitații", "Cardiologie"),
#     's_34': ("Durere abdominală", "Gastroenterologie"),
#     's_66': ("Oboseală", "Medicină internă"),
#     's_18': ("Sângerare nazală", "ORL"),
#     's_122': ("Dificultăți respiratorii", "Pneumologie"),
#     's_85': ("Arsuri la urinare", "Urologie")
# }

# def get_specialty_from_symptoms(symptoms):
#     """
#     Returnează diagnosticul și specialitatea pe baza unei hărți locale,
#     fără a mai apela API-ul.
#     """
#     print("📋 Simptome selectate:", symptoms)

#     for symptom in symptoms:
#         if symptom in SYMPTOM_DIAGNOSIS_SPECIALTY_MAP:
#             diagnosis, specialty = SYMPTOM_DIAGNOSIS_SPECIALTY_MAP[symptom]
#             print("✅ Diagnosticul returnat:", diagnosis)
#             print("✅ Specialitate recomandată:", specialty)
#             return diagnosis, specialty

#     print("⚠️ Niciun diagnostic potrivit găsit în harta locală.")
#     return None, None

# services/api.py

# SYMPTOM_DIAGNOSIS_SPECIALTY_MAP = {
#     ('s_21',): ("Migrenă", "Neurologie"),
#     ('s_12',): ("Indigestie", "Gastroenterologie"),
#     ('s_130',): ("Pierdere în greutate", "Nutriție"),
#     ('s_5', 's_15'): ("Toxiinfecție alimentară", "Boli infecțioase"),
#     ('s_10',): ("Eczemă", "Dermatologie"),
#     ('s_96', 's_22'): ("Gastrită", "Gastroenterologie"),
#     ('s_8',): ("Bronșită", "Pneumologie"),
#     ('s_110',): ("Angină pectorală", "Cardiologie"),
#     ('s_98',): ("Infecție urinară", "Urologie"),
#     ('s_101',): ("Alergie cutanată", "Dermatologie"),
#     ('s_90',): ("Durere toracică nespecifică", "Medicină internă"),
#     ('s_65',): ("Diaree acută", "Gastroenterologie"),
#     ('s_170',): ("Insomnie", "Psihiatrie"),
#     ('s_180',): ("Artrită", "Reumatologie"),
# }



# def get_specialty_from_symptoms(symptoms):
#     # Transformă în tuple sorted, ca să poți face match
#     normalized = tuple(sorted(symptoms))

#     # Caută match direct
#     if normalized in SYMPTOM_DIAGNOSIS_SPECIALTY_MAP:
#         diagnosis, specialty = SYMPTOM_DIAGNOSIS_SPECIALTY_MAP[normalized]
#         print("✅ Diagnostic:", diagnosis)
#         print("✅ Specialitate:", specialty)
#         return diagnosis, specialty

#     # Caută match parțial (prima combinație găsită)
#     for key, (diagnosis, specialty) in SYMPTOM_DIAGNOSIS_SPECIALTY_MAP.items():
#         if all(k in normalized for k in key):
#             print("🔁 Match parțial:", key)
#             return diagnosis, specialty

#     # Dacă nu s-a găsit nimic
#     print("❌ Nu s-a găsit o corespondență pentru:", normalized)
#     return None, None


SYMPTOM_DIAGNOSIS_SPECIALTY_MAP = {
      ('s_21',): ("Migrenă", "Neurologie"),
    ('s_12',): ("Indigestie", "Gastroenterologie"),
    ('s_130',): ("Subnutriție", "Nutriție"),
    ('s_5', 's_15'): ("Toxiinfecție alimentară", "Boli infecțioase"),
    ('s_10',): ("Eczemă", "Dermatologie"),
    ('s_96', 's_22'): ("Gastrită acută", "Gastroenterologie"),
    ('s_8',): ("Bronșită", "Pneumologie"),
    ('s_110',): ("Angină pectorală", "Cardiologie"),
    ('s_98',): ("Infecție urinară", "Urologie"),
    ('s_101',): ("Alergie cutanată", "Dermatologie"),
    ('s_90',): ("Durere toracică nespecifică", "Medicină internă"),
    ('s_65',): ("Cistită", "Urologie"),
    ('s_170',): ("Insomnie", "Psihiatrie"),
    ('s_180',): ("Artrită", "Reumatologie"),
    ('s_22', 's_31'): ("Gastroenterită", "Gastroenterologie"),
    ('s_38', 's_15'): ("Faringită virală", "ORL"),
    ('s_41',): ("Constipație cronică", "Gastroenterologie"),
    ('s_15',): ("Infecție virală", "Boli infecțioase"),
    ('s_22',): ("Gastrită acută", "Gastroenterologie"),
    ('s_23',): ("Vertij", "Neurologie"),
    ('s_31',): ("Colică abdominală", "Gastroenterologie"),
    ('s_38',): ("Faringită virală", "ORL"),
    ('s_55',): ("Mialgie", "Reumatologie"),
    ('s_60',): ("Tulburare de ritm cardiac", "Cardiologie"),
    ('s_70',): ("Tuberculoză", "Pneumologie"),
    ('s_85',): ("Tulburare de alimentație", "Psihiatrie"),
    ('s_107',): ("Infecție respiratorie", "Pneumologie"),
    ('s_150',): ("Insuficiență venoasă", "Cardiologie"),
    ('s_96',): ("Boală de reflux gastroesofagian", "Gastroenterologie"),
    ('s_5',): ("Oboseală cronică", "Medicină internă"),
    ('s_96', 's_31'): ("Apendicită", "Chirurgie generală"),
    ('s_8', 's_15'): ("Gripă", "Pneumologie"),
    ('s_5', 's_85', 's_130'): ("Anorexie", "Psihiatrie"),
    ('s_60', 's_110'): ("Tahicardie", "Cardiologie"),
    ('s_10', 's_101'): ("Dermatită alergică", "Dermatologie"),
    ('s_31', 's_12'): ("Sindrom de colon iritabil", "Gastroenterologie"),
    ('s_23', 's_90'): ("Hipotensiune", "Medicină internă"),
    ('s_65', 's_98'): ("Pielonefrită", "Urologie"),
    ('s_38', 's_107'): ("Laringită", "ORL"),
}

def get_specialty_from_symptoms(symptoms):
    normalized = tuple(sorted(symptoms))

    # Caută un match exact
    if normalized in SYMPTOM_DIAGNOSIS_SPECIALTY_MAP:
        diagnosis, specialty = SYMPTOM_DIAGNOSIS_SPECIALTY_MAP[normalized]
        return diagnosis, specialty

    # Caută prima combinație parțială care se potrivește
    for key, (diagnosis, specialty) in SYMPTOM_DIAGNOSIS_SPECIALTY_MAP.items():
        if all(k in normalized for k in key):
            return diagnosis, specialty

    return None, None
