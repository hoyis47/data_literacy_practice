import numpy as np
import pandas as pd
import seaborn as sns
import pdtypes
from pyskim import skim

df = sns.load_dataset("titanic")
# print(df.head(10))
# print(df.tail(10))
# print(df.info())
# print(df.describe())
# print(df.describe(include='object'))
# print(df['who'].value_counts())
# print(df['embark_town'].value_counts())

# print(df.ndim)
# print(df.shape)
# print(df.index)
# print(df.columns)

# print(df.values)
# print(df.T)

# print(df['class'].value_counts(normalize=True))

# print(df.info())
# print(df.describe(include='object') )

# print(df.info())

# df['pclass'].astype('int32')
# print(df.info())

# print(df.sort_index(ascending=False).head(5))

# print(df.sort_values(by='class', ascending=False).head())

# print(df.dtypes)

# print(df.sort_values(by=['fare','age'], ascending=[False,True]).head())

tips = sns.load_dataset('tips')
# print(tips.sort_values(by=['total_bill','tip'], ascending=[False,False]).head(10))

# print(tips.sort_values(by=['size','tip'], ascending=[False,True]).head(10))

# print(df.head(10))
# print(df.loc[1:5,'class'])
# print(df.loc[2:5,['age','fare','who']])

# print(df.loc[2:5,'class':'deck'].head())
# print(df.loc[:6,'class':'deck'].head())

# cond = df['who'] == 'man'
# print(cond)

# print(df[cond].head())

# print(df.loc[cond].head())

# print(df[cond]['age'])
# df.loc[cond, 'age'] = 2
# print(df)

# print((df.loc[df['age'] >= 30.0]).sort_values(by='fare', ascending=False).head(10))

# skim(df)

# print(df['pclass'].dtype)
# df['pclass'] = df['pclass'].astype('int32')
# print(df)

# print(tips['day'].value_counts())
# print(tips['day'].unique())

# print(df['who']=='man')
# print(df.loc[df['who']=='man', 'age'])

# df.loc[df['who']=='man', 'age'] = 10

# print(df.loc[df['who']=='man','age'])
# print(df['class'])


# print(df.loc[(df['fare'] > 30) & (df['who'] == 'woman')].sort_values(by='fare', ascending=False))

# print(df.loc[df['age'] >= 30].sort_values(by='fare', ascending=False).head(10))

# print(df.loc[(df['age'] >= 20) 
#              & (df['age'] < 40) 
#              & (df['pclass'] < 3), ['survived', 'pclass','age','fare']].head(10))
# print(df['age'].isnull().sum())
# print(df['age'].mean())

# df.loc[df['age'].isnull(), 'age'] = df['age'].mean()

# print((df['age'] == df['age'].mean()).sum())

# print(df.head())
# print(df.iloc[1])
# print(df.iloc[1,3])
# print(df.iloc[[1,3,4],[0,5,6,]])
# print(df.iloc[:3, :5])

# print(df.at[0,'fare'])
# print(df.iat[0,5])
# print(df.tail(5))

# print(df['fare'].where(df['fare'] < 20).tail(5))

# print(df.where(df['fare'] < 10)) 
#    
# print(df)
# print(df['who'].isin(['man']))
# print(df.loc[df['who'].isin(['man'])])

print(tips.head())

print(tips.loc[((tips['day'].isin(['Fri','Sat'])) 
                & (tips['tip'] < 10))
               ,['total_bill','tip','smoker','time','day']].head(10))