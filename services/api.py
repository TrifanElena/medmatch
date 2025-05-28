# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# SYMPTOM_DIAGNOSIS_SPECIALTY_MAP = {
#       ('s_21',): ("Migrenă", "Neurologie"),
#     ('s_12',): ("Indigestie", "Gastroenterologie"),
#     ('s_130',): ("Subnutriție", "Nutriție"),
#     ('s_5', 's_15'): ("Toxiinfecție alimentară", "Boli infecțioase"),
#     ('s_10',): ("Eczemă", "Dermatologie"),
#     ('s_96', 's_22'): ("Gastrită acută", "Gastroenterologie"),
#     ('s_8',): ("Bronșită", "Pneumologie"),
#     ('s_110',): ("Angină pectorală", "Cardiologie"),
#     ('s_98',): ("Infecție urinară", "Urologie"),
#     ('s_101',): ("Alergie cutanată", "Dermatologie"),
#     ('s_90',): ("Durere toracică nespecifică", "Medicină internă"),
#     ('s_65',): ("Cistită", "Urologie"),
#     ('s_170',): ("Insomnie", "Psihiatrie"),
#     ('s_180',): ("Artrită", "Reumatologie"),
#     ('s_22', 's_31'): ("Gastroenterită", "Gastroenterologie"),
#     ('s_38', 's_15'): ("Faringită virală", "ORL"),
#     ('s_41',): ("Constipație cronică", "Gastroenterologie"),
#     ('s_15',): ("Infecție virală", "Boli infecțioase"),
#     ('s_22',): ("Gastrită acută", "Gastroenterologie"),
#     ('s_23',): ("Vertij", "Neurologie"),
#     ('s_31',): ("Colică abdominală", "Gastroenterologie"),
#     ('s_38',): ("Faringită virală", "ORL"),
#     ('s_55',): ("Mialgie", "Reumatologie"),
#     ('s_60',): ("Tulburare de ritm cardiac", "Cardiologie"),
#     ('s_70',): ("Tuberculoză", "Pneumologie"),
#     ('s_85',): ("Tulburare de alimentație", "Psihiatrie"),
#     ('s_107',): ("Infecție respiratorie", "Pneumologie"),
#     ('s_150',): ("Insuficiență venoasă", "Cardiologie"),
#     ('s_96',): ("Boală de reflux gastroesofagian", "Gastroenterologie"),
#     ('s_5',): ("Oboseală cronică", "Medicină internă"),
#     ('s_96', 's_31'): ("Apendicită", "Chirurgie generală"),
#     ('s_8', 's_15'): ("Gripă", "Pneumologie"),
#     ('s_5', 's_85', 's_130'): ("Anorexie", "Psihiatrie"),
#     ('s_60', 's_110'): ("Tahicardie", "Cardiologie"),
#     ('s_10', 's_101'): ("Dermatită alergică", "Dermatologie"),
#     ('s_31', 's_12'): ("Sindrom de colon iritabil", "Gastroenterologie"),
#     ('s_23', 's_90'): ("Hipotensiune", "Medicină internă"),
#     ('s_65', 's_98'): ("Pielonefrită", "Urologie"),
#     ('s_38', 's_107'): ("Laringită", "ORL"),
# }


# EXCLUDED_SYMPTOMS = {'s_65', 's_98' }
# def get_specialty_from_symptoms(symptoms, age=30, sex="female"):
#     """
#     Încearcă să obțină diagnosticul și specialitatea recomandată folosind API-ul Infermedica.
#     Dacă eșuează, revine la fallback-ul local.
#     """
#     # app_id = os.getenv("INFERMEDICA_APP_ID")
#     # app_key = os.getenv("INFERMEDICA_APP_KEY")

