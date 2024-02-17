# %%
import pandas as pd
import numpy as np
import collections

# %%
df = pd.read_csv('.lesson/assets/FemPreg.csv')
# %%
df.columns
# %%
pregord = df['pregordr']
type(pregord)
pregord
# %%
df['totalwgt_lb'] = df.birthwgt_lb + df.birthwgt_oz / 16.0
# %%
df.outcome.value_counts().sort_index()
# %%
df.birthwgt_lb.value_counts().sort_index()
# %%
df.loc[df.birthwgt_lb == 15.0, 'birthwgt_lb'] = np.nan
df.birthwgt_lb.value_counts().sort_index()
# %%
df.query('caseid == 10229')[['caseid', 'row_number', 'outcome']]
# %%
from pathlib import Path
Path('plots').mkdir(parents=True, exist_ok=True)
# %%
t = (0,1,1,2,2,2,1,1,1,2,2,1,2,1,0,1,0,0,1,1,2,1,2,0,1,2,0,1,2,1,2,1,2,)
hist = {}
for x in t:
    hist[x] = hist.get(x,0) + 1 
# %%
from collections import Counter
counter = Counter(t)
# %%
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
mpl.rcParams['figure.dpi']= 150
import pandas as pd
df = pd.read_csv('.lesson/assets/FemPreg.csv')
hist0 = sns.histplot(data=df, x="birthwgt_lb", discrete=True)
fig = hist0.get_figure()
fig.savefig(f'plots/birthwgt_lb.png')
plt.clf()
# %%
# %%
hist1 = sns.histplot(data=df, x="birthwgt_oz", discrete=True)
fig1 = hist1.get_figure()
fig1.savefig('plots/birthwgt_oz.png')
plt.clf()
# %%
hist2 = sns.histplot(data=df, x="agepreg", discrete=True)
fig = hist2.get_figure()
fig.savefig('plots/agepreg.png')
plt.clf()
# %%
hist3 = sns.histplot(data=df, x="prglngth", discrete=True)
fig = hist3.get_figure()
fig.savefig('plots/prglngth.png')
plt.clf()
# %%
(df.
    query('outcome == 1').
    nsmallest(10, 'prglngth').
    loc[:,'prglngth']
)
# %%
(df.
    query('outcome == 1').
    nlargest(10, 'prglngth').
    loc[:,'prglngth']
)
# %%
transform = lambda x: True if x==1 else False
# %%
df = df.assign(firstborn = df.birthord.map(transform))
# %%
hist4 = sns.histplot(data=df, x="prglngth", discrete=True, hue='firstborn')
fig = hist4.get_figure()
fig.savefig('plots/first_born.png')
plt.clf()
# %%
df.query('outcome == 1').prglngth.mean()
df.query('outcome == 1').prglngth.var()
df.query('outcome == 1').prglngth.std()
# %%
