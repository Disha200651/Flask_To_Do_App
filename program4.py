import matplotlib.pyplot as plt
import numpy as np
Aditya=[90,55,40,65]
Aditi=[85,62,54,20]
x=np.arange(4)
barwidth=0.35
plt.bar(x,Aditya,barwidth,label="Aditya",color="violet")
plt.bar(x+barwidth,Aditi,barwidth,label="Aditi",color="pink")
plt.xticks(x,("DSP","CC","CN","QA"))
plt.xlabel("Subject")
plt.ylabel("Score")
plt.title("Scores in subjects")
plt.legend()
plt.show()
