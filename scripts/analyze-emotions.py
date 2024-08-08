import numpy as np
import pandas as pd
import os

# helper functions

def mark_multiple_faces(csvfile,mode):
    url_df = pd.read_csv(csvfile)
    url_df["Face"] = 0
    n = len(url_df)
    for i in range(0,n):
        temp_file = '../data-clean/%s-%s.csv' %(i,mode)
        if not os.path.exists(temp_file):
            continue
        else:
            tcsv = pd.read_csv('../data-clean/%s-%s.csv' %(i,mode))
            nfaces = int((tcsv.shape[1]-1)/8)
            if nfaces>1:
                box1 = tcsv['box1']
                p = sum(~pd.isnull(box1))/box1.shape[0]
                print('For this video in %s %% of all frames we have a second face' %(np.round(100*p)))
                if p>0.05:
                    url_df["Face"][i] = 999
    url_df.to_csv('../results/yt-urls-mark-%s.csv' %(mode))

def fix_object(o):
    n = o.name
    if n in ['Type_Populism',"Type_Values","Type_Populist_Values"]:
        if len(o) > 0:
            return(float(o))
        else:
            return(np.nan)
    else:
        if len(o) > 0:
            if "NULL" in str(o):
                return(np.nan)
            else:
                return(float(o))
        else:
            return(np.nan)

def create_results_df(mode='f50') -> pd.DataFrame
    urls = pd.read_csv(f"../results/yt-urls-mark-manual-{mode}.csv")
    n = len(urls)
    ids = []
    anger = []
    disgust = []
    fear = []
    happy = []
    sad = []
    surprise = []
    neutral = []
    values = []
    countries = []
    populism = []
    populism_values = [] 
    psize = []
    psize_seat = []
    for i in range(0,n):
        if (not i in trash):
            tcsv = pd.read_csv('data-clean/%s-%s.csv' %(i, mode))
            if (i in cut_vids):
                a = cut_from[cut_vids == i][0]
                b = cut_to[cut_vids == i][0]
            else:
                a = 0
                b = len(tcsv)
            k = urls["Face"][i]
            ang = tcsv["angry%s" %(k)][a:b].dropna().mean()
            dis = tcsv["disgust%s" %(k)][a:b].dropna().mean()
            fea = tcsv["fear%s" %(k)][a:b].dropna().mean()
            hap = tcsv["happy%s" %(k)][a:b].dropna().mean()
            sd = tcsv["sad%s" %(k)][a:b].mean()
            sur = tcsv["surprise%s" %(k)][a:b].mean()
            neu = tcsv["neutral%s" %(k)][a:b].mean()
            ids.append(i)
            anger.append(ang)
            disgust.append(dis)
            fear.append(fea)
            happy.append(hap)
            sad.append(sd)
            surprise.append(sur)
            neutral.append(neu)
            party = gps[(gps["CPARTYABB"] == urls["party"][i])]
            countries.append(urls["party"][i].split('_')[0])
            populism.append(fix_object(party["Type_Populism"]))
            values.append(fix_object(party["Type_Values"]))
            populism_values.append(fix_object(party["Type_Populist_Values"]))
            psize.append(fix_object(party["Type_Partysize_vote"]))
            psize_seat.append(fix_object(party["Type_Partysize_seat"]))
    results = pd.DataFrame({'id':ids, 'country':countries,'populism':populism, 'values':values, 'populism_values':populism_values,'psize':psize,'psize_seat':psize_seat,'anger':anger,'disgust':disgust,'fear':fear,'happy':happy,'sad':sad,'surprise':surprise,'neutral':neutral})
    results['negative'] = results['anger'] + results['disgust'] + results['fear'] + results['sad']
    results['populism_2'] = None
    results['populism_2'][results['populism']>2] = 1
    results['populism_2'][results['populism']<=2] = 0
    print('pop done!')
    results['ideology'] = None
    results['ideology'] = results['values']
    # results['lr_2'][results['values'] > 2] = 1
    # results['lr_2'][results['values'] <= 2] = 0
    print('lr done!')
    return results

# main data sources

urls = '../data-raw/yt-urls.csv'
gps = pd.read_csv('../data-raw/gps.csv')


# t300 data analysis

m = 't300'
mark_multiple_faces(urls, m)

# after this step MANUAL REVIEW of the `yt-urls-mark-t300.csv` file is needed
# during MANUAL REVIEW you need to replace 999 with face number which
# represents the selected leader
# also if there is no consistent face selection video is marked as trash below
# if there is consistent face selection only in some interval, then video need to be cut using frame numbers below

# manual review of `yt-urls-mark-t300.csv`
# after review

trash = [5, 11, 41, 43, 103, 104, 111, 112, 159, 205, 212, 214, 216]

cut_vids = np.array([7, 18, 25, 45, 59, 89, 105, 150, 158, 175, 186, 201])
cut_from = np.array([0, 24, 0, 52, 14, 0, 36, 30, 20, 0, 8, 0])
cut_to = np.array([204, 234, 280, 282, 291, 210, 294, 252, 283, 222, 218, 305])

# CAUTION: create results assumes after MANUAL REVIEW we 
# have CSV called results/yt-urls-mark-manual-%s.csv

res = create_results_df(m)
res.to_csv('results/results-%s.csv' %(m))


# f50 data analysis

m = 'f50'
mark_multiple_faces(urls, m)

# manual review of `yt-urls-mark-f50.csv`
# after review

trash = [18, 42, 43, 103, 159, 176, 214] # unsusable videos
cut_vids = np.array([79, 72, 89, 105, 108, 150, 180])
cut_from = np.array([0, 13, 0, 15, 4, 0, 0])
cut_to = np.array([262, 54, 383, 269, 272, 214, 200])



res = create_results_df(m) 
res.to_csv('../results/results-%s.csv' %(m))

