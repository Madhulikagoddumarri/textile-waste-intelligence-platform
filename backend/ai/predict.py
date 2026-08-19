import os
import numpy as np
import tensorflow as tf
from PIL import Image

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "models",
    "fabric_defect_model.keras"
)

CLASS_NAMES = ["Defect", "NoDefect"]

model = None


def get_model():
    global model

    if model is None:
        model = tf.keras.models.load_model(MODEL_PATH)

    return model


def predict_image(image_path):

    model = get_model()

    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))

    img = np.array(img, dtype=np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img, verbose=0)

    predicted_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = float(np.max(prediction))

    return {
        "prediction": predicted_class,
        "confidence": round(confidence * 100, 2)
    }


if __name__ == "__main__":

    image = input("Enter image path: ").strip().strip('"')

    result = predict_image(image)

    print(result)