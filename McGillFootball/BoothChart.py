import pandas as pd
base='/Users/paulmandelos/Desktop/RedBirdsFootball/'
df = pd.read_excel(f'{base}BOOTH CHART AND GRADES.xlsx')
plays = pd.read_csv(f'{base}2023_WRIST_BAND.csv')
df = df.merge(plays[['#','Play']],how='left',left_on='PLAY#',right_on='#')
df['PLAYCALL'] = df['Play']
df.drop(['Play','#'],axis=1,inplace=True)
df.to_excel(f'{base}BOOTH CHART AND GRADES.xlsx')