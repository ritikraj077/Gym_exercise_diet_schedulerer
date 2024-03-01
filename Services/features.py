
def cal_bmi(Weight, Height):
    # Convert height to meters
    height_meters = float(Height) / 100
    
    # Convert weight to kilograms
    weight_kg = float(Weight)
    
    # Calculate BMI
    if height_meters > 0:
        bmi = round((weight_kg / (height_meters ** 2)), 2)
        ##checking the bmi values and giving the masage 
        if bmi < 18.5:
            return f" Bmi is : {str(bmi)} you are Underweight"
        elif bmi >= 18.5 and bmi < 25:
            return f"Bmi is: {str(bmi)} Normal weight"
        elif bmi >= 25 and bmi < 30:
            return f" Bmi is : {str(bmi)} You are Overweight need to Workout"
        else:
            return f"Bmi is {str(bmi)} you are Obese you should losse some weight"

    else:
        return "Invalid Height and Weight"