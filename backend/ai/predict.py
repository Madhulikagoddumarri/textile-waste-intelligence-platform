import os
import numpy as np
import tensorflow as tf
from PIL import Image

# Model path
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "models",
    "fabric_defect_model.keras"
)

CLASS_NAMES = ["Defect", "NoDefect"]

# Model is NOT loaded when the application starts
model = None


def get_model():
    global model

    if model is None:
        print("Loading fabric defect model...")
        model = tf.keras.models.load_model(MODEL_PATH)
        print("Fabric defect model loaded successfully.")

    return model


def predict_image(image_path):

    # Load model only when prediction is requested
    current_model = get_model()

    img = Image.open(image_path).convert("RGB")

    img = img.resize((224, 224))

    img = np.array(img) / 255.0

    img = np.expand_dims(img, axis=0)

    prediction = current_model.predict(img, verbose=0)

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