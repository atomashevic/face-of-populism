import numpy as np
import pandas as pd
# Videos from Japenese leaders
# LDP: 190-194
# NKP: 195-199
# CDP: 200-204

ldp1 = pd.read_csv('data-clean/190-t300.csv')
ldp2 = pd.read_csv('data-clean/191-t300.csv')
ldp3 = pd.read_csv('data-clean/192-t300.csv')
ldp4 = pd.read_csv('data-clean/193-t300.csv')
ldp5 = pd.read_csv('data-clean/194-t300.csv')

ldp1['negative'] = ldp1['angry0'] + ldp1['sad0'] + ldp1['fear0'] + ldp1['disgust0']
ldp2['negative'] = ldp2['angry0'] + ldp2['sad0'] + ldp2['fear0'] + ldp2['disgust0']
ldp3['negative'] = ldp3['angry0'] + ldp3['sad0'] + ldp3['fear0'] + ldp3['disgust0']
ldp4['negative'] = ldp4['angry0'] + ldp4['sad0'] + ldp4['fear0'] + ldp4['disgust0']
ldp5['negative'] = ldp5['angry0'] + ldp5['sad0'] + ldp5['fear0'] + ldp5['disgust0']

ldp1_ng = ldp1['negative'].mean()
ldp1['negative'].max()
ldp1_nt = ldp1['neutral0'].mean()
ldp1['neutral0'].max()
ldp1['angry0'].max()

ldp2_ng = ldp2['negative'].mean()
ldp2['negative'].max()
ldp2_nt = ldp2['neutral0'].mean()
ldp2['neutral0'].max()
ldp2['angry0'].max()

ldp3_ng = ldp3['negative'].mean()
ldp3['negative'].max()
ldp3_nt = ldp3['neutral0'].mean()
ldp3['neutral0'].max()
ldp3['angry0'].max()

ldp4_ng = ldp4['negative'].mean()
ldp4['negative'].max()
ldp4_nt = ldp4['neutral0'].mean()
ldp4['neutral0'].max()
ldp4['angry0'].max()

ldp5_ng = ldp5['negative'].mean()
ldp5['negative'].max()
ldp5_nt = ldp5['neutral0'].mean()
ldp5['neutral0'].max()
ldp5['angry0'].max()

ldp_ng = (ldp1_ng + ldp2_ng + ldp3_ng + ldp4_ng + ldp5_ng) / 5
ldp_nt = (ldp1_nt + ldp2_nt + ldp3_nt + ldp4_nt + ldp5_nt) / 5

ldp_ng
# 0.58
ldp_nt
# 0.38

nkp1 = pd.read_csv('data-clean/195-t300.csv')
nkp2 = pd.read_csv('data-clean/196-t300.csv')
nkp3 = pd.read_csv('data-clean/197-t300.csv')
nkp4 = pd.read_csv('data-clean/198-t300.csv')
nkp5 = pd.read_csv('data-clean/199-t300.csv')

nkp1['negative'] = nkp1['angry0'] + nkp1['sad0'] + nkp1['fear0'] + nkp1['disgust0']
nkp2['negative'] = nkp2['angry0'] + nkp2['sad0'] + nkp2['fear0'] + nkp2['disgust0']
nkp3['negative'] = nkp3['angry0'] + nkp3['sad0'] + nkp3['fear0'] + nkp3['disgust0']
nkp4['negative'] = nkp4['angry0'] + nkp4['sad0'] + nkp4['fear0'] + nkp4['disgust0']
nkp5['negative'] = nkp5['angry0'] + nkp5['sad0'] + nkp5['fear0'] + nkp5['disgust0']

nkp1_ng = nkp1['negative'].mean()
nkp1['negative'].max()
nkp1_nt = nkp1['neutral0'].mean()
nkp1['neutral0'].max()

nkp2_ng = nkp2['negative'].mean()
nkp2['negative'].max()
nkp2_nt = nkp2['neutral0'].mean()
nkp2['neutral0'].max()

nkp3_ng = nkp3['negative'].mean()
nkp3['negative'].max()
nkp3_nt = nkp3['neutral0'].mean()
nkp3['neutral0'].max()

nkp4_ng = nkp4['negative'].mean()
nkp4['negative'].max()
nkp4_nt = nkp4['neutral0'].mean()
nkp4['neutral0'].max()

nkp5_ng = nkp5['negative'].mean()
nkp5['negative'].max()
nkp5_nt = nkp5['neutral0'].mean()
nkp5['neutral0'].max()

nkp_ng = (nkp1_ng + nkp2_ng + nkp3_ng + nkp4_ng + nkp5_ng) / 5
nkp_nt = (nkp1_nt + nkp2_nt + nkp3_nt + nkp4_nt + nkp5_nt) / 5

nkp_ng
#0.27
nkp_nt
#0.68

cdp1 = pd.read_csv('data-clean/200-t300.csv')
cdp2 = pd.read_csv('data-clean/201-t300.csv')
cdp3 = pd.read_csv('data-clean/202-t300.csv')
cdp4 = pd.read_csv('data-clean/203-t300.csv')
cdp5 = pd.read_csv('data-clean/204-t300.csv')

cdp1['negative'] = cdp1['angry0'] + cdp1['sad0'] + cdp1['fear0'] + cdp1['disgust0']
cdp2['negative'] = cdp2['angry0'] + cdp2['sad0'] + cdp2['fear0'] + cdp2['disgust0']
cdp3['negative'] = cdp3['angry0'] + cdp3['sad0'] + cdp3['fear0'] + cdp3['disgust0']
cdp4['negative'] = cdp4['angry0'] + cdp4['sad0'] + cdp4['fear0'] + cdp4['disgust0']
cdp5['negative'] = cdp5['angry0'] + cdp5['sad0'] + cdp5['fear0'] + cdp5['disgust0']

cdp1_ng = cdp1['negative'].mean()
cdp1['negative'].max()
cdp1_nt = cdp1['neutral0'].mean()
cdp1['neutral0'].max()

cdp2_ng = cdp2['negative'].mean()
cdp2['negative'].max()
cdp2_nt = cdp2['neutral0'].mean()
cdp2['neutral0'].max()

cdp3_ng = cdp3['negative'].mean()
cdp3['negative'].max()
cdp3_nt = cdp3['neutral0'].mean()
cdp3['neutral0'].max()


cdp4_ng = cdp4['negative'].mean()
cdp4['negative'].max()
cdp4_nt = cdp4['neutral0'].mean()
cdp4['neutral0'].max()

cdp5_ng = cdp5['negative'].mean()
cdp5['negative'].max()
cdp5_nt = cdp5['neutral0'].mean()
cdp5['neutral0'].max()

cdp_ng = (cdp1_ng + cdp2_ng + cdp3_ng + cdp4_ng + cdp5_ng) / 5
cdp_nt = (cdp1_nt + cdp2_nt + cdp3_nt + cdp4_nt + cdp5_nt) / 5

cdp_ng
# 0.3011
cdp_nt
# 0.638
