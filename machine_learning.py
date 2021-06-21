"This file will handle the machine learning part of the projectimport pandas as pd"
"""
Question: מתי במהלך היום יש את הכמות הגדולה ביותר של תאונות, וכך נוכל להזהיר נהגים.
Q: באיזה חודשים יש את כמות התאונות הגדולה ביותר
Q: השאלה המרכזית: בעקבות הנתונים שקיבלנו, נוציא אזהרה לנהגים 
לשלב את זה בWAZE וברגע שמזהים שעה בעייתית להזהיר את הנהג
"""

###Importing Libraries
import pandas as pd
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.model_selection import train_test_split as tts
from sklearn import metrics

###Importing Dataset
iris = datasets.load_iris()

###Constructing Data Frame
a=pd.read_csv('result_after_cleaning.csv')
data = pd.DataFrame(a)
# print(data["species"])

###Splitting train/test data
x=data[['hour']]
y=data["day_week"]
X_tr, X_ts, y_tr, y_ts = tts(x, y, test_size=30/100, random_state=None)

###Creating Decision Tree Classifier Model
DT = DTC()

###Training the Model
DT.fit(X_tr,y_tr)

###Making Predictions
y_pr=DT.predict(X_ts)
print(y_pr)

###Evaluating Prediction Accuracy
print("Acc %:",metrics.accuracy_score(y_ts, y_pr)*100)

###Making Prediction with Foreign Data
print(DT.predict([[1]]))

