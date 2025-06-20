import matplotlib.pyplot as plt
age1=[1,3,5,10,13,19,15,16,19,21]
age2=[1,23,5,7,9,20,11,13,15,17,19]
plt.hist(age1,label="Age_Group1",color="violet",alpha=0.7,bins=4,edgecolor="black")
plt.hist(age2,label="Age_group2",color="red",alpha=0.5,bins=4,edgecolor="black")
plt.legend()
plt.show()