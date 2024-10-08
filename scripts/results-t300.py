import numpy as np
import pandas as pd
import seaborn as sns
from statsmodels.formula.api import ols
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
import statsmodels.stats.multicomp as mc


import matplotlib.pyplot as plt
import matplotlib.collections as clt
import scipy as sp
import ptitprince as pt

d = pd.read_csv("results/results-t300.csv")
d = d[-d['populism'].isna()]


def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    
    d = (np.mean(group1) - np.mean(group2)) / pooled_std
    
    return d


# TABLE 1

d[["anger","disgust","fear","happy","sad","surprise","neutral","negative"]].describe().round(3).to_csv("../results/t300-emotions-summary.csv")

# frequencies of populism

print('Value counts for populism variable:')
d["populism"].value_counts()

print('Count for populism variable:')
d["populism"].count()

# FIGURE 2

d["populism2"] = d["populism"]

d.loc[d["populism"]<3,"populism2"] = "Pluralist"
d.loc[d["populism"]>=3,"populism2"] = "Populist"

sns.set(style = "whitegrid")
sns.set(rc={'figure.figsize':(8,8)})

plt.clf()
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey='row')
sns.swarmplot(ax=ax1, x = "populism2", y = "negative", data = d, hue="populism2")
ax1.set_ylabel("Avg. score of negative emotions")
ax1.set_xlabel("")
ax1.legend([],[], frameon=False)
sns.swarmplot(ax=ax2, x = "populism2", y = "neutral", data = d, hue="populism2")
ax2.set_ylabel("Avg. score of neutral expression")
ax2.set_xlabel("")
ax2.legend([],[], frameon=False)
plt.savefig('../figures/fig2.png')

print('Mean negative score for pluralists')
d.loc[d["populism2"]=="Pluralist","negative"].mean().round(3)

print('Mean negative score for populists')
d.loc[d["populism2"]=="Populist","negative"].mean().round(3)

print('t-test for negative emotions')
sp.stats.ttest_ind(d.loc[d["populism2"]=="Pluralist","negative"],d.loc[d["populism2"]=="Populist","negative"],equal_var=False)

print('Mean neutral score for pluralists')
d.loc[d["populism2"]=="Pluralist","neutral"].mean().round(3)

print('Mean neutral score for populists')
d.loc[d["populism2"]=="Populist","neutral"].mean().round(3)

print('t-test for neutral expression')
sp.stats.ttest_ind(d.loc[d["populism2"]=="Pluralist","neutral"],d.loc[d["populism2"]=="Populist","neutral"],equal_var=False)


# FIGURE 3

d1 = d.dropna()
d1["populism"] = d1["populism"].astype('int')
sns.set(style="whitegrid",font_scale=2)


dx = "populism"; dy = "negative"; ort = "h"; pal = "Set2"; sigma = .25
dy2 = "neutral"

f, ax = plt.subplots(figsize=(10, 8))

ax1=pt.RainCloud(x = dx, y = dy, data = d1, palette = pal, bw = sigma,
                 width_viol = 0.75, ax = ax, orient = ort, move = .2)

plt.axvline(0.5, 0,2, color = 'black', linestyle='--', alpha = 0.6)
plt.xlabel("Avg. score of negative emotions")
plt.ylabel("Degree of populism")
plt.savefig('../figures/fig3.png', bbox_inches='tight')

# FIGURE 4

d1 = d.dropna()
d1["populism"] = d1["populism"].astype('int')
sns.set(style="whitegrid",font_scale=2)


dx = "populism"; dy = "neutral"; ort = "h"; pal = "Set2"; sigma = .25
dy2 = "neutral"

f, ax = plt.subplots(figsize=(10, 8))

ax1=pt.RainCloud(x = dx, y = dy, data = d1, palette = pal, bw = sigma,
                 width_viol = 0.75, ax = ax, orient = ort, move = .2)

plt.axvline(0.5, 0,2, color = 'black', linestyle='--', alpha = 0.6)
plt.xlabel("Avg. score of neutral expression")
plt.ylabel("Degree of populism")
plt.savefig('../figures/fig4.png', bbox_inches='tight')


# Country-level analysis

### Country-means

