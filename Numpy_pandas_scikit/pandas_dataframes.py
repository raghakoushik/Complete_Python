import pandas as pd
import numpy as np
# creating empty dataframe
df = pd.DataFrame()
print(df)


#creating data frames from lists

content = list(range(0,8))
da_fr = pd.DataFrame(content)
print(da_fr)

contents = [[0,'sun'], [1,'mon'], [2, 'tues'], [3, 'wed'], [4, 'thur'], [5, 'fri'], [6, 'sat']]
dat_fra = pd.DataFrame(contents, columns=['Numbers', 'Day of Week'])
print(dat_fra)

#creating data frames from dictionary

data = [{'a' : 1, 'b' : 2}, {'a' : 5, 'b' : 10, 'c': 20}, {'a' : 10, 'b' : 20, 'c': 30}]
data_fram = pd.DataFrame(data)
print(data_fram)


#screating data frame from series

my_series = pd.Series({"Unitred Kingdom" : "London", "India" : "New Delhi", "United States" : "Washington", "Belgium": "Brussels"})
data_frame = pd.DataFrame(my_series)
print(data_frame)

#dimension of data frames
ds = pd.DataFrame(np.array([[1,2,3], [4,5,6]]))
print(ds.shape)

#len function gives height of data frame

print(len(ds.index))