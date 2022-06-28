def category(BMI):
    if BMI <= 18.4:
        return "Underweight"
    if 18.5 <= BMI <= 24.9: 
        return "Normal Weight"
    if 25 <= BMI <= 29.9:
        return "Overweigth Moderately"
    if 30 <= BMI <= 34.9:
        return "Obese"
    if 35 <= BMI <= 39.9:
        return "Severely Obese"
    if BMI > 40.0:
        return "Very Severely Obese"

def risk(BMI):
    if BMI <= 18.4:
        return "Malnutrition Risk"
    if 18.5 <= BMI <= 24.9: 
        return "Low Risk"
    if 25 <= BMI <= 29.9:
        return "Enhanced Risk"
    if 30 <= BMI <= 34.9:
        return "Medium Risk"
    if 35 <= BMI <= 39.9:
        return "High Risk"
    if BMI > 40.0:
        return "Very high Risk"

def risk_analysis(l):
    for i in l:
        w = i['Weight']
        h_m = i['HeightCM'] / 100
        BMI = round(w/h_m**2,2)
        rsk = risk(BMI)
        cat = category(BMI)
        i['BMI'] = BMI
        i['Category'] = cat
        i['Health Risk'] = rsk

no_of_users = int(input("Please input no of users: "))
l = []
try:
    for i in range(no_of_users):
        data = {}
        gender = input("Please Enter Gender: ")
        heightCM = int(input("Please Enter height in CMs: "))
        weight = int(input("Please Enter weight in KGs: "))
        data['Gender'],data['HeightCM'],data['Weight'] = gender,heightCM,weight
        l.append(data)
        print('------------------------------------------------------------------------------')
except:
    print("Please enter valid details of user")

risk_analysis(l)
