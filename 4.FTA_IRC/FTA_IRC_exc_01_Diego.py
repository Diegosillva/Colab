from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()
knn = KNeighborsClassifier(n_neighbors=5)

x = iris.data
print(x)

y = iris.target
print(y)

knn.fit(x, y)
a = [5.4, 3.4, 1.5, 0.4]
b = [5.8, 2.7, 5.1, 1.9]
c = [4.4, 2.9, 1.4, 0.2]
d = [6.9, 3.1, 5.1, 2.3]

especies_A = knn.predict([a])[0]
especies_B = knn.predict([b])[0]
especies_C = knn.predict([c])[0]
especies_D = knn.predict([d])[0]

print(iris.target_names[especies_A])
# print(iris.target_names[especies_B])
# print(iris.target_names[especies_C])
# print(iris.target_names[especies_D])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

knn.fit(x_train, y_train)
predictions = knn.predict(x_test)

hits = metrics.accuracy_score(y_test, predictions)
print(hits)

# print(iris.data.shape)
# print(iris.target.shape)
