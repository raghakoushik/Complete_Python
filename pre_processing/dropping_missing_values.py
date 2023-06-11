import pandas as pd
import numpy as np

data_frame = pd.DataFrame(np.random.randn(5, 3), index = ['a', 'c', 'e', 'f', 'h'], columns = ['one', 'two', 'three'])

data_frame = data_frame.reindex(['a', 'b', 'c', 'd', 'e', 'f','g', 'h'])

print(data_frame.dropna()) #default axis = 0 drops rows containing nan


data_frame1 = pd.DataFrame(np.random.randn(5, 3), index = ['a', 'c', 'e', 'f', 'h'], columns = ['one', 'two', 'three'])

data_frame1 = data_frame.reindex(['a', 'b', 'c', 'd', 'e', 'f','g', 'h'])

print(data_frame1.dropna(axis=0)) # drops columns containing nan


#replace function

df1 = pd.DataFrame({'one' : [10, 20, 30,40,50,2000]\
                   , 'two' : [1000,0,30,40,50,60] })
print(df1.replace({1000:10, 2000 :20}))