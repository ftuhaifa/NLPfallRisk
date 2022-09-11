# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 18:41:08 2022

@author: Fatimah Altuhaifa
"""
import NLPfallRisk

import pandas as pd

df = pd.read_csv('falldata.csv')

list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []

list7 = []
list8 = []
list9 = []
list10 = []
list11 = []
list12 = []

list13 = []
list14 = []
list15 = []
list16 = []
list17 = []
list18 = []

list19 = []



for index, row in df.iterrows():
    
    list1 = NLPfallRisk.history(str(df["Note"][index])) + list1
    list2 = NLPfallRisk.medical(str(df["Note"][index])) + list2
    list3 = NLPfallRisk.sensory(str(df["Note"][index])) + list3
    list4 = NLPfallRisk.foot(str(df["Note"][index])) + list4
    list5 = NLPfallRisk.footwear(str(df["Note"][index])) + list5
    list6 = NLPfallRisk.mental(str(df["Note"][index])) + list6

    list7 = NLPfallRisk.toileting(str(df["Note"][index])) + list7
    list8 = NLPfallRisk.gait(str(df["Note"][index])) + list8
    list9 = NLPfallRisk.nutritional(str(df["Note"][index])) + list9 
    list10 = NLPfallRisk.balance(str(df["Note"][index])) + list10
    list11 = NLPfallRisk.environmental(str(df["Note"][index])) + list11
    list12 = NLPfallRisk.medicine(str(df["Note"][index])) + list12

    list13 = NLPfallRisk.WalkingAid(str(df["Note"][index])) + list13
    list14 = NLPfallRisk.ADL(str(df["Note"][index])) + list14
    list15 = NLPfallRisk.AGE(str(df["Note"][index])) + list15
    list16 = NLPfallRisk.gender(str(df["Note"][index])) + list16
    list17 = NLPfallRisk.Assist(str(df["Note"][index])) + list17
    list18 = NLPfallRisk.transfer(str(df["Note"][index])) + list18

    list19 = NLPfallRisk.fear(str(df["Note"][index])) + list19
    

print ("******************************************")
print ("******************************************")
print ("******************************************")
print (list1)
print ("******************************************")
print (list2)
print ("******************************************")
print (list3)
print ("******************************************")
print (list4)
print ("******************************************")
print (list5)
print ("******************************************")
print (list6)
print ("******************************************")
print (list7)
print ("******************************************")
print (list8)
print ("******************************************")
print (list9)
print ("******************************************")
print (list10)
print ("******************************************")
print ("******************************************")
print (list11)
print ("******************************************")
print (list12)
print ("******************************************")
print (list13)
print ("******************************************")
print (list14)
print ("******************************************")
print (list15)
print ("******************************************")
print (list16)
print ("******************************************")
print (list17)
print ("******************************************")
print (list18)
print ("******************************************")
print (list19)
print ("******************************************")






