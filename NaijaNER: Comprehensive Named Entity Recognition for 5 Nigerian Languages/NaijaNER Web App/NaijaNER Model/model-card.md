# NaijaNER Model Card

## Model Details

NaijaNER is a Named Entity Recognition(NER) model trained on the combination of Nigerian English, Hausa, pidgin, Igbo, Yoruba languages, 
The research and innovation team at Data Science Nigeria developed the model as a base model to locate and highlight
named entities (person names, organizations, locations, time expressions, quantities, monetary values, percentages, etc) in unstructured text in the languages.
We found that a combined Named Entity Recognition that works with different languages can be a valuable tool in low resourced language systems and can help drive inclusion, ease of deployment in production and reusability of NER models 

### Model date
February 2021

### Model type
Language model

### Model version
Verson 0.1

### Paper & samples
[NaijaNER : Comprehensive Named Entity Recognition for 5 Nigerian Languages.](https://www.researchgate.net/publication/350557499_NaijaNER_Comprehensive_Named_Entity_Recognition_for_5_Nigerian_Languages)
[NaijaNER demo app](https://nigner.herokuapp.com/)
## Model Use
The intended direct users of NaijaNER are developers who intend to integrate a combined language model of the 5 major Nigerian languages(Nigerian English, Hausa, pidgin, Igbo, Yoruba) in their applications and based on the limitations listed below, improve the model by gathering more data in the above named languages to improve the model. 
NaijaNER model should not be used on other languages except the above named languages for expected result
## Data, Performance, and Limitations

### Data 
The NaijaNER model is training and evaluation dataset is composed of text, majorly news articles posted to the internet.  
 
### Performance
Given its training data, NaijaNER’s outputs and performance are versatile for multilanguage applications 
and has a good performance on each of the languages compared to individual language models, which showed better performance on their specific languages
but will require deployment of multiple models. 

## Limitations
NaijaNER model was majorly to share our learning on how information extraction using Named Entity Recognition can be optimized for the multilanguage applications,
The model was intended to be a base model which requires further work, it was trained and evaluated on limited data, 2500 news articles(50 news articles per Language)therefore resulting to low F1score. 
## Where to send questions or comments about the model
Please use this 
