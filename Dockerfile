# Utilise une image Python officielle
FROM python:3.10-slim

# Crée un dossier de travail
WORKDIR /app

# Copie les fichiers requis
COPY api.py .
COPY exported_model ./exported_model
COPY requirements.txt .
#COPY "MLmodel" ./MLmodel  # facultatif

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Lancer l’API
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
