import streamlit as st
import spacy
import bs4
from io import StringIO
import os,base64
import time
#from typing import List, Sequence, Tuple, Optional, Dict, Union, Callable
import spacy_streamlit
#from spacy import displacy
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

from streamlit import caching
from datetime import date

#Clear cache after one day
def cache_clear_dt(dummy):
   clear_dt = date.today()
   return clear_dt

if cache_clear_dt("dummy")<date.today():
   caching.clear_cache()

timestamp = time.strftime("%Y%m%d-%H%M%S")

file_name = 'document'+ timestamp + ".txt"


@st.cache(allow_output_mutation=True)
def load_model(model_name):
    return spacy.load(model_name)

#@st.cache(allow_output_mutation=True)
def NER(model,raw_text):
  doc = model(raw_text)
  with st.beta_expander("Show/Hide Result",expanded=True):
      spacy_streamlit.visualize_ner(doc,labels=model.get_pipe('ner').labels)
  return doc

@st.cache # to make the function run faster
def get_text(url):
    page = urlopen(url)
    soup = BeautifulSoup(page,features="html.parser")
    fetched_text = " ".join(map(lambda p:p.text, soup.find_all('p')))
    return fetched_text

@st.cache(suppress_st_warning=True)
def download_file(df):
    obj_to_download = df.to_csv(index=False)
    b64 = base64.b64encode(obj_to_download.encode()).decode()
    href = f'<a href="data:file/readfile;base64,{b64}">Download</a>'
    return href

def get_result(doc):
    txt, start, end, label = [], [], [], []
    for ent in doc.ents:
        txt.append(ent.text)
        start.append(ent.start_char)
        end.append(ent.end_char)
        label.append(ent.label_)
        df = pd.DataFrame(txt)
        df.columns = ["entities"]
        df["start_char"] = start
        df["end_char"] = end
        df["label"] = label
    download_link = download_file(df)
    st.markdown(download_link, unsafe_allow_html=True)
    st.markdown("<p style='font-size:12px;'>See GLOSSARY for entity description.</p>", unsafe_allow_html=True)


#@st.cache(suppress_st_warning=True)
def get_about_page():
    df1 =["PERSON","NORP","FAC","ORG","GPE","LOC","PRODUCT","DATE","TIME","PERCENT","MONEY","QUANTITY","ORDINAL","CARDINAL","EVENT","WORK_OF_ART","LAW","LANGUAGE"]
    df2 =["These are proper names of people, including fictional people, first names, last names, individual or family names, unique nicknames.",
    "This type represents adjectival forms of GPE and Location names, as well as adjectival forms of named religions, heritage and political affiliation.",
    "Names of man-made structures: infrastructure (streets, bridges), buildings, monuments, etc. belong to this type.",
    "These are names of companies, government agencies, educational institutions, sports teams.",
    "Names of countries, cities, states, provinces, municipalities.",
    "Names of geographical locations other than GPEs.",
    "This can be the name of any product, generally a model name or model name and number.",
    "Used to classify a reference to a date or period, etc. Age also falls under this category, even when it’s a noun phrase referring to a person.",
    "Any time ending with 'a.m.' or 'p.m.' If the 'a.m.' or 'p.m.' is explicit, it must be tagged along with the numbers. Other times of day (units smaller than a day) and time durations less than 24 hours are also marked: morning, noon, night, 3 hours, a minute.",
    "Any percentage",
    "Any monetary value including all monetary denominations.",
    "Used to classify measurements with standardized units.",
    "All ordinal numbers, including adverbials.",
    "Numerals, including whole numbers, fractions, and decimals, that provide a count or quantity and do not fall under a unit of measurement, money, per cent, date or time.",
    "Named hurricanes, battles, wars, sports events, attacks.",
    "Titles of books, songs, television programs and other creations.",
    "Any document that has been made into a law, including named treaties and sections and chapters of named legal documents.",
    "Any named language."]
    entity = pd.DataFrame({'OntoNotes Named Entities' : df1,'Description' : df2},index=None)
    entity.set_index('OntoNotes Named Entities', inplace=True)
    st.table(entity)

 
