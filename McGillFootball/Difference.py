import pandas as pd
df = pd.read_csv('/Users/paulmandelos/Desktop/RedBirdsFootball/CoachTedMTLD.csv')
print(df.columns)
#df['isPass'] = df['PLAY TYPE'].str.contains('Pass')

##What the defence
#FRONT, BLITZ 

defFront = df.groupby(by=['SITUATION (AFTER)','DEF FRONT']).count().sort_values(by=['DEF FRONT'])
defCov = df.groupby(by=['SITUATION (AFTER)','COVERAGE']).count().sort_values(by=['COVERAGE'])

print(defFront)
print(defCov)
#d2['Count'] = df.groupby(by=['SITUATION (AFTER)'])['isPass'].size().to_frame('Count').reset_index()['Count']
#d2['GainOrLossAverage'] = round(df.groupby(by=['SITUATION (AFTER)'])['GN/LS'].mean(),1).to_frame('GainOrLossAverage').reset_index()['GainOrLossAverage']
#d2['AverageDistanceToFirst'] = round(df.groupby(by=['SITUATION (AFTER)'])['DIST'].mean(),1).to_frame('AverageDistanceToFirst').reset_index()['AverageDistanceToFirst']
#d2 = d2[['SITUATION (AFTER)','Count','PercentagePass','GainOrLossAverage','AverageDistanceToFirst']]
#d2.sort_values(by=['Count'],ascending=False,inplace=True)
#d2.to_csv('/Users/paulmandelos/Desktop/RedBirdsFootball/coacht.csv')
#print(d2)