#     # # fallback dacă lipsesc cheile
#     # if not app_id or not app_key:
#     #     print("⚠️ Cheile API lipsesc — folosim fallback local.")
#     #     return local_fallback(symptoms)
#     app_id = os.getenv("INFERMEDICA_APP_ID")
#     app_key = os.getenv("INFERMEDICA_APP_KEY")
#     print(f"🛠️ DEBUG ENV → App ID: {app_id!r}, App Key: {app_key!r}")
#     if not app_id or not app_key:
#         print("⚠️ Cheile API lipsesc — folosim fallback local.")
#         return local_fallback(symptoms)


#     headers = {
#         "App-Id": app_id,
#         "App-Key": app_key,
#         "Content-Type": "application/json",
#         "Accept": "application/json",
#     }

#     # evidence = [{"id": s, "choice_id": "present"} for s in symptoms]
#     # filtrăm simptomele excluse
#     filtered = [s for s in symptoms if s not in EXCLUDED_SYMPTOMS]

# # dacă nu a rămas nimic, apelăm fallback
#     if not filtered:
#         return local_fallback(symptoms)

# # construim evidence doar cu simptome permise
#     evidence = [{"id": s, "choice_id": "present"} for s in filtered]

    

#     body = {
#         "sex": sex,
#         "age": { "value": age },
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

#                 # opțional: traduceri EN -> RO + mapare la specialitate
#                 diagnosis_map = {
#                     "Common cold": ("Răceală comună", "Pneumologie"),
#                     "Migraine": ("Migrenă", "Neurologie"),
#                     "Gastritis": ("Gastrită", "Gastroenterologie"),
#                     "Sinusitis": ("Sinuzită", "ORL"),
#                     "Urinary tract infection": ("Infecție urinară", "Urologie"),
#                     "Asthma": ("Astm", "Pneumologie"),
#                     "Flu": ("Gripă", "Pneumologie"),
#                     "COVID-19": ("COVID-19", "Pneumologie"),
#                     # adaugă ce vrei aici
#                 }

#                 diagnosis, specialty = diagnosis_map.get(diagnosis_en, (diagnosis_en, None))

#                 if specialty:
#                     print("✅ Traducere și specialitate:", diagnosis, "→", specialty)
#                     return diagnosis, specialty
#                 else:
#                     print("⚠️ Nu avem specialitate pentru acest diagnostic — fallback.")
#                     return local_fallback(symptoms)
#             else:
#                 print("⚠️ API nu a returnat condiții — fallback.")
#                 return local_fallback(symptoms)

#         else:
#             print("❌ Eroare status:", response.status_code, "— fallback.")
#             return local_fallback(symptoms)

#     except Exception as e:
#         print("❌ Eroare la conectare API:", str(e))
#         return local_fallback(symptoms)
    

# def local_fallback(symptoms):
#     normalized = tuple(sorted(symptoms))

#     # match exact
#     if normalized in SYMPTOM_DIAGNOSIS_SPECIALTY_MAP:
#         diagnosis, specialty = SYMPTOM_DIAGNOSIS_SPECIALTY_MAP[normalized]
#         print("🔁 Fallback exact:", diagnosis, specialty)
#         return diagnosis, specialty

#     # match parțial
#     for key, (diagnosis, specialty) in SYMPTOM_DIAGNOSIS_SPECIALTY_MAP.items():
#         if all(k in normalized for k in key):
#             print("🔁 Fallback parțial:", diagnosis, specialty)
#             return diagnosis, specialty

#     print("⚠️ Fallback: niciun match.")
#     return None, None

import os
import requests
from dotenv import load_dotenv
import logging

# ─── ÎNCĂRCARE MEDIU ȘI CONFIGURARE LOGGER ───────────────────────────
load_dotenv()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)
# ────────────────────────────────────────────────────────────────────────

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

# Lista de simptome care nu vor fi trimise niciodată la Infermedica
EXCLUDED_SYMPTOMS = {'s_65', 's_98'}


