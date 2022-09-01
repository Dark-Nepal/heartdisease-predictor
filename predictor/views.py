from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from .forms import HeartDiseaseForm



def heart(request):

    """ 
    17:29:46 31 Aug, 2022 by Deepesh Mahato
    Reading the training data set.

    """

    # importing csv data into a Pandas DataFrame

    heart_data = pd.read_csv('static/heart.csv')

    # the first 5 rows of the dataset should be printed
    heart_data.head()

    #  last 5 rows of the dataset
    heart_data.tail()

    # number of rows and columns in the dataset
    heart_data.shape

    # getting some info about the data
    heart_data.info()

    # checking for missing values
    heart_data.isnull().sum()

    # statistical measures about the data
    #heart_data.describe()

    # checking the distribution of Target Variable
    heart_data['target'].value_counts()

    X = heart_data.drop(columns='target', axis=1)
    Y = heart_data['target']


    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

    model = LogisticRegression()

    # training the LogisticRegression model with Training data
    model.fit(X_train, Y_train)

    # accuracy on training data
    X_train_prediction = model.predict(X_train)
    training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

    # accuracy on test data
    X_test_prediction = model.predict(X_test)
    test_data_accuracy = accuracy_score(X_test_prediction, Y_test)


    """ 
    17:45:26 31 Aug, 2019 by Deepesh Mahato
    Reading data from the user. 
    """

    value = ''

    if request.method == 'POST':

        age = float(request.POST['age'])
        sex = float(request.POST['sex'])
        cp = float(request.POST['cp'])
        trestbps = float(request.POST['trestbps'])
        chol = float(request.POST['chol'])
        fbs = float(request.POST['fbs'])
        restecg = float(request.POST['restecg'])
        thalach = float(request.POST['thalach'])
        exang = float(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = float(request.POST['slope'])
        ca = float(request.POST['ca'])
        thal = float(request.POST['thal'])

        user_data = np.array(
            (age,
             sex,
             cp,
             trestbps,
             chol,
             fbs,
             restecg,
             thalach,
             exang,
             oldpeak,
             slope,
             ca,
             thal)
        ).reshape(1, 13)

        prediction = model.predict(user_data)
    
        
        if int(prediction[0]) == 0:
          value = 'donot have '
        else:
          value = 'have'
    
    
    form = HeartDiseaseForm()


    return render(request , 'heart.html' , {
        'context':value,
        'form':form,
    })
