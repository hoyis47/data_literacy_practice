import numpy as np
import pandas as pd
import seaborn as sns
import pdtypes

df = sns.load_dataset('titanic')
print(df.head())

# print(df.describe())

# print(df.count())
# print(df['age'].count())

# print(df.mean())
# print(df['age'].mean())

# print(df['age'].sum())

# print(df.loc[(df['age'] >= 20),'age'].mean())

# print(df.loc[(df['fare'] >= 30) & (df['fare'] < 40) & (df['pclass'] == 1),'pclass'].count())

# print(df.loc[(df['fare'] >= 30) & (df['fare'] < 40) & (df['pclass'] == 1),'age'].count())
# print(df.loc[(df['fare'] >= 30) & (df['fare'] < 40) & (df['pclass'] == 1),'age'].mean())

# print(df.mean(skipna=False))
# print(df.mean(skipna=True))

# print(pd.Series([1,2,3,4,5]).median())

# # print(f"나이평균:{df['age'].mean():.2f}\n나이중앙값:{df['age'].median()}\n차이:{df['age'].mean()-df['age'].median():.5f}")
# print(df.sum())
# print(df['fare'].sum())

# print(df['age'].cumsum())
# print(df['age'].cumprod())

# print(df['fare'].var())
# print(df['fare'].std())
# print(df['age'].min())
# print(df['age'].max())

# print(df['age'].agg(['min','max','count','mean']))
# print(df[['age','fare']].agg(['min','max','count','mean']))

# print(type(df['age']))
# print(type(df[['age','fare']]))



# print(df['age'].quantile(0.1))
# print(df['age'].quantile(0.2))
# print(df['age'].quantile(0.5))
# print(df['age'].quantile(0.8))
# print(df['age'].median())

print(df['who'].unique())
print(df['who'].nunique())
print(df['who'].mode())
print(df['deck'].mode())

print(df.corr())
print(df.corr()['survived'])