import pandas

# read data
pandas.set_option('display.max_rows',None)
pandas.set_option('display.max_columns',None)
data = pandas.read_csv('BeijingPM20100101_20151231.csv')

# select 2015 into 2015.csv
data_2015 = data[data['year']==2015]
data_2015.to_csv('2015_tmp.csv', index=None)

# select null record
data_2015 = pandas.read_csv('2015_tmp.csv')
print(data_2015.isnull().sum())

# solve null
new_data=data_2015.dropna(subset=['Iws']).fillna(method='pad', axis=0)
new_data.to_csv('2015.csv', index=None)
print(new_data.isnull().sum())