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


The article that is related to this code can be found in 
https://www.sciencedirect.com/science/article/pii/S2666990023000149

citation this code 

Altuhaifa, F., Al Tuhaifa, D., Al Ribh, E., & Al Rebh, E. (2023). Identifying and defining entities associated with fall risk factors events found in fall risk assessment tools. Computer Methods and Programs in Biomedicine Update, 3. doi:10.1016/j.cmpbup.2023.100105


