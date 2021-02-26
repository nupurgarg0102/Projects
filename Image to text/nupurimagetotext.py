#%%
def background(filepath):
    import cv2
    import numpy as np
    import pytesseract
    from pytesseract.pytesseract import Output
    # %matplotlib inline
    import numpy as np
    import pandas as pd 
    import nltk
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    from nltk.stem import WordNetLemmatizer 
    from textblob import TextBlob
    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    #%%
    from nltk.corpus import stopwords 
    from nltk.tokenize import word_tokenize
    import re
    text = text.lower()
    tweet_list = [ele for ele in text.split()]
    clean_tokens = [t for t in tweet_list if re.match(r'[^\W\d]*$', t)]
    clean_s = ' '.join(clean_tokens)
    stop_words = set(stopwords.words('english')) 

    word_tokens = word_tokenize(clean_s) 

    filtered_sentence = [w for w in word_tokens if not w in stop_words] 

    sentence = [] 

    for w in word_tokens: 
        if w not in stop_words: 
            sentence.append(w) 

    print(sentence) 

    #%%
    from nltk.corpus import wordnet
    from openpyxl import Workbook
    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "WORDS"
    sheet["B1"] = "SYNONYMS"
    sheet["C1"] = "ANTONYMS"
    sheet["D1"] = "MEANING"

    workbook.save(filename="translate.xlsx")
    lwords=[]
    j=2
    for i in range(len(sentence)):
        lwords.append(sentence[i])
        s="A"+str(j)
        sheet[s]=sentence[i]
        j=j+1
        workbook.save(filename="translate.xlsx")
    j=2
    synonyms = []
    antonyms = []
    meanings = []
    js=2
    for i in lwords:
        synonyms=[]
        for syn in wordnet.synsets(i):
            for lm in syn.lemmas():
                    synonyms.append(lm.name())#adding into synonyms
        if len(synonyms)>0:
            s="B"+str(js)
            sheet[s]=synonyms[0]
            workbook.save(filename="translate.xlsx")
        js=js+1
    js=2
    for i in lwords:
        antonyms=[]
        for syn in wordnet.synsets(i):
            for lm in syn.lemmas():
                if lm.antonyms():
                    antonyms.append(lm.antonyms()[0].name()) #adding into antonyms
        if len(antonyms)>0:
            s="C"+str(js)
            sheet[s]=antonyms[0]
            workbook.save(filename="translate.xlsx")
        js=js+1
    js=2


    #%%
    from PyDictionary import PyDictionary 
    dic = PyDictionary()
    mean=[]
    mean1=[]

    for i in lwords:
        try:   
            data = dic.meaning(i)
            data = list(data.values())
            mean.append(data)
        except Exception:
            mean.append("null")
    

    #%%
    m = []
    for i in range(0,len(mean)-1):
        if mean[i] is None:
            m.append(None)
        if mean[i] is not None:
            try:
                m.append(mean[i][0][0])
            except Exception:
                m.append(mean[i][1][0])


    # %%
    js=2

    for i in range(len(m)):
        s="D"+str(js)
        sheet[s]=m[i]
        workbook.save(filename="translate.xlsx")
        js=js+1


# %%
