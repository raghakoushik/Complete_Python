import pandas as pd
import numpy as np

data_frame = pd.DataFrame(np.random.randn(5, 3), index = ['a', 'c', 'e', 'f', 'h'], columns = ['one', 'two', 'three'])

data_frame = data_frame.reindex(['a', 'b', 'c', 'd', 'e', 'f','g', 'h'])

print(data_frame.fillna(method='pad'))

data_frame1 = pd.DataFrame(np.random.randn(5, 3), index = ['a', 'c', 'e', 'f', 'h'], columns = ['one', 'two', 'three'])

data_frame1 = data_frame.reindex(['a', 'b', 'c', 'd','i', 'e', 'f','g', 'h'])
print(data_frame1)

print(data_frame1.fillna(method='backfill'))