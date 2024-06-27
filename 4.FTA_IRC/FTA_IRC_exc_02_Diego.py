from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

iris = load_iris()
knn = KNeighborsClassifier(n_neighbors=5)

log = LogisticRegression(penalty="l1", solver="liblinear", random_state=16, tol=0.01)

x = iris.data

y = iris.target
print(y)

log.fit(x, y)
a = [5.4, 3.4, 1.5, 0.4]

especies_A = log.predict([a])[0]

print(iris.target_names[especies_A])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

log.fit(x_train, y_train)
predictions = log.predict(x_test)

hits = metrics.accuracy_score(y_test, predictions)
print(hits)
