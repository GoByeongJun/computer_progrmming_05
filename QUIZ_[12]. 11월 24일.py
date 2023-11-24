import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from pandas.plotting import scatter_matrix  # Added import for scatter_matrix
import matplotlib.pyplot as plt  # Added import for matplotlib.pyplot

filename = "./data/09_irisdata.csv"

column_names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

data = pd.read_csv(filename, names=column_names)

print("데이터 셋의 행렬 크기:", data.shape)

X = data.iloc[:, 0:4].values
Y = data.iloc[:, 4].values

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

print("데이터 셋의 요약:")
print(data.describe())

class_counts = data.groupby('class').size()
print("데이터 셋의 클래스 종류:")
print(class_counts)

scatter_matrix(data)
plt.savefig("./results/scatter_plot.png")

kfold = KFold(n_splits=10)
model = DecisionTreeClassifier()
results = cross_val_score(model, X_scaled, Y, cv=kfold, scoring='accuracy')

print("K-fold의 평균 정확도:", results.mean())