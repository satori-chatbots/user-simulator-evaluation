
# Evaluation - Cooking Assistant

This test case evaluates [Cooking assistant](https://github.com/materight/cooking-assistant) which is a chatbot that provides recommendations about recipes given a set of ingredients.

### Technologies

* Rasa 2.x

### Installation

The original install instructions doesn't seem to work well.

Before installing the dependencies, it is better if 
you create a specific Python environment:

```bash
python -m venv venv 
source venv/bin/activate
```

Install manually specific Rasa versions.

```bash
pip install rasa==2.0
pip install rasa[spacy]
pip install protobuf==3.20.*
```

Apply these changes to requirements.txt
```
-numpy==1.19.5
+numpy
 pandas==1.3.1
 PyYAML==6.0
-rasa==2.8.27
-rasa[spacy]==2.8.27
-transformers==4.19.4
-scikit-learn==0.24.2
+#rasa==2.8.27
+#rasa[spacy]
+#==2.8.27
+transformers
+scikit-learn
 chatette==1.6.3
-word2number==1.1
+word2number
```

Then:

```bash
    pip install -r requirements.txt
    python -m spacy download en_core_web_md
    python generate_data.py
    rasa train
```


### Running the chatbot

To execute the chatbot:

```bash
    rasa run actions
    rasa shell
```
