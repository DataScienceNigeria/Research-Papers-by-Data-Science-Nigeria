# COVNLP: A Multisource COVID-19 dataset for Natural Language Processing

This Paper is currently under review at the International Workshop on Social Impact of AI for Africa (SIAIA-22) at the Thirty-Sixth AAAI Conference on Artificial Intelligence (AAAI-22)

In this work, we propose `COVNLP`, a novel dataset for Natural language processing tasks.  
The openly available dataset consists of 3,199 de-identified peer-to-peer messages shared across different channels like Whatsapp, SMS and Social media channels 
from volunteers during the COVID-19 pandemic in Nigeria. The messages were labelled by both participants at submission and independent data annotators after submission 
under three(3) major themes; message genuity, type and impact. We discovered that the most trusted source of information for the participants during the COVID-19 pandemic 
were international stations, social media and websites. 31.20\% of the messages received by volunteers were labelled to have psychological effects such as emotional disturbance, 
depression, stress, mood alterations. The dataset is available here

As part of our experimentation, we developed a basic machine learning model to classify the messages into misinformation, disinformation and rumour classes based. 
The best performing algorithm was Logistic Regression with count vectorizer with Area under the curve (AUC) value of 0.813 compared to Naive Bayes Classifier (0.716 ) and Random Forest Classifier(0.710)
