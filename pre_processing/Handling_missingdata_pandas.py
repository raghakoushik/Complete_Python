import pandas as pd
import numpy as np

data_frame = pd.DataFrame(np.random.randn(5, 3), index = ['a', 'c', 'e', 'f', 'h'], columns = ['one', 'two', 'three'])

print(data_frame)

data_frame = data_frame.reindex(['a', 'b', 'c', 'd', 'e', 'f','g', 'h'])

print(data_frame)


#check null with isnull() and notnull()

print(data_frame['one'].isnull())


print(data_frame['one'].notnull())


#calculating sum values of column

print(data_frame['one'].sum())