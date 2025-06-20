import numpy as np
from sklearn.linear_model import LinearRegression
x=np.array([5,15,25,36]).reshape((-1,1))
y=np.array([5,20,30,38])
model=LinearRegression().fit(x,y)
r_sq=model.score(x,y)
print("Coeff ",r_sq)
print("Intercept:",model.intercept_)
print(f"slope: {model.coef_}")
y_pred=model.predict(x)
print(f"Perdicted response{y_pred}")