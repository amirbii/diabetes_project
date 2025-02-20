import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
import pandas as pd

diabetes = load_diabetes()
df = pd.DataFrame(data=diabetes.data, columns=diabetes.feature_names)

df['target'] = diabetes.target


y = df['target']
x = df[['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']]



x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, shuffle=True)

model = LinearRegression()

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

Rmse = root_mean_squared_error(y_test, y_pred)

print(Rmse)

plt.scatter(range(len(y_test)), y_test, color="b", label="Test Data")
plt.plot(range(len(y_pred)), y_pred, color="red", label="Predicted Data")
plt.legend()
plt.show()

print(model.intercept_, model.coef_)
