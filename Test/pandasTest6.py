import numpy as np
import pandas as pd
import seaborn as sns
import pdtypes

df = sns.load_dataset('titanic')

# df['VIP']=True
# print(df)

# df = df.drop(1)
# print(df)

# df = df.drop(np.arange(10))
# print(df)

# df = df.drop([1,3,5,7,8])
# print(df)

# print(df.drop('pclass', axis=1).head())

# df.drop(['who','deck','alive'], axis=1, inplace=True)
# print(df)


# df.drop([1,3,5], inplace=True)
# print(df)

# df.drop(['embarked','class','alone'], axis=1, inplace=True)
# print(df)

# df['family'] = df['sibsp'] + df['parch']
# print(df.head())

# df['gender'] = df['who'] + '-' + df['sex']
# print(df.head())

# df['round'] = round(df['fare'] / df['age'], 2)
# print(df)

# print(df.loc[df['age'].isnull(), 'deck':].head())

# print(df['pclass'].astype('int32').head())
# print(df)

# df['pclass']=df['pclass'].astype('str')
# print(df)

# print(df['who'].value_counts())
# print(df['who'].dtype)
# print(df['who'].astype('category'))

df['who']=df['who'].astype('category')

# print(df['who'].dtype)

# print(df['who'].cat.codes)



df['who'].cat.categories = [f'Group{g}' for g in df['who'].cat.categories]
print(df['who'].value_counts())
