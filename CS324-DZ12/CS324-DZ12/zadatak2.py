from pyexpat import model
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')

X_cs_101 = df[['cs_101_ocena']]
X_cs_115_izostanci = df[['cs_115_izostanci']]
X_all = df.drop(['cs_115_ocena', 'cs_115_položen'], axis=1)

y = df['cs_115_ocena'] 


def train_and_evaluate(X, y, test_size):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)


    model = LinearRegression()
    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    accuracy = model.score(X_test, y_test)

    return model, y_test, y_pred, mse, accuracy

for X in [X_cs_101, X_cs_115_izostanci, X_all]:
    for test_size in [0.25, 0.10]:
        model, y_test, y_pred, mse, accuracy = train_and_evaluate(X, y, test_size)
        print(f'Test size: {test_size}, MSE: {mse}, Accuracy: {accuracy}')


        if X.shape[1] == 1:
            plt.scatter(X, y, color='blue')
            plt.plot(X, model.predict(X), color='red')
            plt.title(f'Predviđanja modela vs. Stvarne vrednosti (Test size: {test_size})')
            plt.xlabel(X.columns[0])
            plt.ylabel('cs_115_ocena')
            plt.show()
