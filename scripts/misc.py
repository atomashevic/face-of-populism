import numpy as np
import pandas as pd
import pytube

urls = pd.read_csv('../data-raw/yt-urls.csv')
length = 0

# Total length of the videos
for i in range(0,len(urls)):
    print(i)
    if i!=84 and i!=159:
        yt = pytube.YouTube(urls.loc[i,'url'])
        length = length + yt.length

# Average number of frames
frames = 0

for i in range(0,len(urls)):
    if i!=84 and i!=159:
        tdf = pd.read_csv('data-clean/%s-f50.csv' %(i))
        frames = frames + len(tdf)

print('Mean number of frames:')
print(frames/len(urls))