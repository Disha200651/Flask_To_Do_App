import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
Shravan_marks=[27,28,26,30,25,26,20,25,24,30]
Ira_mark=[25,27,25,15,24,30,21,30,23,30]
plt.plot(x,Shravan_marks,label="Shravan_marks",color="red",marker="*")
plt.plot(x,Ira_mark,label="Ira_marks",color="green",marker="*")
plt.legend()
plt.xticks(x)
plt.show()