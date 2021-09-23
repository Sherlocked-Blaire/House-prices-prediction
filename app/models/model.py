from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.datasets import load_boston
import pickle


data = load_boston()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)
clf = tree.DecisionTreeRegressor()
clf.fit(X_train, y_train)
with open("model.pkl", "wb") as f:
    pickle.dump(clf, f)