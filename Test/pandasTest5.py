import numpy as np
import pandas as pd
import seaborn as sns
import pdtypes

df = sns.load_dataset('titanic')

df_copy = df.copy()
# print(df_copy)

# print(id(df))
# print(id(df_copy))

# df_copy.loc[0,'age'] = 99999
# print(df_copy.head(5))
# print(df.head(5))

# print(df.isnull().sum())
# print(df.isna().sum())

# print(df.isnull().sum().sum())

# print(df.notnull().sum())
# print(df.notnull())

# print(df.loc[df['age'].isnull()])

# df.loc[df['age'].isnull(), 'age'] = 30
# # print(df.head(30))

# assert df['age'].isnull().sum() == 0
# assert df['age'].mean().round(4) == 29.7589

# print(df_copy['age'].fillna(700).tail())
# df_copy['age'] = df_copy['age'].fillna(600)
# print(df_copy.head(10))

# print(df_copy['deck'].isnull().sum())
# print(df_copy['deck'].unique())

# df_copy['deck'] = df_copy['deck'].fillna('A')
# print(df_copy.head(10))

# print(df_copy['deck'].cat.add_categories('No Data').fillna('No Data').head(10))

# df_copy['age'] = df_copy['age'].fillna(df_copy['age'].mean())
# print(df_copy.head(10))

# cond_m_age = df_copy.loc[(df_copy['sex']=='male'),'age']
# cond_f_age = df_copy.loc[(df_copy['sex'] == 'female'), 'age']
# print(type(cond_f_age))
# print(cond_m_age.mean())

# df_copy.loc[(df_copy['sex']=='male'),'age'] = df_copy.loc[(df_copy['sex']=='male'),'age'].fillna(df_copy.loc[(df_copy['sex']=='male'),'age'].mean())

# print(cond_m_age.fillna(cond_m_age.mean()))

# print(cond_f_age.mean())
# df_copy.loc[(df_copy['sex'] == 'female'), 'age'] = df_copy.loc[(df_copy['sex'] == 'female'), 'age'].fillna(df_copy.loc[(df_copy['sex'] == 'female'), 'age'].mean())
# print(cond_f_age.fillna(cond_f_age.mean()))

# print(df_copy.head(30))

# assert(df_copy['age'].isnull().sum() == 0)
# print(df_copy['age'].mean())

# print(df_copy['deck'].mode())

# print(df_copy['deck'].isnull().sum())

# df_copy['deck']=df_copy['deck'].fillna(df_copy['deck'].mode()[0])
# print(df_copy['deck'].fillna(df_copy['deck'].mode()[0]).tail())
# print(df_copy['deck'].isnull().sum())


df_copy = df_copy.dropna(how='all')
print(df_copy.head(10))