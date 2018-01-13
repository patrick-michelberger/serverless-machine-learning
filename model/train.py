from sklearn import datasets
from sklearn.ensemble import GradientBoostingClassifier
import pickle

# import data
iris = datasets.load_iris()

X = iris.data[:, :2]  # we only take the first two features.
Y = iris.target

# init model
clf = GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,
                                 max_depth=2, random_state=0)
# fit model
clf.fit(X, Y)

# save model
pickle.dump(clf, open("model.pkl", "wb"))