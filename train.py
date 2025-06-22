import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Chargement du dataset
df = pd.read_csv('IMDB Dataset.csv')

# Prétraitement simple
X = df['review']
y = df['sentiment'].map({'positive': 1, 'negative': 0})

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorisation
vectorizer = TfidfVectorizer(max_features=10000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Modèle
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Sauvegarde du modèle et du vectorizer
with open('exported_model/model.pkl', 'wb') as f:
    pickle.dump(model, f)
with open('exported_model/vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Training terminé, modèle sauvegardé !")