def show_slider(raw_text):
    text_len = st.slider("Increase Slider to reduce text preview", 1, 500)
    #len_of_text = len(raw_text)
    len_of_preview = round(len(raw_text)/text_len)
    st.write(raw_text[:len_of_preview])
    
yor_1 = """Adelé alága APC l'Eko ní àdéhùn wà láàrín Buhari àti Tinubu lórí ìdíje ipò ààrẹ lọ́dún 2023 
Adele alaga ẹgbẹ oṣelu APC nipinlẹ Eko, ọgbẹni Tunde Balogun ti ṣalaye pe aarẹ Muhammadu Buhari, 
Asiwaju Bola Tinubu atawọn eekan mii ninu ẹgbẹ jọ ṣe adehun lọdun 2014 pe apa iwọ oorun Gusu ni oludije fun ipo aarẹ 
lọdun 2023 yoo ti wa. Ọgbẹni Balogun sọ pe ko ni boju mu ti ẹgbẹ APC ba kọ eti ikun si adehun yii. Awọn kan ti n sọ 
pe awọn ogunna gbongbo ọmọ ẹgbẹ APC kan ti n gbimọ lati gba ipo adari ẹgbẹ naa ati lati bẹrẹ iṣẹ lori idibo gbogbogbo 
ọdun 2023. Ẹwẹ, igbimọ alaṣẹ ẹgbẹ oṣelu APC, NEC labẹ adari aarẹ Buhari ṣe afiku akoko ti igbimọ amuṣẹya ti Mai Mala 
Buni ṣagbatẹru pẹlu oṣu mẹfa sii. Bakan naa ni igbimọ NEC buwọlu agbekalẹ igbimọ alaṣẹ to ti di tutuka tẹlẹ. Amọ, 
ohun ti alaga APC ipinlẹ Eko n sọ ni pe ki awọn agbaagba to da ẹgbẹ oṣelu APC silẹ ma gbagbe adehun ọdun 2014. """

yor_2 = """ Manchester United ra Ahmad Diallo lọ́wọ́ Atalanta fun ọ̀dun mẹ̀rin abọ̀, Ẹgbẹ agbabọọlu Manchester United ti 
fi ẹnu adehun jona lori rira Amad Diallo, agbabọọlu Atalanta bayii. Ni bi a ṣe n sọrọ yii ẹgbẹ agbabọọlu Manchester 
United ti kede rẹ faye gbọ pe Diallo ti gunlẹ si gbagede Old Trafford lati ikọ Atalanta lorilẹede Italy . 
Ole Gunnar Solskjaer, akọnimọọgba Manchester United ni oinu oun dun pe adehun idunadura naa bọ si nitori pe: 
"Ni igbagbọ oun, Diallo wa lara awọn ọdọ agbabọọlu taye n wari fun lọwọ lagbaye." Ọdun mẹrin abọ ni adehun naa ti 
wọn ṣe pẹlu agbabọọlu ọmọ orilẹede Cotedivoire naa. Ninu ọrọ tirẹ, Ahmad Diallo ni ọdun to kọja loun ti n reti ki 
adehun naa bọsi nitori o da oun loju pe ẹgbẹ agbabọọẹu to ṣe rẹgi fun idagbasoke oun ni Manchester United jẹ."""

pidgin1= """While many pipo dey speculate say di beef between Davido and Burna Boy bin start
since di announcement of di 2020 Grammys Award, wey Burna Boy, African Giant dey nominated, 
but di real time wey every pesin see am na for May 2020."""

pidgin2 = """Coming to America 2: See tins you need to know about di movie trailer wey just drop.
Eddie Murphy go return back to im royal homeland of Zamunda for "Coming 2 America." Di first official 
trailer for di feem don land, and former Prince Akeem (wey Murphy play) na di new-crown king - King Akeem"""