countries = d['country'].unique()
negatives = []
neutrals = []
for country in countries:
    negatives.append(d.loc[d['country']==country,'negative'].mean().round(3))
    neutrals.append(d.loc[d['country']==country,'neutral'].mean().round(3))
country_means = pd.DataFrame({'country':countries,'negative':negatives,'neutral':neutrals})
country_means.to_csv('../results/country-means-f50.csv', index=False)

### Country X populism means

countries = d['country'].unique()
populisms = d['populism2'].unique()
populisms = populisms[::-1]
negatives = []
neutrals = []
for country in countries:
    for populism in populisms:
        print(country)
        print(populism)
        if (len(d.loc[(d['country']==country)&(d['populism2']==populism)])>0):
            print(d.loc[(d['country']==country)&(d['populism2']==populism),'negative'].mean().round(3))
            negatives.append(d.loc[(d['country']==country)&(d['populism2']==populism),'negative'].mean().round(3))
            print(d.loc[(d['country']==country)&(d['populism2']==populism),'neutral'].mean().round(3))
            neutrals.append(d.loc[(d['country']==country)&(d['populism2']==populism),'neutral'].mean().round(3))
        else:
            negatives.append(np.nan)
            neutrals.append(np.nan)

pops = np.tile(populisms, len(countries))
df = pd.DataFrame({'country':np.repeat(countries, len(populisms)),'populism':pops,'negative':negatives,'neutral':neutrals})
df.to_csv('../results/country-populism-means-f50.csv', index=False)


# FIGURE 8

f, ax = plt.subplots(figsize=(16, 8))
hue_order= ['Pluralist','Populist']
sns.swarmplot(x='country', y='negative', hue='populism', data=df, marker='D', size = 5, hue_order= ['Pluralist','Populist', ])
sns.swarmplot(x='country', y='negative', hue='populism2', data=d,alpha=0.5, size=3,hue_order= ['Pluralist','Populist', ])
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles, hue_order, title='Populism', loc='upper right')

plt.xlabel("Country")
plt.ylabel("Score of negative emotions")

plt.savefig('../figures/fig8.png', bbox_inches='tight')

# FIGURE 9

f, ax = plt.subplots(figsize=(16, 8))
hue_order= ['Pluralist','Populist']
sns.swarmplot(x='country', y='neutral', hue='populism', data=df, marker='D', size = 5, hue_order= ['Pluralist','Populist', ])
sns.swarmplot(x='country', y='neutral', hue='populism2', data=d,alpha=0.5, size=3,hue_order= ['Pluralist','Populist', ])
handles, labels = plt.gca().get_legend_handles_labels()
plt.legend(handles, hue_order, title='Populism', loc='upper left')

# axis labels "Country" and "Avg. score of negative emotions"
plt.xlabel("Country")
plt.ylabel("Score of neutral expression")
# title of the legend "Populism"

plt.savefig('../figures/figA4-2', bbox_inches='tight')

# ANOVA

## Negative

d2 = d.dropna()
d2["populism"] = d2["populism"].astype('str')

model = ols('negative ~ populism', data=d2).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table
print('ANOVA table for negative emotions')
esq_sm = aov_table['sum_sq'][0]/(aov_table['sum_sq'][0]+aov_table['sum_sq'][1])
aov_table['EtaSq'] = [esq_sm, 'NaN']
print('Table for negative emotions with eta-squared')
print(aov_table)

## Neutral emotions

print('ANOVA table for neutral emotions')
model = ols('neutral ~ populism', data=d2).fit()
aov_table = sm.stats.anova_lm(model, typ=2)
aov_table
esq_sm = aov_table['sum_sq'][0]/(aov_table['sum_sq'][0]+aov_table['sum_sq'][1])
aov_table['EtaSq'] = [esq_sm, 'NaN']
print('Table for neutral emotions with eta-squared')
print(aov_table)


comp = mc.MultiComparison(d2['negative'],d2['populism'])
print('Tukey HSD for negative emotions')
print(comp.tukeyhsd())

comp = mc.MultiComparison(d2['neutral'],d2['populism'])
print('Tukey HSD for neutral emotions')
print(comp.tukeyhsd())
