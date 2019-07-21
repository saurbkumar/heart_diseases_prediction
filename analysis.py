import pandas as pd
import numpy as np
from featexp import get_univariate_plots
from sklearn.model_selection import train_test_split
trainDataInput = pd.read_csv('train_values.csv')
trainDataOutput = pd.read_csv('train_labels.csv')


data = pd.concat([trainDataInput, trainDataOutput['heart_disease_present']], axis=1, join='inner')
train=data.sample(frac=0.8,random_state=200)
test=data.drop(train.index)
#get_univariate_plots(data=data, target_col='heart_disease_present')

# relation
get_univariate_plots(data=train, target_col='heart_disease_present', data_test=test,
                     features_list=['slope_of_peak_exercise_st_segment'])
trainDataInput.info()
trainDataInput.describe()

import matplotlib.pyplot as plt
import seaborn as sns