hausa1 = """Ashiru Nagoma: Mene ne ke damun tsohon darakta a Kannywood?14 Janairu 2021Asalin hoton, 
Aminu BarciTun bayan da hotunan wani tsohon darakta a masana'antar shirya fina-finan Hausa ta Kannywood Ashiru 
Nagoma suka bayyana da ke nuna shi cikin hali na fitar hayyaci, maganganu suka fara yaÉ—uwa a tsakanin al'umma 
kan ainihin abin da ke damunsa.Rahotanni dai sun ce Ashiru Nagoma ya daÉ—e a cikin yanayi mai kama da matsalar, 
inda a wasu lokutan har za a gan shi tamkar "ba ya cikin """

hausa2 ="""Daga Bakin mai Ita tare da Ibrahim MandawariNa'urarku na da matsalar sauraren sauti...
Daga Bakin mai Ita tare da Ibrahim Mandawari7 Janairu 2021Ku latsa hoton da ke sama don kallon bidiyon:Daga bakin 
mai ita wani shiri na BBC Hausa da ke kawo muku hira da fitattun mutane kan wasu abubuwan da suka shafi rayuwarsu 
zallah.A wannan kashi na 31, shirin ya tattauna da fitaccen dan fim, mai ba da umarni da kuma mai shiryawa, 
Ibrahim Mandawari.A cikin hirar, ya bayyana yadda aka yi ya shiga harkar fim, wadanda ya fi so a hada shi da su a 
fim da kuma burikan da yake so ya cimma a rayuwa.Daukar bidiyo: Yusuf YakasaiTacewa: Fatima OthmanGa wasu na baya 
da za ku so ku kalla:...Daga Bakin Mai Ita tare da Umar M Sheriff...Daga Bakin Mai Ita tare da Fati Shu'uma...
Daga Bakin Mai Ita tare da Umma ShehuWadanda aka fi kallo1:13Bidiyo, Donal Trump: Yadda za ka zama tsohon shugaban, 
Tsawon lokaci 1,13Sa'o'i 6 da suka wuce1:32Bidiyo, Kamala Harris: Abin da ya kamata ku sani game da mataimakiyar 
shugaban Amurka mai jiran gado, Tsawon lokaci 1,3219 Janairu 2021."""

igbo1 = """Ihe mere m mgbe a gbachara m ọgwụ mgbochị covid-19,"Dọkịta Ije Akunyili na-arụ n\'ụlọọgwụ ebe a na-elekọta 
ndị na-arịa covid-19 kwuru na kamgbe ọgwụ mgbochi gbasara covid-19 pụtara , ụjọ anaghị atụ ha ma ha na-eleta ndị 
na-arịa ọrịa covid 19  O kwuru na mgbe ọ gbara ọgwụ mgbochi a n'izuụka gara aga, obere ahụ ọkụ metụrụ ya mana o 
nweghị ihe ọzọ ya bụ ọgwụ mere ya. O kwuru na o teela e bidoro mewe nyocha maka ọgwụ mgbochi a kpatara o ji dị mfe iwepụta ya ugbua. O kwuru ka ndị mmadụ leghara anya izu ọjọ a na-agba maka ọgwụ mgbochi covid-19 nke Pfizer, Moderna nakwa. AstraZeneca ma nabata ya iji gbanahụ maka mkpa mkpa covid na-akpa."""

