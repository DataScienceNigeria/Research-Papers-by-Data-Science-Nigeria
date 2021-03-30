# NaijaNER: Comprehensive Named Entity Recognition for 5 Nigerian Languages
NaijaNER streamlit app deployed on Heroku

Web App link: https://nigner.herokuapp.com/

The NaijaNER Web App folder contains:
- `ner_app.py` file which is the source code for the Named Entity Recognition App using Streamlit
- `Procfile` which contains the process types in the app, used to deploy to Heroku
- `setup.sh` helps create the necessary environment for our streamlit app to run
- `requirements.txt` contains a list of all the specific python plugins required to run the streamlit application
- `HausaNER`,`IgboNER`,`NGNEnglishNER`,`PidginNER`,`YorubaNER` Model folders contains NER models for each language and 
- `NaijaNER` folder, a combined NER model for all 5 languages.

- `HausaNER` model identifies Hausa named entities in context, with `F1score of 44.84%` and `52.59% Precision`
- `IgboNER` model identifies Igbo named entities in context, with `F1score of 35.48%` and `47.18% Precision`
- `NGNEnglishNER` model identifies Nigerian English named entities in context, with `F1score of 54.49%` and `55.48% Precision`
- `PidginNER` model identifies Pidgin named entities in context, with `F1score of 67.13%` and `70.29% Precision`
- `NaijaNER` model is trained on the combination of Nigerian English, Hausa, pidgin, Igbo, Yoruba languages. `F1score of 53.75%` and `62.43% Precision`



