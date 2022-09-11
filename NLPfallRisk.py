# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:18:24 2022

@author: Fatimah Altuhaifa
"""


import string
import spacy
import scispacy
import pandas as pd
from nltk.stem import WordNetLemmatizer
#this packeges for linke the entites with UMLS
from scispacy.linking import EntityLinker
from spacy.tokens import Span
from nltk.classify import SklearnClassifier
from wordcloud import WordCloud, STOPWORDS 
from nltk.stem import WordNetLemmatizer
import string
import re



#you will need to install this in command line
#pip install --user dynarray
#pip install --user scispacy
#!pip install -U spacy
#conda install -c pytorch pytorch
#conda install -c conda-forge nmslib

#python -m spacy download en_core_web_sm

# Load data example
MedNote = pd.read_csv('risk.csv')

nlp = spacy.load("en_ner_bc5cdr_md")
nlp2 = spacy.load("en_core_web_sm")



#*********************Medical Condition **************************************  
def medical(text):
    ''' Function to return list '''
    MedicalCondition = []
    text = text.lower()
    doc = nlp(text)
    
    for entity in doc.ents:
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["Medical condition"])):
             if str(MedNote["Medical condition"][j]) == str(entity):
                 MedicalCondition.append(entity)
    MedicalCondition = list(dict.fromkeys(MedicalCondition))
    return MedicalCondition


#*********************SensoryLosses **************************************  
def sensory(text):
    ''' Function to return list '''
    SensoryLosses = []
    text = text.lower()
    doc = nlp(text)
    
    for entity in doc.ents:
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["Sensory losses"])):
             if str(MedNote["Sensory losses"][j]) == str(entity):
                 SensoryLosses.append(entity)
    SensoryLosses = list(dict.fromkeys(SensoryLosses))
    return SensoryLosses


#********************* FootIssues **************************************  
def foot(text):
    ''' Function to return list '''
    FootIssues = []
    text = text.lower()
    doc = nlp(text)
    
    for entity in doc.ents:
        
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["Foot issues"])):
             if str(MedNote["Foot issues"][j]) == str(entity):
                 FootIssues.append(entity)
                 
    list1 = re.findall(r"\bcorn*", text)
    list2 = re.findall(r"\bbunion*", text)
    list3 = re.findall(r"\bswollen \w+(?:[^\w,]){0,2}", text)
    list4 = re.findall(r"\bdeformed \w+(?:[^\w,]){0,2}", text)
    list5 = re.findall(r"\bimpaired \w+(?:[^\w,]){0,2}", text)
    list6 = re.findall(r"\breduced \w+(?:[^\w,]){0,2}", text)
    list7 = re.findall(r"\w+(?:[^\w,]){0,2} \btoe", text)
    list8 = re.findall(r"\btoe \w+(?:[^\w,]){0,2}", text)
    list9 = re.findall(r"\w+(?:[^\w,]\w+){0,2} \btoe", text)
    list10 = re.findall(r"\w+(?:[^\w,]\w+){0,1} \btoe", text) 
    list11 = re.findall(r"\bfallen \w+(?:[^\w,]){0,2}", text)
    list12 = re.findall(r"\bslip \w+(?:[^\w,]){0,2}", text)
    list13 = re.findall(r"\bpainful \w+(?:[^\w,]){0,2}", text)
    
    

    Footlist = list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9 + list10 + list11 + list12 + list13
 
    for entity in Footlist:
        
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["Foot issues"])):
             if str(MedNote["Foot issues"][j]) == str(entity):
                 FootIssues.append(entity)        
                
#swollen
    FootIssues = list(dict.fromkeys(FootIssues))
    return FootIssues


#********************* footwearIssues **************************************  
def footwear(text):
    ''' Function to return list '''
    footweariss = []
    text = text.lower()
    doc = nlp(text)
    
    for entity in doc.ents:
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["Footwear issues"])):
             if str(MedNote["Footwear issues"][j]) == str(entity):
                 footweariss.append(entity)
                 
    list1 = re.findall(r"\bwearing \w+(?:[^\w,]\w+){0,2}", text)
    list2 = re.findall(r"\bloose \w+(?:[^\w,]){0,2}", text)

    list3 = re.findall(r"\bslingback*", text)
    list4 = re.findall(r"\bscuff*", text)
    list5 = re.findall(r"\bthong*", text)
    list6 = re.findall(r"\bbarefoot", text)
    list7 = re.findall(r"\bbarefeet", text)
    list8 = re.findall(r"\bstockin \w+(?:[^\w,]){0,2}", text)


    footwearisslist  = list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + footweariss 
    
    for entity in footwearisslist:
        for j in range(len(MedNote["Footwear issues"])):
             entity = entity.replace("  ", "")
             entity = entity.rstrip()
             if str(MedNote["Footwear issues"][j]) == str(entity):
                 footweariss.append(entity) 
    
    
    
    footweariss = list(dict.fromkeys(footweariss))
    return footweariss

#********************* mental **************************************  
def mental(text):
    ''' Function to return list '''
    Mentalcognitive = []
    text = text.lower()
    doc = nlp(text)
    
    for entity in doc.ents:
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["Mental cognitive"])):
             if str(MedNote["Mental cognitive"][j]) == str(entity):
                 Mentalcognitive.append(entity)
    Mentalcognitive = list(dict.fromkeys(Mentalcognitive))
    return Mentalcognitive

#********************* Toileting habits **************************************  
def toileting(text):
    ''' Function to return list '''
    Toiletinghabits = []
    text = text.lower()
    doc = nlp(text)
    
    for entity in doc.ents:
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["Mental cognitive"])):
             if str(MedNote["Toileting habits"][j]) == str(entity):
                 Toiletinghabits.append(entity)
    Toiletinghabits = list(dict.fromkeys(Toiletinghabits))
    return Toiletinghabits


#********************* Nutritional factors **************************************  
def nutritional(text):
    ''' Function to return list '''
    Nutritionalfactors = []
    text = text.lower()
    doc = nlp(text)
    
    for entity in doc.ents:
        
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["Nutritional factors"])):
             if str(MedNote["Nutritional factors"][j]) == str(entity):
                 Nutritionalfactors.append(entity)
    Nutritionalfactors = list(dict.fromkeys(Nutritionalfactors))
    return Nutritionalfactors


#********************* Balance problems **************************************  
def balance (text):
    ''' Function to return list '''
    Balanceproblems = []
    text = text.lower()
    doc = nlp(text)
    
    for entity in doc.ents:
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["Balance problems"])):
             if str(MedNote["Balance problems"][j]) == str(entity):
                 Balanceproblems.append(entity)
    Balanceproblems = list(dict.fromkeys(Balanceproblems))
    return Balanceproblems


#********************* Environmental **************************************  
def environmental (text):
    ''' Function to return list '''
    Environmental = []
    text = text.lower()
    doc = nlp2(text)
    
    for entity in doc:
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["Environmental"])):
             if str(MedNote["Environmental"][j]) == str(entity):
                 Environmental.append(entity)
                 
    list1 = re.findall(r"\black \w+(?:[^\w,]\w+){0,2}", text)
    list2 = re.findall(r"\black \w+(?:[^\w,]){0,3}", text)
    list3 = re.findall(r"\bpoor \w+(?:[^\w,]\w+){0,1}", text)
    list4 = re.findall(r"\bpoor \w+(?:[^\w,]){0,3}", text)
    list5 = re.findall(r"\bwet \w+(?:[^\w,]){0,3}", text)
    list6 = re.findall(r"\bunsecured \w+(?:[^\w,]){0,3}", text)
    list7 = re.findall(r"\bloose \w+(?:[^\w,]){0,3}", text)
    list8 = re.findall(r"\bbroken \w+(?:[^\w,]){0,3}", text)
    list9 = re.findall(r"\bdim \w+(?:[^\w,]){0,3}", text)
    list10 = re.findall(r"\bslippery \w+(?:[^\w,]){0,3}", text)
    list11 = re.findall(r"\blow \w+(?:[^\w,]){0,3}", text)
    list12 = re.findall(r"\buneven \w+(?:[^\w,]){0,3}", text)
    list13 = re.findall(r"\bunstable \w+(?:[^\w,]){0,3}", text)
    list14 = re.findall(r"\bobstructed  \w+(?:[^\w,]){0,3}", text)
    
    
    list15 = re.findall(r"\bpother", text)
    list16 = re.findall(r"\bclutter", text)
    list17 = re.findall(r"\bleak", text)
    list18 = re.findall(r"\bwalkway*", text)
    list19 = re.findall(r"\bslippery \w+(?:[^\w,]){0,2}", text)
    list20 = re.findall(r"\btripping \w+(?:[^\w,]){0,2}", text)
    list21 = re.findall(r"\bobstacles*", text)
    list22 = re.findall(r"\bunstable \w+(?:[^\w,]){0,2}", text)


    
    lack = list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9 + list10 + list11 + list12 + list13 + list14 + list15 + list16 + list17 + list18 + list19 + list20 + list21 + list22
    
    
    
    for entity in lack:
        for j in range(len(MedNote["Environmental"])):
             entity = entity.replace("  ", "")
             entity = str(entity)
             entity = entity.rstrip()
             if str(MedNote["Environmental"][j]) == str(entity.replace("  ", "")):
                 Environmental.append(entity)
#    if "pother" in text:
#        Environmental.append("pother")
#    if "walkway" in text:
#        Environmental.append("walkway")
#    if "walkways" in text:
#        Environmental.append("walkways")
#   if "clutter" in text:
#        Environmental.append("clutter")
#    if "leak" in text:
#        Environmental.append("leak")
        
    Environmental = list(dict.fromkeys(Environmental))
    return Environmental


    if "floor" in text:
        Environmental.append("floor")
    if "lack of stair handrails" in text:
        Environmental.append("lack of stair handrails")
    if "poor stair design" in text:
        Environmental.append("poor stair design")
    if "loose carpets" in text:
        Environmental.append("loose carpets")
    if "lack of bathroom grab bars" in text:
        Environmental.append("lack of bathroom grab bars")

        
#newd = re.findall(r"\black \w+(?:[^\w,]\w+){0,2}", Text)


#print(newd)


#********************* medicine **************************************  
def medicine (text):
    ''' Function to return list '''
    medici = []
    text = text.lower()
    doc = nlp(text)
    
    for entity in doc.ents:
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["medicine"])):
             if str(MedNote["medicine"][j]) == str(entity):
                 medici.append(entity)
                 

    medici = list(dict.fromkeys(medici))
    return medici


#*********************** Gait ************************************************
def gait (text):
    
    gt = []
    text = text.lower()
    doc = nlp(text)
    for entity in doc:
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["Gait Abnormalities"])):
             if str(MedNote["Gait Abnormalities"][j]) == str(entity):
                 gt.append(entity)
                 
    list1 = re.findall(r"\w+(?:[^\w,]){0,2} \bgait", text)
    list2 = re.findall(r"\w+(?:[^\w,]){0,3} \bgait", text)
    list3 = re.findall(r"\bgait \w+(?:[^\w,]){0,2}", text)

    
    gtlist = list2 + list1 + list3

    for entity in gtlist:
        for j in range(len(MedNote["Gait Abnormalities"])):
             entity = entity.replace("  ", "")
             entity = str(entity)
             entity = entity.rstrip()
             if str(MedNote["Gait Abnormalities"][j]) == str(entity.replace("  ", "")):
                 gt.append(entity)
                 
    gt = list(dict.fromkeys(gt))
    return gt
    
#********************** Walking **********************************************               
def WalkingAid (text):
    ''' Function to return list '''
    walk = []
    text = text.lower()
    doc = nlp(text)
    
    for entity in doc.ents:
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["Walking aids"])):
             if str(MedNote["Walking aids"][j]) == str(entity):
                 walk.append(entity)
                 
     
    list1 = re.findall(r"\w+(?:[^\w,]\w+){0,2} \bwalker", text)
    list4 = re.findall(r"\w+(?:[^\w,]\w+){0,3} \bwalker", text)
    list2 = re.findall(r"\w+(?:[^\w,]){0,3} \bwalker", text)
    list3 = re.findall(r"\w+(?:[^\w,]\w+){0,1} \bwalker", text)
    list5 = re.findall(r"\w+(?:[^\w,]){0,3} \bcane", text)
    list6 = re.findall(r"\w+(?:[^\w,]){0,3} \brollator", text)
    list7 = re.findall(r"\bwheelchair", text)
    
    llist = list1 + list2 + list3 + list4 + list5 + list6 + list7
    for entity in llist:
        for j in range(len(MedNote["Walking aids"])):
             entity = entity.replace("  ", "")
             entity = entity.rstrip()
             if str(MedNote["Walking aids"][j]) == str(entity.replace("  ", "")):
                 walk.append(entity)
    walk = list(dict.fromkeys(walk))             
    return walk 

#*********************************ADL *****************************************
def ADL (text):
    ''' Function to return list '''
    ad = []
    text = text.lower()
    doc = nlp(text)
    
    for entity in doc.ents:
        entity = str(entity)
        entity = entity.rstrip()
        for j in range(len(MedNote["ADL"])):
             if str(MedNote["ADL"][j]) == str(entity):
                 ad.append(entity)
                 
    list2 = re.findall(r"\bwalking \w+(?:[^\w,]){0,3}", text)
    list6 = re.findall(r"\w+(?:[^\w,]){0,3} \bwalk*", text)
    list7 = re.findall(r"\bwalk*", text)
    list1 = re.findall(r"\brun*", text)
    list3 = re.findall(r"\baerobic exercise", text)
    list4 = re.findall(r"\bexercise", text)
    list5 = re.findall(r"\bunicycling", text)
    list8 = re.findall(r"\byoga", text)
    list9 = re.findall(r"\w+(?:[^\w,]){0,3} \bride", text)
    list10 = re.findall(r"\w+(?:[^\w,]){0,3} \briding", text)

    list11 = re.findall(r"\w+(?:[^\w,]){0,3} \bchores", text)
    list12 = re.findall(r"\w+(?:[^\w,]){0,3} \belevator", text)
    list13 = re.findall(r"\w+(?:[^\w,]){0,3} \bstair*", text)

    list14 = re.findall(r"\w+(?:[^\w,]){0,3} \bactivity", text)             
                 
    llist = list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9 + list10 + list11 + list12 + list13 + list14
    for entity in llist:
        for j in range(len(MedNote["ADL"])):
             entity = entity.replace("  ", "")
             entity = str(entity)
             entity = entity.rstrip()
             if str(MedNote["ADL"][j]) == str(entity.replace("  ", "")):
                 ad.append(entity)
                 
    ad = list(dict.fromkeys(ad))
    return ad      
#*********************** AGE *************************************************

def AGE (text):
    ''' Function to return list '''
    age = []
    #text = text.lower()
    
    list1 = re.findall(r"\d+(?:[^\w,]){0,3} \bage", text)
    list2 = re.findall(r"\d+(?:[^\w,]){0,3} \byear*", text)
    list3 = re.findall(r"\d+(?:[^\w,]){0,3} \bold", text)
    
    age = list1 + list2 + list3

    age = list(dict.fromkeys(age))                                               
    return age 
#**************** Gender ******************************************************
def gender (text):
    ''' Function to return list '''
    gend = []
    text = text.lower()
    
    list1 = re.findall(r"\bmale", text)
    list2 = re.findall(r"\bfemale", text)
    list3 = re.findall(r"\bgender* \w+(?:[^\w,]){0,3}", text)
    
    gend = list1 + list2 + list3 
    gend = list(dict.fromkeys(gend))                                             
    return gend 
#**************************** History *****************************************
def history (text):
    ''' Function to return list '''
    hist = []
    text = text.lower()
    
    list1 = re.findall(r"\bfall \w+(?:[^\w,]\w+){0,2}", text)
    list2 = re.findall(r"\bfall \w+(?:[^\w,]){0,2}", text)
    list3 = re.findall(r"\w+(?:[^\w,]){0,2} \bfall", text)
    list4 = re.findall(r"\w+(?:[^\w,]){0,2} \bfalling", text)
    list5 = re.findall(r"\bfall \w+(?:[^\w,]\w+){0,3}", text)

    histlist = list1 + list2 + list3 + list4 + list5
    

    for entity in histlist:
        for j in range(len(MedNote["History"])):
             entity = entity.replace("  ", "")
             entity = entity.rstrip()
             if str(MedNote["History"][j]) == str(entity):
                 hist.append(entity)
    
    hist = list(dict.fromkeys(hist))
                                                   
    return hist      
#************************************ Assist *********************************
def Assist (text):
        
    assi = []
    text = text.lower()
    
    list1 = re.findall(r"\bassistance \w+(?:[^\w,]\w+){0,1}", text)
    list2 = re.findall(r"\w+(?:[^\w,]){0,3} \bassistance*", text)
    list3 = re.findall(r"\bhelp \w+(?:[^\w,]\w+){0,1}", text)
    list4 = re.findall(r"\w+(?:[^\w,]){0,3} \bhelp*", text)
    list5 = re.findall(r"\bassistance \w+(?:[^\w,]\w+){0,2}", text)
    list6 = re.findall(r"\bhelp \w+(?:[^\w,]\w+){0,2}", text)
    list7 = re.findall(r"\w+(?:[^\w,]\w+){0,2} \bassistance", text)
    
    assilist = list1 + list2 + list3 + list4 + list5 + list6 + list7
    

    
    for entity in assilist:
        for j in range(len(MedNote["Assisted mobility"])):
             #entity = entity.replace("  ", "")
             #entity = entity.rstrip()
             if str(MedNote["Assisted mobility"][j]) == str(entity):
                 assi.append(entity)
    

    assi = list(dict.fromkeys(assi))                                               
    return assi   

#********************************** Transfer *********************************

def transfer (text):
        
    tra = []
    text = text.lower()
    
    list1 = re.findall(r"\brise \w+(?:[^\w,]\w+){0,1}", text)
    list2 = re.findall(r"\w+(?:[^\w,]){0,3} \brise", text)
    list3 = re.findall(r"\brising \w+(?:[^\w,]\w+){0,1}", text)
    list4 = re.findall(r"\w+(?:[^\w,]){0,3} \brising", text)
    list5 = re.findall(r"\btransferring \w+(?:[^\w,]\w+){0,1}", text)
    list6 = re.findall(r"\btransfer \w+(?:[^\w,]\w+){0,1}", text)
    
    
    tralist = list1 + list2 + list3 + list4 + list5 + list6
    
    for entity in tralist:
        for j in range(len(MedNote["Transferring"])):
             entity = entity.replace("  ", "")
             entity = entity.rstrip()
             if str(MedNote["Transferring"][j]) == str(entity):
                 tra.append(entity)
    
    
     
    tra = list(dict.fromkeys(tra))                                             
    return tra 
#******************************* Fear ****************************************
def fear (text):
        
    fea= []
    text = text.lower()
    
    list1 = re.findall(r"\bfear of fall*", text)
    list2 = re.findall(r"\bfall fear", text)
    
    list3 = re.findall(r"\bafraid to fall*", text)
    list4 = re.findall(r"\bafraid from fall*", text)
    
    list5 = re.findall(r"\bscaring from fall*", text)
    list6 = re.findall(r"\bscare to fall*", text)

    list7 = re.findall(r"\bfall scare", text)
    list8 = re.findall(r"\bfalling scare", text)
    list9 = re.findall(r"\bfalling fear", text)
    list10 = re.findall(r"\bafraid \w+(?:[^\w,]\w+){0,2}", text)
    list11 = re.findall(r"\bafraid \w+(?:[^\w,]\w+){0,3}", text)
    list12 = re.findall(r"\bfear \w+(?:[^\w,]\w+){0,2}", text)
    list13 = re.findall(r"\bscare \w+(?:[^\w,]\w+){0,3}", text)
    list14 = re.findall(r"\bscare \w+(?:[^\w,]\w+){0,2}", text)
    list15 = re.findall(r"\w+(?:[^\w,]\w+){0,2} \bfall", text)
    list16 = re.findall(r"\w+(?:[^\w,]\w+){0,2} \bfalling", text)

    
    fealist = list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9 + list10 + list11 + list12 + list13 + list14 + list15 + list16
    
    for entity in fealist:
        for j in range(len(MedNote["Fear"])):
             entity = entity.replace("  ", "")
             entity = entity.rstrip()
             if str(MedNote["Fear"][j]) == str(entity):
                 fea.append(entity)
    #Remove duplicate from the list
    fea = list(dict.fromkeys(fea))
    return fea
    
#    for i in range(len(MedNote["Medical condition"])):
#
 #       your_list.append(i)
#    return your_list

