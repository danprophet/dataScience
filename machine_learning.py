"This file will handle the machine learning part of the projectimport pandas as pd"
"""
Question: מתי במהלך היום יש את הכמות הגדולה ביותר של תאונות, וכך נוכל להזהיר נהגים.
Q: באיזה חודשים יש את כמות התאונות הגדולה ביותר
Q: השאלה המרכזית: בעקבות הנתונים שקיבלנו, נוציא אזהרה לנהגים 
לשלב את זה בWAZE וברגע שמזהים שעה בעייתית להזהיר את הנהג
"""
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.model_selection import train_test_split as tts
from sklearn import metrics


