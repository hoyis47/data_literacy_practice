import pandas as pd
import numpy as np

arr = np.arange(100,150)

s = pd.Series(arr, dtype='int32')
# print(s)

s = pd.Series(['Hoy','Tae','Tong','Kong',3])
#print(s[-1])

s = pd.Series(['Marketing','Develop','Test'], index=['a1','a2','a3'])
# print(s['a2'], s[0])

# print(s.index)
# print(s.values)
# print(s[-1])

s=pd.Series(['Marketing','Test','Develop','Service'])
s.index = list('abcd')
# print(s.index)

# print(s.ndim)
# print(s.shape)
# print(s.size)

s = pd.Series(['TTT','SSS',np.nan,'AAA'])
# print(s)

arr = np.arange(50,55)
s1 = pd.Series(arr, dtype='float32')
# print(s1)

s2 = pd.Series(['apple',np.NaN,'banana','kiwi','gubong'])
s2.index = list('abcde')
# print(s2)

# print(s[1:3])

# print(s2.isnull())
# print(s2.isna())
# print(s2.notnull())
# print(s2.notna())
# print(s2[s2.notnull()])
# print(s2[[True,False,False,False,False]])
# print(s2[['a','c']])

df = pd.DataFrame([[1,2,3],
                   [4,5,6],
                   [7,8,9]], columns = ['가','나','다'])

# print(df['가'].values)
# print(df.columns)
# print(df.index)
# print(df.dtypes)
# print(df.T)
# print(df)

data = {
    'name' : ['Kim','Lee','Park'],
    'age' : [24,12,60],
    'children' : [2,3,2]
}

df = pd.DataFrame(data)
# print(df)
# print(df.index)
# print(df.columns)
# print(df.values)
# print(df.dtypes)
# print(df.T)

df.index = list('abc')
# print(df)

# print(df['name'])
# print(type(df['name']))

# print(df[['name','children']])

# df.rename(columns={'name':'이름'}, inplace=True)
# print(df)

# df.rename({'name':'름름'}, axis=1, inplace=True)
# print(df)


print(df[['name','age']])
df.rename(columns={'name':'이름'},inplace=True)
print(df)