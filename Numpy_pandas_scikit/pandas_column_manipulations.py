import pandas as pd
d ={'one' : pd.Series([1,2,3], index = ['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3, 4], index = ['a','b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df['one'])


d1 ={'one' : pd.Series([1,2,3], index = ['a', 'b', 'c']),
    'two' : pd.Series([1, 2, 3, 4], index = ['a','b', 'c', 'd'])}

df1 = pd.DataFrame(d1)
print("Adding a new column by passing as Series:")
df1['three'] = pd.Series([10, 20, 30], index= ['a', 'b', 'c' ])
print(df1)


#deleting
print("Deleting the first column using DEL function:")
del df1['one']
print(df1)
df1.pop('two')
print(df1)

#New rows can also be added. The append function is used to add rows to a DataFrame.
df2 = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df3 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df4 = pd.concat([df2, df3])
print(df4)


#drop functin using label to drop
df5 = df4.drop(0)
print(df5)