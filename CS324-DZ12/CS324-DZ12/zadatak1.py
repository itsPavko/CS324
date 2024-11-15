import pandas as pd
import numpy as np
n = 500
np.random.seed(0)  
df = pd.DataFrame({
    'cs_101_ocena': np.random.randint(5, 11, size=n),
    'it_101_ocena': np.random.randint(5, 11, size=n),
    'ma_101_ocena': np.random.randint(5, 11, size=n),
    'cs_115_izostanci': np.random.randint(0, 16, size=n),
    'cs_115_položen': np.random.randint(0, 2, size=n),
    'cs_115_ocena': np.random.randint(5, 11, size=n),
})

df.loc[df['cs_101_ocena'].between(8, 10), 'cs_115_ocena'] = df['cs_115_ocena'] + 1
df.loc[df['cs_115_izostanci'].between(5, 12), 'cs_115_ocena'] = df['cs_115_ocena'] - 1
df.loc[df['cs_115_izostanci'].between(13, 15), 'cs_115_ocena'] = df['cs_115_ocena'] - 2
df.loc[df['ma_101_ocena'].between(9, 10), 'cs_115_ocena'] = df['cs_115_ocena'] + 1
df.loc[df['cs_115_položen'] == 0, 'cs_115_ocena'] = 5

df['cs_115_ocena'] = df['cs_115_ocena'].clip(lower=5, upper=10)

df.to_csv('dataset.csv', index=False)