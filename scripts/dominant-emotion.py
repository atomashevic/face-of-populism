import numpy as np
import pandas as pd

# t300

urls = pd.read_csv('../results/yt-urls-mark-manual-t300.csv')
gps = pd.read_csv('../data-clean/gps.csv')
n = len(urls)

results = pd.DataFrame(0.0, dtype = float, index = range(n), columns = range(9) )
results.columns = ['angry', 'disgust','fear','happy','sad','surprise','neutral','negative','populism']

for i in range(n):
    f = urls['Face'][i]
    print(i)
    if (f<99 and i!=159):
        df = pd.read_csv('data-clean/%i-t300.csv' %i)
        party = gps[(gps["CPARTYABB"] == urls["party"][i])]
        df = df.iloc[:, 1:]
        df = df.iloc[:,f*8+1:f*8+8]
        m = len(df)
        for j in range(m):
            # print(j)
            if df.iloc[j].isna().sum() < 7:
                max_col_label = df.iloc[j].idxmax()
                max_col_number = df.columns.get_loc(max_col_label)
            results.iloc[i,max_col_number] = results.iloc[i,max_col_number] + 1/m   
            if(df.iloc[j,[0,1,2,4]].sum() >= 0.5):
                results.iloc[i,7] = results.iloc[i,7] + 1/m
            if (not party.empty):
                results.iloc[i,8] = party['Type_Populism'].values[0]
results.to_csv('../results/t300-dominant-emotions.csv')

#Pluralists
results[results['populism'].astype(float)<3].describe()

results[results['populism'].astype(float)>=3].describe()


# f50

urls = pd.read_csv('../results/yt-urls-mark-manual-f50.csv')
gps = pd.read_csv('../data-clean/gps.csv')
n = len(urls)

results = pd.DataFrame(0.0, dtype = float, index = range(n), columns = range(9) )
results.columns = ['angry', 'disgust','fear','happy','sad','surprise','neutral','negative','populism']

for i in range(n):
    f = urls['Face'][i]
    print(i)
    if (f<99 and i!=159):
        df = pd.read_csv('data-clean/%i-f50.csv' %i)
        party = gps[(gps["CPARTYABB"] == urls["party"][i])]
        df = df.iloc[:, 1:]
        df = df.iloc[:,f*8+1:f*8+8]
        m = len(df)
        for j in range(m):
            # print(j)
            if df.iloc[j].isna().sum() < 7:
                max_col_label = df.iloc[j].idxmax()
                max_col_number = df.columns.get_loc(max_col_label)
            results.iloc[i,max_col_number] = results.iloc[i,max_col_number] + 1/m   
            if(df.iloc[j,[0,1,2,4]].sum() >= 0.5):
                results.iloc[i,7] = results.iloc[i,7] + 1/m
            if (not party.empty):
                results.iloc[i,8] = party['Type_Populism'].values[0]

results.to_csv('../results/f50-dominant-emotions.csv')


print('Descriptive statistics for Pluralists')
results[results['populism'].astype(float)<3].describe()

print('Descriptive statistics for Populists')
results[results['populism'].astype(float)>=3].describe()

