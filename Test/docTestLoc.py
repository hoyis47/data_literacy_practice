import pandas as pd

df = pd.DataFrame([[1,2], [4,5], [7,8]],
                  index = ['cobra','viper','sidewinder'],
                  columns=['max_speed','shield'])

print(df)

print(df.loc[['viper','sidewinder'],['max_speed']])
print(df.loc['cobra','shield'])
print(df.loc['cobra':'viper','max_speed'])
print(df.loc[[True,True,False]])

print(df.loc[df['shield'] > 6, ['max_speed']])
print(df.loc[lambda df:df['shield']==8])

df.loc[['viper','sidewinder'],['shield']] = 50
print(df)

df.loc['cobra'] = 10
print(df)

df.loc[:,'max_speed'] = 30
print(df)

df.loc[df['shield'] > 35] = 0
print(df)

