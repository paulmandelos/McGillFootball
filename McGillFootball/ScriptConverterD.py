import pandas as pd
import numpy as np
import ast
date = '2023-08-16'
base = '/Users/paulmandelos/Desktop/RedBirdsFootball/'
gg = pd.read_excel(f'{base}Scripts/{date}-Script.xlsx')
script = pd.DataFrame(pd.read_excel(f'{base}Scripts/{date}-Script.xlsx', skiprows=1))
calls = pd.read_csv('/Users/paulmandelos/Desktop/RedBirdsFootball/RedBirdsCalls.csv')
holder = script[(script['Sit.']!=('Open')) & (script['Sit.']!=('Sit.'))]
blitzdict = ast.literal_eval(list(calls['BlitzDict'].values)[0])
stuntdict = ast.literal_eval(list(calls['StuntDict'].values)[0])
df1 = pd.DataFrame({
    "Sit.": [str(gg.columns[0])],
})
holder.index = holder.index+1
holder = pd.concat([holder,df1])
script = script[script['Sit.']=='Open']
script = script.dropna(axis='columns')

def stringMatcher(front,cov):
    front = str(front)
    front = front.lstrip()
    front = front.rstrip()
    cov = str(cov)
    cov = cov.lstrip()
    cov = cov.rstrip()
    defensiveFronts = calls['Def Front'].unique()
    defensiveFronts = [str(x) for x in defensiveFronts]
    stunts = calls['Stunts'].unique()
    stunts = [str(x) for x in stunts]
    blitz = calls['Blitz'].unique()
    blitz = [str(x) for x in blitz]
    coveragecall = calls['Coverage'].unique()
    coveragecall = [str(x) for x in coveragecall]
    coveragetype = calls['Coverage Type'].unique()
    coveragetype = [str(x) for x in coveragetype]
    dflst = []
    stuntlst = []
    blitzlst = []
    coveragelst = []
    peellst = []
    covtypelst = []
    #This will find the specific text in the Play Call
    for x in defensiveFronts:
        templst=[]
        count=0
        front = front.replace('JOK', 'JK')
        front = front.replace('JOKER', 'JK')
        #to ensure no doubles
        if str(x) in front:
            for y in defensiveFronts:
                if (x !=y) and (str(x) in str(y)):
                    templst.append(str(y))
            for y in templst:
                if str(y) in front:
                    count+=1
            if (count>0):
                continue
            else:
                dflst.append(str(x))
    for x in stunts:
        templst=[]
        count=0
        if x in front:
            for y in stunts:
                if (x !=y) and (x in y):
                    templst.append(str(y))
            for y in templst:
                if y in front:
                    count+=1
            if (count>0):
                continue
            else:
                if len(x)==1:
                    y = " " + x + " "
                    z = " " + x
                    if (y in front) or (z in front):
                        if x =='R':
                            x = 'RUN'
                        stuntlst.append(str(x))
                    else:
                        continue
                else:
                    if dflst==[]:
                        try:
                            value = stuntdict[x]
                            dflst.append(str(value))
                        except:
                            0
                    if x=='BANA':
                        x = 'BANANA'
                    stuntlst.append(str(x))
    for x in blitz:   
        if x in front:
            templst=[]
            count=0  
            for y in blitz:
                if (x !=y) and (x in y):
                    templst.append(str(y))
            for y in templst:
                if y in front:
                    count+=1
            if (count>0):
                continue
            else:
                try:
                    value = blitzdict[x]
                    dflst.append(str(value))
                except:
                    0
                blitzlst.append(str(x))
    for x in coveragecall:
        templst=[]
        count=0  
        if x in cov:
            for y in coveragecall:
                if (x !=y) and (x in y):
                    templst.append(str(y))
            for y in templst:
                if y in cov:
                    count+=1
            if (count>0):
                continue
            else:
                if x == 'RED BAM':
                    x = 'BAM'
                if x == 'JET/HAM':
                    x = 'HOLD'
                if x == '2 FLIP':
                    x = '2FLIP'
                if x == 'SNIFF SAM MATCH':
                    x = 'SNI S M'
                if x =='SNIFF':
                    x = 'SNI'
                if x == 'CLEVAGE':
                    x = 'CLV'
                    blitzlst.append('MUD MAN')
                coveragelst.append(str(x))
    for x in coveragetype:
        templst=[]
        count=0
        if x in cov:
            for y in coveragetype:
                if (x !=y) and (x in y):
                    templst.append(str(y))
            for y in templst:
                if y in cov:
                    count+=1
            if (count>0):
                continue
            else:
                covtypelst.append(str(x))
    if ("PL" or "PEEL" or "PE") in cov:
        peellst.append("PL")  
    
    return pd.Series({"Def Front" : " ".join(dflst),"Stunts":" ".join(stuntlst),"Blitz":" ".join(blitzlst),"Coverage":" ".join(coveragelst),"Peel":" ".join(peellst),"Coverage Type":" ".join(covtypelst)})

m = script[["FRONT", "COV"]].apply(lambda x: stringMatcher(x['FRONT'], x['COV']), axis=1)

finished = pd.merge(script,m, on=script.index, how="inner")

finished = finished.set_index("key_0")
finished.index=finished.index+1
finished = pd.concat([finished,holder])
finished = finished.sort_index()
finished = finished.drop(columns = ['DL','LB','DB'])
finished.reset_index(inplace=True)
finished['Coverage'].replace(['BLACK'],['BLK'],inplace=True)
finished = finished.drop(columns = ['index','Jeu','B'])
finished.rename(columns = {'D': 'DN', 'D.1': 'DIST','P':'PERSONNEL','Offensive':'OFF PLAY',"Stunts":'stunt','Coverage Type':'CV TYPE'},inplace=True)
lst = list(finished['Sit.'].unique())
lst.remove('Open')
lst = [x for x in lst if not str.isnumeric(x)]
indexlst=[]
for x in lst:
    temp = finished[finished['Sit.']==x]
    indexlst.append(temp.index.values[0])
for x in lst:
    if "/" in x:
        y = x.replace("/"," ")
        lst[lst.index(x)] = y
finished = finished.drop(columns = ['Sit.'])
for x in range(len(lst)):
    try:
        temp = finished.iloc[indexlst[x]+1:indexlst[x+1]]
    except:
        temp = finished.iloc[indexlst[x]+1:]
    temp.to_csv(f'{base}HuddlReadyScripts/{date}-Script-Hudl-{lst[x]}.csv',index=False)
finished.to_csv(f'{base}HuddlReadyScripts/{date}-Script-Hudl.csv',index=False)