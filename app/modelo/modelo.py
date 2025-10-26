import pickle
import re
import pathlib

_version_ = "0.1.0"

BASE_DIR = pathlib.Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / f"modelo-{_version_}.pkl"


with open(f"{BASE_DIR}/modelo-{_version_}.pkl", "rb") as f:
    model = pickle.load(f)

classes = [
    "Arabic",
    "Danish",
    "English",
    "French",
    "Italian",
    "German",
    "Portuguese",
    "Spanish",
]

def predict_pipeline(texto):
    texto = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", texto)
    texto = re.sub(r"[[]]", " ", texto)
    texto = texto.lower()
    pred = model.predict([texto])
    return classes[pred[0]]