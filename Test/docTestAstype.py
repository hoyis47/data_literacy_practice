import pandas as pd

d = {'col1':[1,2], 'col2':[3,4]}
df = pd.DataFrame(data=d)
print(df.dtypes)

print(df.astype('int32').dtypes)

print(df.astype({'col1': 'int32'}).dtypes)

ser = pd.Series([1,2], dtype='int32')
print(ser)

print(ser.astype('int64'))

print(ser.astype('category'))

from pandas.api.types import CategoricalDtype
cat_dtype = CategoricalDtype(
    categories=[2,1],ordered=True
)

print(ser.astype(cat_dtype))

ser_date = pd.Series(pd.date_range('20230706', periods=3))
print(ser_date)