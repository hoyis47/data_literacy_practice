import numpy as np
import pandas as pd
# from teddynote import dataset

# dataset.download('서울시대중교통')
#dataset.download('서울시주민등록인구')


# excel = pd.read_excel('data/seoul_transportation.xlsx', sheet_name='철도', engine='openpyxl')
# print(excel.head())

# print(type(excel))

excel = pd.read_excel('data/seoul_transportation.xlsx', sheet_name='버스', engine='openpyxl')
# print(excel)

# print(excel[list(excel.keys())[0]])
# print(excel[excel.keys()])

# excel.to_excel('data/sample.xlsx',index=False,sheet_name='샘플')
# write = pd.ExcelWriter('sample2.xlsx')
# excel.to_excel(write, index=False, sheet_name='샘플1')
# excel.to_excel(write, index=False, sheet_name='샘플2')
# excel.to_excel(write, index=False, sheet_name='샘플3')
# write.close()

df = pd.read_csv('data/seoul_population.csv')
# print(df.head())

# df.to_csv('data/sample.csv', index=False)
# excel.to_csv('sample.csv', index=False)

sample = pd.read_excel('data/file_sample.xlsx', sheet_name=None)
print(sample.keys())

sample_202010 = pd.read_excel('data/file_sample.xlsx', sheet_name='2020년 10월')
# print(sample_202010)

sample_202010.to_csv('2020-10-oil-price.csv', index=False)

sample_csv = pd.read_csv('2020-10-oil-price.csv', chunksize=5)

for sam in sample_csv:
    print(sam)



