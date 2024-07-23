import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.formula.api import ols
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
import statsmodels.stats.multicomp as mc

def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    
    d = (np.mean(group1) - np.mean(group2)) / pooled_std
    
    return d


import matplotlib.pyplot as plt
import matplotlib.collections as clt
import scipy as sp
import ptitprince as pt

d = pd.read_csv("../results/results-t300.csv")
d = d[-d['populism'].isna()]
d = d[-d['ideology'].isna()]

print('Value counts for populism variable:')
d["ideology"].value_counts(dropna=False)

print('Count for populism variable:')
d["populism"].count()

d['left'] = pd.NA
d.loc[d['ideology']<3,'left']= 1
d.loc[d['ideology']>=3,'left']= 0

d['lib'] = pd.NA
d.loc[(d['ideology']==1) | (d['ideology']==3), 'lib'] = 1
d.loc[(d['ideology']==2) | (d['ideology']==4), 'lib'] = 0

# LEFT

print('Mean negative score for Left')
d.loc[d["left"]==1,"negative"].mean().round(3)

print('Mean negative score for Right')
d.loc[d["left"]==0,"negative"].mean().round(3)

print('t-test for negative emotions')
sp.stats.ttest_ind(d.loc[d["left"]==0,"negative"],d.loc[d["left"]==1,"negative"],equal_var=False)

cohens_d(d.loc[d["left"]==0,"negative"],d.loc[d["left"]==1,"negative"])

print('Mean neutral score for left')
d.loc[d["left"]==1,"neutral"].mean().round(3)

print('Mean neutral score for populists')
d.loc[d["left"]==0,"neutral"].mean().round(3)

print('t-test for neutral expression')
sp.stats.ttest_ind(d.loc[d["left"]==0,"neutral"],d.loc[d["left"]==1,"neutral"],equal_var=False)

cohens_d(d.loc[d["left"]==0,"neutral"],d.loc[d["left"]==1,"neutral"])

# LIB

print('Mean negative score for Liberals')
d.loc[d["lib"]==1,"negative"].mean().round(3)

print('Mean negative score for Convervatives')
d.loc[d["lib"]==0,"negative"].mean().round(3)

print('t-test for negative emotions')
sp.stats.ttest_ind(d.loc[d["lib"]==0,"negative"],d.loc[d["lib"]==1,"negative"],equal_var=False)

cohens_d(d.loc[d["lib"]==0,"negative"],d.loc[d["left"]==1,"negative"])

print('Mean neutral score for Liberals')
d.loc[d["lib"]==1,"neutral"].mean().round(3)

print('Mean neutral score for Conservatives')
d.loc[d["lib"]==0,"neutral"].mean().round(3)

print('t-test for neutral expression')
sp.stats.ttest_ind(d.loc[d["lib"]==1,"neutral"],d.loc[d["lib"]==0,"neutral"],equal_var=False)

cohens_d(d.loc[d["lib"]==0,"neutral"],d.loc[d["lib"]==1,"neutral"])


# Repeat analysis for populism

d.loc[d["populism"]<3,"populism2"] = "Pluralist"
d.loc[d["populism"]>=3,"populism2"] = "Populist"

sp.stats.ttest_ind(d.loc[d["populism2"]=="Pluralist","negative"],d.loc[d["populism2"]=="Populist","negative"],equal_var=False)

cohens_d(d.loc[d["populism2"]=="Pluralist","negative"],d.loc[d["populism2"]=="Populist","negative"])

cohens_d(d.loc[d["populism2"]=="Pluralist","neutral"],d.loc[d["populism2"]=="Populist","neutral"])

