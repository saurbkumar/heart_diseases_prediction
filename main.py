import pandas as pd
import numpy as np

trainDataInput = pd.read_csv('train_values.csv')
trainDataOutput = pd.read_csv('train_labels.csv')

trainDataInput.info()
trainDataInput.describe()

import matplotlib.pyplot as plt
import seaborn as sns
# Histogram plot for features (not going to be as helpful)
trainDataInput.plot(kind='hist',subplots=True, layout=(4,3), figsize=(15,15),sharex=False,alpha=.5,grid = True,
                 title="Histogram Plot for Patient features")
plt.show()

fig, axes = plt.subplots(nrows=4, ncols=3,figsize=(15,15))

#plot 1
trainDataInput['slope_of_peak_exercise_st_segment'].hist(ax=axes[0, 0],alpha=.5);
axes[0, 0].set_title('slope_of_peak_exercise_st_segment')
#axes[0, 0].set_xlabel('slope_of_peak_exercise_st_segment')
#axes[0, 0].set_ylabel('slope_of_peak_exercise_st_segment')

#plot 2
trainDataInput['thal'].value_counts().plot(ax=axes[0,1], kind='bar',alpha=.5);
axes[0, 1].set_title('thallium stress test')
axes[1, 2].tick_params(axis='x', rotation=45)
axes[0, 1].set_ylabel('patient count')
axes[0, 1].grid()

#plot 3
trainDataInput['resting_blood_pressure'].plot(ax=axes[0,2], kind='hist',bins=40,color='#58508d');
axes[0, 2].set_title('resting_blood_pressure')
axes[0, 2].set_ylabel('patient count')
axes[0, 2].grid()

#plot 4
trainDataInput['chest_pain_type'].value_counts(sort=False).plot(ax=axes[1,0], kind='bar',alpha=.5);
axes[1, 0].set_title('chest_pain_type')
axes[1, 0].set_ylabel('patient count')
axes[1, 0].grid()


#plot 5
trainDataInput['num_major_vessels'].value_counts().plot(ax=axes[1,1], kind='bar',alpha=.5);
axes[1, 1].set_title('num_major_vessels')
axes[1, 1].set_ylabel('patient count')
axes[1, 1].grid()

#plot 6
trainDataInput['fasting_blood_sugar_gt_120_mg_per_dl'].value_counts().plot(ax=axes[1,2], kind='bar',alpha=.5);
axes[1, 2].set_title('fasting blood sugar > 120 mg/dl')
axes[1, 2].set_xticklabels(["<= 120"," >120"])
axes[1, 2].tick_params(axis='x', rotation=-360)
axes[1, 2].set_ylabel('patient count')
axes[1, 2].grid()

#plot 7
trainDataInput['resting_ekg_results'].value_counts(sort=False).plot(ax=axes[2,0], kind='bar',alpha=.5);
axes[2,0].set_title('resting electrocardiographic results')
axes[2,0].set_ylabel('patient count')
axes[2,0].grid()


#plot 8
trainDataInput['serum_cholesterol_mg_per_dl'].plot(ax=axes[2,1], kind='hist',bins=80,color='#ff7c43');
axes[2,1].set_title('serum cholestoral in mg/dl')
axes[2,1].set_ylabel('patient count')
axes[2,1].grid()

# plot 9
trainDataInput['oldpeak_eq_st_depression'].plot(ax=axes[2,2], kind='hist',bins=40,color='#a05195');
axes[2,2].set_title('ST depression induced by exercise relative to rest')
axes[2,2].set_ylabel('patient count')
axes[2,2].grid()

# plot 10
trainDataInput['sex'].value_counts(sort=False).plot(ax=axes[3,0], kind='bar',alpha=.5);
axes[3,0].set_title('Gender')
axes[3,0].set_xticklabels(["female","male"])
axes[3,0].set_ylabel('patient count')
axes[3,0].grid()

# plot 11
trainDataInput['age'].plot(ax=axes[3,1], kind='hist',bins=40,alpha=.5);
axes[3,1].set_title('age')
axes[3,1].set_ylabel('patient count')
axes[3,1].grid()

# plot 12
trainDataInput['max_heart_rate_achieved'].plot(ax=axes[3,2], bins=40,kind='hist',alpha=.5);
axes[3,2].set_title('maximum heart rate achieved')
axes[3,2].set_ylabel('patient count')
axes[3,2].grid()

## plot 13 ,title="exercise-induced chest pain"
#fig1, axes1 = plt.subplots(nrows=1, ncols=1)
plt.figure(0) # Here's the part I need
trainDataInput['exercise_induced_angina'].value_counts(sort=False).plot(title='exercise_induced_angina',kind='bar',alpha=.5);



