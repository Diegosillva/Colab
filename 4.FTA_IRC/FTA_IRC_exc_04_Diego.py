from sklearn import metrics
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression


wine = load_wine()

x = wine.data
# print(x)

y = wine.target
# print(y)

print(wine.data.shape)
print(wine.target.shape)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(x, y)

a = [
    1.166e01,
    1.880e00,
    1.920e00,
    1.600e01,
    9.700e01,
    1.610e00,
    1.570e00,
    3.400e-01,
    1.150e00,
    3.800e00,
    1.230e00,
    2.140e00,
    4.280e02,
]

vinho = knn.predict([a])[0]
print(wine.target_names[vinho])


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

knn.fit(x_train, y_train)
predictions = knn.predict(x_test)

hits = metrics.accuracy_score(y_test, predictions)
print(round(hits, 2))

print("#" * 20)

reg = LogisticRegression(penalty="L2", solver="liblinear", random_state=16, tol=0.01)
reg.fit(x, y)

b = [
    1.166e01,
    1.880e00,
    1.920e00,
    1.600e01,
    9.700e01,
    1.610e00,
    1.570e00,
    3.400e-01,
    1.150e00,
    3.800e00,
    1.230e00,
    2.140e00,
    4.280e02,
]

vinhos = reg.predict([a])[0]
print(wine.target_names[vinhos])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

reg.fit(x_train, y_train)
predictions = reg.predict(x_test)

hits = metrics.accuracy_score(y_test, predictions)
print(round(hits, 2))
