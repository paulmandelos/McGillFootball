import pandas as pd
import numpy as np
from collections import Counter
###Add the date of the script here
date = '2023-04-30'
##this is the filepath of the folder where you keep the scripts on your computer
base = '/Users/paulmandelos/Desktop/RedBirdsFootball/'
###ADD WHERE THE SCRIPT IS
#script = pd.DataFrame(pd.read_excel(f'{base}{date}OffensiveScript.csv'))
script = pd.read_csv('/Users/paulmandelos/Downloads/2023-04-30-OffensiveScipt.csv')
###ADD WHERE THE CALLS ARE
calls = pd.read_csv(f'{base}RedBirdsOCalls.csv')
script = script.apply(lambda x: x.astype(str).str.upper())
calls = calls.apply(lambda x: x.astype(str).str.upper())
holder = script[script['FORMATION-PLAY'].isnull()]
script = script[(~script['FORMATION-PLAY'].isnull()) & (script['FORMATION-PLAY']!='FORMATION-PLAY')]
pf = {list(calls["PFInput"])[i]: list(calls["PlayFamily"])[i] for i in range(len(list(calls["PFInput"])))}
concept = {list(calls["ConceptInput"])[i]: list(calls["Concept"])[i] for i in range(len(list(calls["ConceptInput"])))}
reca = {list(calls["RecAlignmentInput"])[i]: list(calls["RecAlignment"])[i] for i in range(len(list(calls["RecAlignmentInput"])))}

def stringMatcher(playname):
    temp = playname.split("(")
    playname = temp[0]
    motion = calls['Motion'].unique()
    aam = calls['ArriveAtMesh'].unique()
    protection = calls['protection'].unique()
    pflist = []
    conceptlist = []
    recalist = []
    aam2 = ''
    protection2 = ''
    motion2 = ''
    for x in list(concept.keys()):
        y = x
        if len(x) == 1:
                y = " " + str(x) + " "
        if y in playname:
            conceptlist.append(concept[x])
    for x in list(pf.keys()):
        y = x
        if len(x) == 1:
                y = " " + str(x) + " "
        if y in playname:
            pflist.append(pf[x])
    for x in list(reca.keys()):
        y = x
        if len(x) == 1:
                y = " " + str(x) + " "
        if y in playname:
            recalist.append(reca[x])        
    
    for x in motion:
        try:
            if x in playname:
                if x == 'still':
                    motion2 = '-'
                    break
                else:
                    motion2 = x
        except:
            motion2 = ''
            continue
        
    for x in aam:
        try:
            if x in playname:
                aam2 = x
        except:
            aam2 = ''
            continue
        
    for x in protection:
        try:
            if x in playname:
                protection2 = x
        except:
            protection2 = ''
            continue
    if (conceptlist==[]):
        conceptlist.append("DROPBACK")
        
    if ("WK" in playname):
        for x in recalist:
            x = ''.join(reversed(str(x)))
    return pd.Series({"RecAlignment" : " ".join(pd.Series(recalist).drop_duplicates().tolist()),"Motion":motion2,"ArriveAtMesh":aam2,"Concept":" ".join(pd.Series(conceptlist).drop_duplicates().tolist()),"PlayFamily":" ".join(pd.Series(pflist).drop_duplicates().tolist()),"Protection":protection2})


m = script[["FORMATION-PLAY"]].apply(lambda x: stringMatcher(x['FORMATION-PLAY']), axis=1)
finished = pd.merge(script,m, on=script.index, how="inner")
print(finished)
###Add to where you want the columns outputed
#m.to_csv(f'{base}finished/{date}-Script-finished.csv')