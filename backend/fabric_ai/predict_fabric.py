import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "fabric_model.keras")
model = tf.keras.models.load_model(MODEL_PATH)

# Class names
class_names = [
    "Abaca",
    "Cotton",
    "Hessian",
    "Linen",
    "Silk",
    "Wool"
]


def predict_fabric(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    prediction = model.predict(img_array, verbose=0)
    print("Raw prediction:", prediction)

    class_index = np.argmax(prediction)

    confidence = float(np.max(prediction) * 100)

    return {
        "prediction": class_names[class_index],
        "confidence": round(confidence, 2)
    }
if __name__ == "__main__":
    test_image = "fabric_ai/dataset/Cotton/Cotton_10.jpg"
    print(predict_fabric(test_image))