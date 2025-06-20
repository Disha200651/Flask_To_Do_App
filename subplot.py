import pandas as pd
df1=pd.DataFrame({
    "city":["nw","US","SA","india"],
    "temp":[21,12,22,28]
})
print(df1)
df2=pd.DataFrame({
    "city":["US","nw","japan","hubli"],
    "humidity":[65,68,75,80]
})
print(df2)
df3=pd.merge(df1,df2,on="city")
print(df3)
df4=pd.merge(df1,df2,on="city",how="outer")
print(df4)