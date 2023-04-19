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

d = pd.read_csv("../results/results-t300.csv")
d = d[-d['populism'].isna()]


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
