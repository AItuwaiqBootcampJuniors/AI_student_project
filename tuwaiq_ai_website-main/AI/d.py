from joblib import load
import pandas as pd

# تحميل النموذج
model = load('logistic_regression_model.joblib')

hospital_customer = False
feature_names = ['gender', 'age', 'ever_married', 'avg_glucose_level', 'bmi']  # تأكد من أن هذه هي أسماء الميزات الصحيحة
while not hospital_customer:
    # جمع بيانات المستخدم
    data = []
    for feature in feature_names:
        data.append(float(input(f"Enter your {feature}: ")) if feature != 'gender' and feature != 'ever_married' 
                    else int(input(f"Enter your {feature} (1 for yes, 0 for no): ")))

    # إنشاء DataFrame مع أسماء الأعمدة
    user_data_df = pd.DataFrame([data], columns=feature_names)
    
    # استخدام النموذج للتنبؤ
    predn = model.predict(user_data_df)
    print("Risk of stroke: ", "High" if predn[0] == 1 else "Low")
    print(predn[0])

    hospital_customer_input = input("Do you want to continue [y/n]: ").lower()
    hospital_customer = (hospital_customer_input == 'n')
