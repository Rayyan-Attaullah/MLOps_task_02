
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib


X = np.array([[500], [1000], [1500], [2000], [2500]])
y = np.array([150000, 300000, 450000, 600000, 750000])


model = LinearRegression()
model.fit(X, y)


joblib.dump(model, 'model.pkl')
 