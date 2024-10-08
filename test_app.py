import requests
import json

# Base URL of the API
BASE_URL = 'http://localhost:2005'

# Function to test /list_label endpoint (GET request)
def test_list_labels():
    url = f"{BASE_URL}/list_label"
    response = requests.get(url)
    
    if response.status_code == 200:
        labels = response.json().get('labels', [])
        print(f"Labels: {labels}")
    else:
        print(f"Failed to list labels. Status code: {response.status_code}")

# Function to test /classify endpoint (POST request)
def test_classify_text(input_text):
    url = f"{BASE_URL}/classify"
    headers = {'Content-Type': 'application/json'}
    data = {"text": input_text}
    
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 200:
        result = response.json()
        print(f"Input Text: {result['text']}")
        print(f"Predicted Label: {result['predicted_label']}")
        print(f"Probability: {result['prob']}")
    else:
        print(f"Failed to classify text. Status code: {response.status_code}")

# Run the test functions
if __name__ == '__main__':
    print("Testing /list_label endpoint:")
    test_list_labels()
    
    print("\nTesting /classify endpoint with text 'I love this product!':")
    test_classify_text("An apple a day keeps doctor away.")
