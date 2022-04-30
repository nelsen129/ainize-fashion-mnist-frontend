import base64
import json
import requests
import streamlit as st
import tensorflow.keras as keras

from PIL import Image

api = 'https://main-ainize-fashion-mnist-nelsen129.endpoint.ainize.ai/predict'

categories = ['T-shirt/Top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle Boot']


def process_image(image_path):
    img = Image.open(image_path)
    img_arr = keras.utils.img_to_array(img)
    img_arr = keras.preprocessing.image.smart_resize(img_arr, (28, 28))
    img = keras.utils.array_to_img(img_arr)
    img = img.convert('L')  # grayscale
    img_bytes = img.tobytes()
    img_b64 = base64.b64encode(img_bytes).decode('utf8')

    return img_b64


def send_request(image_path):
    img_b64 = process_image(image_path)

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    payload = json.dumps({"image": img_b64})
    response = requests.post(api, data=payload, headers=headers)
    status_code = response.status_code
    return status_code, response


# send_request(test_image_path)

st.title("Fashion-MNIST Classification")
st.header("Classify Fashion-MNIST using TensorFlow and Convolutional Neural Networks")

image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
if image_file is not None:
    # To View Uploaded Image
    st.image(Image.open(image_file), width=500)

    if st.button("Submit"):
        status_code, response = send_request(image_file)
        if status_code == 200:
            prediction = response.json()
            max_score = max(prediction["prediction"])
            category = categories[[i for i in range(len(categories)) if prediction["prediction"][i] == max_score][0]]
            st.success(category)
        else:
            st.error(str(status_code) + " Error")

else:
    st.text("Upload image to run prediction!")

