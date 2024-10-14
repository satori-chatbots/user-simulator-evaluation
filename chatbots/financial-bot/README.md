
# Evaluation - Financial bot

This test case evaluates [Financial bot](https://github.com/dDeuce222/Financial-chatbot),
a chatbot which is intended to be model or framework to build concrete financial services.

### Technologies

* Rasa 3.x

### Installation

The install instructions are available in the original [Github repository](https://github.com/dDeuce222/Financial-chatbot?tab=readme-ov-file#install-dependencies).
To make it work we needed to do some small changes.

Here is the diff:
```
diff --git a/actions/requirements-actions.txt b/actions/requirements-actions.txt
index bcbded1..dd92745 100644
---d a/actions/requirements-actions.txt
+++ b/actions/requirements-actions.txt
@@ -2,4 +2,4 @@ python-dateutil==2.8.1
 numpy~=1.19.2
 pytz~=2019.3
 ruamel.yaml
-sqlalchemy~=1.3.22
+sqlalchemy
diff --git a/requirements.txt b/requirements.txt
index ac018fe..ac771be 100644
--- a/requirements.txt
+++ b/requirements.txt
@@ -1,6 +1,10 @@
 -r actions/requirements-actions.txt
 
-rasa[spacy]==3.1.0
+rasa[spacy]==3.2.0
 
 # Sync with `Dockerfile`
-rasa-sdk==3.1.0
+rasa-sdk==3.2.0
```

Before installing the dependencies, it is better if 
you create a specific Python environment:

```bash
python -m venv venv 
source venv/bin/activate
```

Then, you can install the dependencies:

```bash
pip install -r requirements.txt
```

Moreover, to fix errors when running the chatbot we manually installed:

```bash
pip install websockets==10.0
python -m spacy download en_core_web_md
```

### Running the chatbot

Before running the user simulator with this chatbot you need to execute three services (in different terminals):

```bash
rasa run actions --port 5056
docker run -p 8000:8000 rasa/duckling

rasa run --enable-api
```

If you want to test the chatbot interactively, you can use use `rasa shell --debug` instead of `rasa run`.

## User simulator execution

```
python3 ../user-simulator/src/autotest.py --technology rasa --chatbot http://0.0.0.0:5005/webhooks/rest/webhook --user chatbots/financial-bot/conversations/ --extract output/financial-bot
```
