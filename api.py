from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.pyfunc

# Chargement du modèle depuis le registry MLflow
model = mlflow.pyfunc.load_model("exported_model")


# Création de l'app FastAPI
app = FastAPI()

# Définition du schéma de requête
class TextInput(BaseModel):
    text: str

# Endpoint de prédiction
@app.post("/predict")
def predict(input: TextInput):
    prediction = model.predict([input.text])
    return {"prediction": int(prediction[0])}
