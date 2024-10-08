# Tools and Resources
OS: Ubuntu 22.04

Framework:
- Tensorflow 2.13.1
- NLTK
- Flask

Dataset: [News Aggregator Data Set](https://archive.ics.uci.edu/ml/datasets/News+Aggregator)

# Contribution
## Training model
Check out `training_notebook.ipynb` to see the preprocessing method and the architecture of model

## Run Flask server
Run app at `http://localhost:2005`:
```bash
python3 app.py
```

Test application:
```bash
python3 test_app.py
```

Results:
```bash
Testing /list_label endpoint:
Labels: ['Business', 'Science', 'Entertainment', 'Health']

Testing /classify endpoint with text 'I love this product!':
Input Text: An apple a day keeps doctor away.
Predicted Label: Health
Probability: 0.40282243490219116
```