igbo2 = """Lee ụzọ ị ga-eji were ekwentị gị kpatawa ego,"Ụwa na-agbanwe n'ike n'ike dịka tekịnụzụ na-akawanye mma 
kwa ụbochị. Ịntaneetị so n'otu n'ime ihe wetara mgbanwe pụrụiche n'ụwa nke mere ọtụtụ ji ekwu n'ụwa ugbua dizi ka otu 
obodo (Global village). N'ihi mgbanwe a ịntanetị wetara, ohere buru ibu mmadụ ị nọ n'ụlọ ya, were igwe kọmputa 
maọbụ ekwentị ya na-akpatara onwe ya ego. Ọkachasị n'oge a ọrịa coronavirus malitere ifesa, ọtụtụ na-ejizi naanị 
ịntaneetị akpata ihe afọ na-eri. Ọ bụ eziokwu na e nwere ọtụtụ ụzọ ndị ekperima si anapụ mmadụ ego n'ịntaneetị, 
mana e nwekwara ụzọ kwụ ọtọ e si akpata ego na ya. Ọkaiwu Anulika Enemuo bụ onye ihe gbasara ịkpata ego n'ịntaeeti 
(online business) doro anya. Ọ kọwaara BBC Igbo ụfọdụ ihe mmadụ nwere ike iji ekwentị 
ya na-eme iji na-akpata ego. Onye ntoroọbịa ọbụla ị kpara aka n'ọnụ ugbua, ọ sị gị na ya etinyela ego ya na Bitcoin. 
Bitcoin bụ ụdị ego anaghị ahụ anya; Bekee kpọrọ ya 'Digital Currency' maọbụ 'Virtual Currency' maọbụ 
'Cryptocurrency'. Otu onye achọghị ka a kpọpụta aha ya kwuru na ya nwere ụdị ụlọahịa a ebe ọ na-eresi ndị mmadụ ihe 
dị icheiche dịka akwa, akpụkpọ ụkwụ, ntutuisi aka mere, dịrị gawazie. O kwuru sị: ""Ihe m na-eme bụ itinye foto 
ihe ndị a n'akara Instagram, facebook, nakwa Whatsapp, mana ọ bụghị na azụtala m ha."" 
""Kama ọ bụrụ na mmadụ chọọ ịzụ ihe ndị ahụ, aga m aga n'ahịa zụta ya, ma tinye obere ego n'elu (uru) 
ya  iji resi onye ahụ."" ""Ana m ewegara onye ahụ ngwaahịa ahụ n'ụlọ ya maọbụ n'ụlọọrụ ya, nke pụtara na ọ 
gaghị enye onwe ya nsogbu ịgawa ahịa."""

nigEng1 = """The Nigerian police say four officers were killed and one is still missing after they clashed with an armed criminal
 gang in the Birnin-Gwari area of Kaduna state.Police Spokesperson Frank Mba in a statement on Sunday said the officers 
 were ambushed by about 100 "bandits" as they returned from an operation in neighbouring Niger state.
 The police say "tens" of gunmen were also killed in the clashes on Friday.The police statement denies 
 initial reports that 18 officers were abducted during the attack.It says "only 16" officers were involved in the 
 incident and that the bodies of four of them and their weapons had been recovered, 11 survived while "efforts are 
 being intensified to rescue the officer still missing".It’s not clear whether the missing officer had been abducted 
 by the armed men.Meanwhile, in other separate attacks on Sunday also in Kaduna state, the authorities confirmed at 
 least five people including an 80-year-old woman and a local traditional ruler were killed and several others 
 wounded.The state commissioner for Internal Security, Samuel Aruwan, says the gunmen targeted three rural areas of Giwa, Igabi and Chikun."""

nigEng2 = """Prof Biodun Ogunyemi, the national president of the Academic Staff Union of Universities, told the BBC 
that the union decided to suspend the strike after "concrete agreements" were reached with the federal government 
on Tuesday. Prof Ogunyemi said lecturers will return to the universities from Thursday but warned that the union 
would resume the strike action if the government failed to fulfil a return to work deal.
The union has been pushing the government to implement a 2009 agreement that promised equipment for universities 
and an increase in lecturers' pay.The union said students will be invited back to universities after measures are 
put in place to prevent the spread of Covid-19"""


