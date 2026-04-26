import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# load dataset
data = pd.read_csv("rocket_data.csv")

# features TArget
X = data[["mass", "thrust", "burn_time"]]
y = data["max_height"]

# train model
model = RandomForestRegressor()
model.fit(X, y)

# predictions
predictions = model.predict(X)

# evaluate error
error = mean_absolute_error(y, predictions)
print("Average error:", error)

# feature importance
print("Feature importance:", model.feature_importances_)

# plot results
plt.scatter(y, predictions)
plt.xlabel("Actual Height")
plt.ylabel("Predicted Height")
plt.title("Actual vs Predicted")
plt.show()

mass = float(input("Mass: "))
thrust = float(input("Thrust: "))
burn_time = float(input("Burn time: "))

pred = model.predict([[mass, thrust, burn_time]])
print("Predicted height:", pred[0])