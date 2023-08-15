import pandas as pd

df = pd.read_excel('/Users/paulmandelos/Downloads/ENTIRE_D.xlsx')

stunt = df.groupby(['STUNT','DEF FRONT']).size().reset_index().rename(columns={0:'count'})
blitz = df.groupby(['BLITZ','DEF FRONT']).size().reset_index().rename(columns={0:'count'})
stuntdict={}
blitzdict ={}
def make_dict(dict,stunt,deffront):
    if (stunt in dict.keys()):
        temp = dict[stunt]
        temp1 = temp + ' or ' + deffront
        dict[stunt] = temp1
    else:
        dict[stunt] = deffront
    return 0

stunt.apply(lambda x: make_dict(stuntdict,x.STUNT,x['DEF FRONT']),axis=1)
blitz.apply(lambda x: make_dict(blitzdict,x.BLITZ,x['DEF FRONT']),axis=1)

cov = ''
if ' M' in cov and cov not in 'SN S M':
    cov = cov.replace(' M', '')

#R is RUN for stunt