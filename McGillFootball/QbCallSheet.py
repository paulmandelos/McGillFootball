import pandas as pd
#WHEREVER YOU HAVE THE DOCUMENT KEPT
base = '/Users/marcoingelmo/Desktop/mcgill football/SPRING CAMP/'
#EVERYTHING AFTER THE 'base' IS THE NAME OF THE FILE SO YOU CAN CHANGE IT TO WHAT EVER YOU WANT
cs = pd.read_csv(f'{base}2023_CALL_SHEET.csv')
df = pd.DataFrame(columns=['#','Play'])
df['#'] = cs['#']
cs['temp'] = cs['FORMATION'] + " " +  cs['PLAYS']
df['Play'] = cs['temp']

#IF YOU NEED TO ADD ANYTHING FOR THE CONVERSION ADD IT HERE 
#EXAMPLE PAIR TO USE ("TEXT 1","TEXT 2")
pairs = [("SAIL","SOAR"),
         ("HAIR","HEEL"),
         (" 2 "," 3 "),
         ("32","23"),
         ("33","22"),
         (" 6 "," 7 "),
         ("36","27"),
         (" 4 "," 5 "),
         ("34","25"),
         ("35","24"),
         (" 8 "," 9 "),
         ("28","39"),
         ("EAST","WEST"),
         ("LEB","ROSE"),
         ("70","71"),
         ("74","75"),
         ("76","77"),
         ("60","61"),
         ("64","65"),
         ("66","67"),
         ("50","51"),
         ("BLUE",'RED'),
         ("RAMBO","LIMBO"),
         ("RAM","LION"),
         ("RAZOR","LASER"),
         ("RAIN","LIGHT")]

def conversions(string,pairs):  
    for (x,y) in pairs:
        if x in string:
            string = string.replace(x,str(x + "|" +y))
        elif y in string:
            string = string.replace(y,str(y + "|" +x))
    if "RT" in string:
        string = string.replace("RT","RT/LT")
    elif "LT" in string:
        string = string.replace("LT","LT/RT")
    return string

df['Play'] = df.apply(lambda x: conversions(x.Play,pairs),axis=1)
#WHEREVER YOU WANT TO STORE THE FILE AND THE NAME
df.to_csv(f'{base}2023_WRIST_BAND.csv')