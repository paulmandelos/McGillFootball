import pandas as pd
pd.set_option('display.max_columns', 500)
df = pd.read_excel('/Users/paulmandelos/Downloads/MTL_ALL_AVAILABLE_FULL_GAMES.xlsx')
df.dropna(subset=['BLITZ','RESULT'],inplace=True)

df = df[df['ODK']=='D']
print(df.columns)
print(list(df.OPPONENT.unique()))
complete = ['Complete','Complete, TD','Scramble']
incomplete = ['Incomplete','Dropped']
df['isComplete'] = df['RESULT'].isin(complete)
df['isIncomplete'] = df['RESULT'].isin(incomplete)
df['isPass'] = df['PLAY TYPE'].str.contains('Pass')
df['isFirstDown'] = df['GN/LS'] > df['DIST']
df2 = df[['GN/LS','BLITZ','RESULT','isPass','isComplete','isIncomplete','isFirstDown']]
df2['isSack'] = df2['RESULT'].str.contains('Sack')
df3 = df2.groupby(by=['BLITZ'])['isSack'].count().to_frame('NumberOfPlays').reset_index()
df3['Comp%'] = round(df2.groupby(by=['BLITZ'])['isComplete'].mean()* 100,0).to_frame('mean').reset_index()['mean']
df3['Incomp%'] = round(df2.groupby(by=['BLITZ'])['isIncomplete'].mean()* 100,0).to_frame('mean').reset_index()['mean']
df3['FirstDown%'] = round(df2.groupby(by=['BLITZ'])['isFirstDown'].mean()* 100,0).to_frame('mean').reset_index()['mean']
df3['Sack%'] = round(df2.groupby(by=['BLITZ'])['isSack'].mean()* 100,0).to_frame('mean').reset_index()['mean']
df3['Pass%'] = round(df2.groupby(by=['BLITZ'])['isPass'].mean()* 100,0).to_frame('mean').reset_index()['mean']
df3['AverageGainOrLoss'] = round(df2.groupby(by=['BLITZ'])['GN/LS'].mean(),0).to_frame('mean').reset_index()['mean']
df3.sort_values(by=['NumberOfPlays','Sack%'],ascending=False,inplace=True)
print(df3)