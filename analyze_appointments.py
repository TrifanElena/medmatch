import os
import pandas as pd
import matplotlib.pyplot as plt

print("► Script începe…")
print("► CWD:", os.getcwd())
print("► Fișiere în director:", os.listdir())

CSV_PATH = 'appointments.csv'

if not os.path.exists(CSV_PATH):
    print(f"❌ Fișierul {CSV_PATH} nu există în folderul curent!")
    exit(1)

try:
    df = pd.read_csv(CSV_PATH, parse_dates=['date'])
    print("✅ Am încărcat CSV-ul cu", len(df), "rânduri.")
except Exception as e:
    print("❌ Eroare la citirea CSV-ului:", e)
    exit(1)

print("► Primele 5 rânduri:")
print(df.head())

# Verifică coloane
print("► Coloane CSV:", df.columns.tolist())

# Afișează tipurile de date
print("► Tipuri de date:")
print(df.dtypes)

# Dacă totul e OK, continuăm:
daily_rate = df.groupby(df['date'].dt.date)['fulfilled'].mean() * 100
print("\nRata de prezență pe zi (%):")
print(daily_rate.round(2))

plt.figure()
daily_rate.plot(kind='bar')
plt.title('Rata de prezență la consultații pe zi')
plt.xlabel('Dată')
plt.ylabel('Rată de prezență (%)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('attendance_rate_per_day.png')
print("✅ Grafic salvat ca attendance_rate_per_day.png")
plt.show()
