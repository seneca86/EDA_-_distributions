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
from pprint import pprint

d1 = collections.defaultdict(list)
for index, caseid in df.caseid.items():
    d1[caseid].append(index)
pprint(d1)
# %%
d1[10229]
df.outcome[d1[10229]]
# %%

