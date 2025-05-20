# services/infermedica_client.py
import requests

API_URL = "https://api.infermedica.com/v3"
APP_ID = "c6226d3c"
APP_KEY = "f83318d47b5a04ee66cab2a0d95f52ee"

HEADERS = {
    "App-Id": APP_ID,
    "App-Key": APP_KEY,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def get_all_symptoms():
    response = requests.get(f"{API_URL}/symptoms", headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return []

def get_diagnosis(symptoms, age, sex):
    evidence = [{"id": s_id, "choice_id": "present"} for s_id in symptoms]
    payload = {
        "sex": sex,
        "age": {"value": age},
        "evidence": evidence
    }
    response = requests.post(f"{API_URL}/diagnosis", headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json()
    return None