def get_specialty_from_symptoms(symptoms, age=30, sex="female"):
    """
    Încearcă să obțină diagnosticul și specialitatea recomandată folosind API-ul Infermedica.
    Dacă eșuează sau nu se obține un diagnostic, revine la fallback-ul local.
    """
    app_id = os.getenv("INFERMEDICA_APP_ID")
    app_key = os.getenv("INFERMEDICA_APP_KEY")

    # Logăm doar faptul că s-au încărcat credențialele, fără a afișa cheia
    logger.debug("ENV ➤ App credentials loaded")

    # Dacă lipsește App ID sau App Key, folosim fallback-ul local
    if not app_id or not app_key:
        logger.warning("Cheile API lipsesc — fallback local.")
        return local_fallback(symptoms)

    # Filtrăm simptomele excluse
    filtered = [s for s in symptoms if s not in EXCLUDED_SYMPTOMS]
    if not filtered:
        logger.warning("Toate simptomele excluse — fallback local.")
        return local_fallback(symptoms)

    # Construim payload-ul pentru Infermedica
    evidence = [{"id": s, "choice_id": "present"} for s in filtered]
    body = {
        "sex": sex,
        "age": {"value": age, "unit": "year"},
        "evidence": evidence
    }

    headers = {
        "App-Id": app_id,
        "App-Key": app_key,
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    try:
        response = requests.post(
            "https://api.infermedica.com/v3/diagnosis",
            headers=headers,
            json=body
        )

        if response.status_code == 200:
            data = response.json()
            conditions = data.get("conditions", [])

            if conditions:
                diagnosis_en = conditions[0]["name"]
                logger.info("Recomandare API: %s", diagnosis_en)

                # Mapare EN → RO + specialitate
                diagnosis_map = {
                    "Common cold": ("Răceală comună", "Pneumologie"),
                    "Migraine": ("Migrenă", "Neurologie"),
                    "Gastritis": ("Gastrită", "Gastroenterologie"),
                    "Sinusitis": ("Sinuzită", "ORL"),
                    "Urinary tract infection": ("Infecție urinară", "Urologie"),
                    "Asthma": ("Astm", "Pneumologie"),
                    "Flu": ("Gripă", "Pneumologie"),
                    "COVID-19": ("COVID-19", "Pneumologie"),
                    # adaugă traduceri suplimentare după necesitate
                }

                diagnosis, specialty = diagnosis_map.get(
                    diagnosis_en, (diagnosis_en, None)
                )

                if specialty:
                    logger.info("Traducere și specialitate: %s → %s", diagnosis, specialty)
                    return diagnosis, specialty
                else:
                    logger.warning("Fără specialitate pentru '%s' — fallback local.", diagnosis_en)
                    return local_fallback(symptoms)

            else:
                logger.warning("API nu a returnat condiții — fallback local.")
                return local_fallback(symptoms)

        else:
            logger.error("Eroare API status %s — fallback local.", response.status_code)
            return local_fallback(symptoms)

    except Exception as e:
        logger.error("Eroare la conectare API: %s", e)
        return local_fallback(symptoms)


def local_fallback(symptoms):
    """
    În cazul în care API-ul nu furnizează un rezultat, folosim un fallback local
    bazat pe harta de simptome predefinită.
    """
    normalized = tuple(sorted(symptoms))

    # Căutare exactă
    if normalized in SYMPTOM_DIAGNOSIS_SPECIALTY_MAP:
        diagnosis, specialty = SYMPTOM_DIAGNOSIS_SPECIALTY_MAP[normalized]
        logger.debug("Fallback exact: %s → %s", diagnosis, specialty)
        return diagnosis, specialty

    # Căutare parțială
    for key, (diagnosis, specialty) in SYMPTOM_DIAGNOSIS_SPECIALTY_MAP.items():
        if all(k in normalized for k in key):
            logger.debug("Fallback parțial: %s → %s", diagnosis, specialty)
            return diagnosis, specialty

    logger.warning("Fallback local nereușit: niciun match găsit.")
    return None, None
