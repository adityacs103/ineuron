import pandas as pd
import numpy as np
import os

import mlflow 
import mlflow.sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import ElasticNet
from sklearn.metrics import accuracy_score,mean_squared_error,mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
import argparse
import warnings
warnings.filterwarnings('ignore')

#fucntion for geting data from uci
def get_data():
    url="https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    #reading the data ad df file
    try:
        df=pd.read_csv(url,sep=";")
        return df
    except Exception as e:
        raise e

def evaluate(y_test,pred):
    # mae=mean_absolute_error(y_test,pred)
    # mse=mean_squared_error(y_test,pred)
    # rmse=np.sqrt(mean_squared_error(y_test,pred))
    # r2=r2_score(y_test,pred)
    # return mae,mse,rmse,r2

    accuracy=accuracy_score(y_test,pred)
    return accuracy


def main(n_estimators,max_depth):
    df = get_data()
    train,test=train_test_split(df)
    #train test split of the raw data
    x_train=train.drop(columns=['quality'])
    x_test=test.drop(columns=["quality"])
    y_train=train["quality"]
    y_test=test["quality"]
    #model traning 
    # lr=ElasticNet()
    # lr.fit(x_train,y_train)
    # pred=lr.predict(x_test)

    rf=RandomForestClassifier(n_estimators=n_estimators,max_depth=max_depth)
    rf.fit(x_train,y_train)
    pred=rf.predict(x_test)

    #evaluate the model
    accuracy=evaluate(y_test,pred)
    #print the model accuracy
    print(f"model accuracy= {accuracy}")


if __name__ == "__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--n_estimator","-n",default=50,type=int)
    args.add_argument("--max_depth","-m",default=5,type=int)
    parse_args=args.parse_args()
    try:
        main(n_estimators=parse_args.n_estimators,max_depth=parse_args.max_depth)
    except Exception as e:
        raise e 

