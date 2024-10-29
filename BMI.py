def BMI_calculate(weight, hgt):
    bmi =  weight/(hgt**2)
    return bmi
print("enter your weight in kgs and height in meters")
value = float(input("weight in kgs"))
h =  float(input("height in meters"))
result = BMI_calculate(value , h)
if(result<18.5):
    print("you are under weight" , result)
elif ((result<24.9) or (result == 18.5)):
    print("you are normal" , result)
elif(result<=25 or result<29.9):
    print("overweight" , result)
elif(result>=29.9):
    print(f"obese, {result}!")


