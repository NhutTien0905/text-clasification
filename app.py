from flask import Flask, request, jsonify
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
from keras.src.legacy.preprocessing.text import one_hot
from tensorflow.python.keras.models import load_model
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import re

app = Flask(__name__)

# Load your trained TensorFlow model
model = load_model('model/model.h5')

# Load your tokenizer (assuming you have saved it during preprocessing)
ps = PorterStemmer()
dict_size = 5000

def preprocess_text(text):
    cleaned = []
    for i in range(0,len(text)):
        msg = re.sub('[^a-zA-Z]',' ',text[i])
        msg = msg.lower()
        msg = msg.split()
        msg = [ps.stem(words) for words in msg if not words in set(stopwords.words('english'))]
        msg = ' '.join(msg)
        cleaned.append(msg)

    one_hot_mat = [one_hot(words,dict_size) for words in cleaned]
    embedded_layer = pad_sequences(one_hot_mat,padding = 'pre',maxlen = 201)
    return embedded_layer

# Get the list of labels (assume you have a list of labels)
labels = ['Business','Science','Entertainment','Health']  # Replace with your actual labels

# Maximum sequence length (set according to your training data)
MAX_SEQ_LENGTH = 201

# 2-5-1. List labels
@app.route('/list_label', methods=['GET'])
def list_labels():
    return jsonify({"labels": labels})

# 2-5-2. Classify text
@app.route('/classify', methods=['POST'])
def classify_text():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Tokenize the input text
    padded_sequences = preprocess_text([text])
    print(padded_sequences.shape)

    # Run the classification
    predictions = model.predict(padded_sequences)
    predicted_label_index = tf.argmax(predictions[0]).numpy()
    predicted_label = labels[predicted_label_index]
    prob = float(tf.reduce_max(predictions).numpy())

    return jsonify({
        "text": text,
        "predicted_label": predicted_label,
        "prob": prob
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2005)
