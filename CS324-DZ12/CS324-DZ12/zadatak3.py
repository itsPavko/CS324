import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset.csv')

X_cs_101 = df[['cs_101_ocena']]  
X_cs_115_izostanci = df[['cs_115_izostanci']]  
X_all = df.drop(['cs_115_ocena', 'cs_115_položen'], axis=1) 


y = df['cs_115_položen']

def train_and_evaluate_logistic(X, y, test_size):
   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

 
    model = LogisticRegression()
    model.fit(X_train, y_train)

    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    conf_matrix = confusion_matrix(y_test, y_pred)

    return model, y_test, y_pred, accuracy, conf_matrix

for X in [X_cs_101, X_cs_115_izostanci, X_all]:
    for test_size in [0.25, 0.10]:
        model, y_test, y_pred, accuracy, conf_matrix = train_and_evaluate_logistic(X, y, test_size)
        print(f'Test size: {test_size}, Accuracy: {accuracy}')
        sns.heatmap(conf_matrix, annot=True, fmt='g')
        plt.title(f'Confusion Matrix (Test size: {test_size})')
        plt.xlabel('Predicted')
        plt.ylabel('True')
        plt.show()
