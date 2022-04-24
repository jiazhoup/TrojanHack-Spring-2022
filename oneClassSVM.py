
import os
from os import walk
import sys
import pandas as pd
import numpy as np
from sklearn.svm import OneClassSVM
from sklearn.preprocessing import StandardScaler, OneHotEncoder


"""
One Class
"""
def machineLearning(dir, file):
    fileNames = os.listdir(dir)
    features = ['st_mode', 'st_ino', 'st_dev', 'st_nlink', 'st_uid',
                'st_gid', 'st_size', 'st_atime', 'st_mtime', 'st_ctime']
    os.chdir(dir)

    statuses = []
    df_temp = []
    i = 0
    for f in fileNames:
         statuses.append(list(os.stat(f)))
         df_temp.append(pd.DataFrame([statuses[i]]))
         i += 1

    df_f = pd.concat(df_temp, ignore_index=True)
    df_f.columns = features  # set column names


    data = {'fName': fileNames}
    df = pd.DataFrame(data)
    df = pd.concat([df, df_f], axis=1, join='inner')

    pd.set_option('display.width', None)
    X = df.drop(['fName', 'st_ino', 'st_dev'], axis=1)

    norm = StandardScaler()
    X.iloc[:, 3:] = pd.DataFrame(norm.fit_transform(X.iloc[:, 3:]), columns=X.iloc[:, 3:].columns)

    OH_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
    OH_cols = pd.DataFrame(OH_encoder.fit_transform(X['st_mode'].values.reshape(-1, 1)))
    num_X = X.drop('st_mode', axis=1)
    OH_X = pd.concat([num_X, OH_cols], axis=1)

<<<<<<< HEAD
    model = OneClassSVM()
    model.fit(OH_X)

    pred_l = list(os.stat(file))
    df_pred = pd.DataFrame(pred_l)

    pred = model.predict(df_pred)
    return pred
=======
model = OneClassSVM()
model.fit(OH_X)

model.predict
>>>>>>> 22424c28425799ab77713f0fd004a41eb6b2fc1e
