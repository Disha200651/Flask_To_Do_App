import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv("Book1lab.csv")
print(data)
t=data['Temp'].tolist()
sl=data['Slushie'].tolist()
plt.scatter(t,sl)
plt.plot(np.unique(t),np.poly1d(np.polyfit(t,sl,1))(np.unique(t)),color="red")
plt.show()