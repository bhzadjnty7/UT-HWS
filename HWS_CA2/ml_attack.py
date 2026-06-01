import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#Load the previously saved CRPs 
challenges = np.loadtxt("challenges.csv", delimiter=",", dtype=int)
responses = np.loadtxt("responses.csv", delimiter=",", dtype=int)
#Split data: 70% training, 30% testing .
X_train, X_test, y_train, y_test = train_test_split(challenges, responses, test_size=0.3, 
random_state=42)
#Train a logistic regression model .
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
#Predict on test set and evaluate accuracy .
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Machine Learning Attack Accuracy:", accuracy)