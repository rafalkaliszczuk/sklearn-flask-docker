# Import dependencies
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
import pickle

# Load the dataset in a dataframe object and include only four features as mentioned
iris=load_iris()
df = pd.DataFrame(data = np.c_[iris['data'], iris['target']], 
                  columns=iris['feature_names']+['target'])

#Define Perceptron class

class Perceptron:
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,y):
                update=self.eta*(target-self.predict(xi))
                self.w_[1:] += update *xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
    
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]
    
    def predict(self, X):
        return np.where(self.net_input(X) >= 0, 1, -1)

# Perceptron classifier

X = iris['data']
y = iris['target']
perceptron_model = Perceptron()
perceptron_model.fit(X, y)

# Save your model
pickle.dump(perceptron_model, 'model.pkl')

perceptron_file = open('SVMModel.pckl', 'wb')
pickle.dump(perceptron_model, perceptron_file)
perceptron_file.close()

# Load the model that you just saved
lr = joblib.load('model.pkl')

