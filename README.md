# NLPfallRisk
With the NLPfallRisk tool, fall risk factors can be extracted from free text based on using scispacy, a regular expression language.
for using the NLPfallRisk tool, download the NLPfallRisk.py and risk.cvs files. Then you have to install scispacy 

# This tool is a python based tool

#you will need to install this in command line 

pip install --user dynarray

pip install --user scispacy

!pip install -U spacy

conda install -c pytorch pytorch

conda install -c conda-forge nmslib

python -m spacy download en_core_web_sm


#example for Using NLPfallRisk tool

import NLPfallRisk

import pandas as pd

text = "He is suffereing from: Incontinence, Hypertension, and Gout, propulsive gait loose shoe"

#for extracting disease fall risk factors

disease = NLPfallRisk.medical(text)

print (disease)

#for extracting Foot issues fall risk factors

foot = NLPfallRisk.foot(text)

print (foot)



# The tool has 19 functions which are 
history(text), medicine(text), medical(text), sensory(text), 

foot(text), footwear(text), mental(text), toileting(text), 

nutritional(text), Assist(text),

balance(text), gait(text), WalkingAid(text), ADL(text), 

gender(text), age(text), transfer(text), environmental (text),  and fear(text). 



# you can download the demo files which are file fall.py and falldata.csv and run fall.py to see how it does work.