def main():
    st.title("NLP APP")
    menu = ["Home", "Glossary"]
    choice = st.sidebar.selectbox("Named Entity Recognition",menu)
    if choice == "Home":
        #st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
        st.subheader("Named Entity Recognition")
        st.markdown("<p style='font-size:12px;'>Named Entity Recognition(NER) locates named entities (person names, organizations, locations, time expressions, quantities, monetary values, percentages, etc) in unstructured text.</p>", unsafe_allow_html=True)
        models = ["Yoruba NER", "Naija NER","NGNEnglish NER","Igbo NER","Hausa NER","Pidgin NER"]
        dict1 = {"Yoruba":"45.57","Igbo":"35.48","Hausa":"44.84","Pidgin":"67.13","NigerianEnglish":"54.49" }
        model_choice = st.selectbox("Select Model",models)
        if model_choice == "Yoruba NER":
            comment = "This model identifies {0} named entities in context, with F1score of {Yoruba}% and 53.64% Precision".format(*dict1,**dict1)
        elif model_choice == "Igbo NER":
            comment = "This model identifies {1} named entities in context, with F1score of {Igbo}% and 47.18% Precision".format(*dict1,**dict1)
        elif model_choice == "Hausa NER":
            comment = "This model identifies {2} named entities in context, with F1score of {Hausa}% and 52.59% Precision".format(*dict1,**dict1)   
        elif model_choice == "Pidgin NER":
            comment = "This model identifies {3} named entities in context, with F1score of {Pidgin}% and 70.29% Precision ".format(*dict1,**dict1)   
        elif model_choice == "NGNEnglish NER":
            comment = "This model identifies {4} named entities in context, with F1score of {NigerianEnglish}% and 55.48% Precision".format(*dict1,**dict1)   
        else:
            comment = "This model is trained on the combination of Nigerian English, Hausa, pidgin, Igbo, Yoruba languages. F1score of 53.75% and 62.43% Precision"  
        st.markdown("<p style='font-size:12px;'>{}</p>".format(comment), unsafe_allow_html=True)

       #with st.beta_expander("Input Text"):
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        add_text = st.radio("Select Options", ("Sample Text","Enter Text", "Get text from URL", "Upload text"))
        if add_text == "Enter Text":
            raw_text = st.text_area("Your Text","Enter Text Here")
        elif add_text == "Sample Text":
            if model_choice == "Yoruba NER":
                raw_text = (yor_1,yor_2)
            elif model_choice == "Naija NER":
                raw_text = (yor_2,hausa2,igbo2,nigEng2,pidgin2)
            elif model_choice == "NGNEnglish NER":
                raw_text = (nigEng1,nigEng2)
            elif model_choice == "Igbo NER":
                raw_text = (igbo1,igbo2)
            elif model_choice == "Hausa NER":
                raw_text = (hausa1,hausa2)
            elif model_choice == "Pidgin NER":
                raw_text = (pidgin1,pidgin2)
            value = st.selectbox("Sample text",raw_text)
            st.write(value) 
            raw_text = value          
        elif add_text == 'Get text from URL':
            # use beautiful soup to scrape data from url
            st.subheader("Analyse Text from URL")
            raw_url = st.text_input("Enter URL", "Paste link")
            if raw_url == "Paste link":
                pass
            else:
                raw_text = get_text(raw_url)
                show_slider(raw_text)
        else:
            # Upload text from local computer
            uploaded_file = st.file_uploader(label="Choose a Text File", type='txt')
            if uploaded_file == None:
                pass
            else:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                raw_text = stringio.read()
                show_slider(raw_text)  

        if st.button("Submit"):
            if model_choice == "Yoruba NER":
                yoruba_model=load_model('YorubaNER Model')
                result = NER(yoruba_model,raw_text)
            elif model_choice == "Naija NER":
                naija_model = load_model('NaijaNER Model')
                result = NER(naija_model,raw_text)
            elif model_choice == "NGNEnglish NER":
                NGNEnglish_model = load_model("NGNEnglishNER Model")
                result = NER(NGNEnglish_model,raw_text)
            elif model_choice == "Igbo NER":
                Igbo_model = load_model("IgboNER Model")
                result = NER(Igbo_model,raw_text)
            elif model_choice == "Hausa NER":
                Hausa_model = load_model("HausaNER Model")
                result = NER(Hausa_model,raw_text) 
            else:
                model_choice == "Pidgin NER"
                pidgin_model = load_model("PidginNER Model")
                result = NER(pidgin_model,raw_text)
            get_result(result)

                           
    else:
        st.subheader("Glossary")
        get_about_page()
        
             
if __name__ == '__main__':
    main()
