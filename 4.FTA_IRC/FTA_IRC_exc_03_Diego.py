from sklearn import metrics
from sklearn.datasets import load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split


cancer = load_breast_cancer()

x = cancer.data
print(x)

y = cancer.target
print(y)

print(cancer.data.shape)

print(cancer.target.shape)

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(x, y)

a = [
    1.799e01,
    1.038e01,
    1.228e02,
    2.654e-01,
    4.601e-01,
    1.189e-01,
    2.057e01,
    1.777e01,
    1.329e02,
    1.860e-01,
    2.750e-01,
    8.902e-02,
    1.969e01,
    2.125e01,
    1.300e02,
    2.430e-01,
    3.613e-01,
    8.758e-02,
    1.660e01,
    2.808e01,
    1.083e02,
    1.418e-01,
    2.218e-01,
    7.820e-02,
    2.060e01,
    2.933e01,
    1.401e02,
    2.650e-01,
    4.087e-01,
    1.240e-01,
]


species = knn.predict([a])[0]
print(cancer.target_names[species])

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

knn.fit(x_train, y_train)
predictions = knn.predict(x_test)

hits = metrics.accuracy_score(y_test, predictions)
print(hits)

# from sklearn.datasets import load_breast_cancer
# cancer = load_breast_cancer()

# x = cancer.data
# print(x)

# y = cancer.target
# print(y)

# print(cancer.data.shape)

# print(cancer.target.shape)

# from sklearn.linear_model import LogisticRegression
# reg=LogisticRegression(penalty='l1',solver='liblinear',random_state=16,tol=0.01)
# reg.fit(x,y)

# reg.fit(x,y)

# a=[1.799e+01, 1.038e+01, 1.228e+02, 2.654e-01, 4.601e-01,
#         1.189e-01,
#        2.057e+01, 1.777e+01, 1.329e+02, 1.860e-01, 2.750e-01,
#         8.902e-02,
#        1.969e+01, 2.125e+01, 1.300e+02, 2.430e-01, 3.613e-01,
#         8.758e-02,
#        1.660e+01, 2.808e+01, 1.083e+02, 1.418e-01, 2.218e-01,
#         7.820e-02,
#        2.060e+01, 2.933e+01, 1.401e+02, 2.650e-01, 4.087e-01,
#         1.240e-01,
# ]

# species = reg.predict([a])[0]
# print(iris.target_names[species])

# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.30)

# reg.fit(x_train, y_train)
# predictions = reg.predict(x_test)

# from sklearn import metrics
# hits = metrics.accuracy_score(y_test, predictions)
# print(hits)
