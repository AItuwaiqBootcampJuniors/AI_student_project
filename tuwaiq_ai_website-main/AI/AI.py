import sys
from joblib import load
import pandas as pd


#تعديل عبدالله اليحيى
model = load('logistic_regression_model.joblib')

feature_names = ['gender', 'age','ever_married', 'avg_glucose_level', 'bmi']

data = [int(sys.argv[1]),float(sys.argv[2]),int(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5])]

user_data_df = pd.DataFrame([data], columns=feature_names)
    
# استخدام النموذج للتنبؤ
predn = model.predict(user_data_df)
print(1 if predn[0] == 1 else 0)
