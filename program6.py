import matplotlib.pyplot as plt
rollno=[1,2,3,4,5,6,7,8,9,10]
marks=[90,93,97,96,90,87,89,91,92,95]
avgls=[]
for i in marks:
    avg=i/100*100
    avgls.append(avg)
plt.scatter(x=rollno,y=marks,c=avgls,cmap="plasma")
plt.colorbar(label="Percentage",orientation="vertical")
plt.xlabel("Roll number")
plt.ylabel("Marks")

plt.show()