#Function to take height and its unit and convert it into meter stand.
def convert_H():
    H_unit = int(input("Height: Select your Unit\n 1. centimeter   2. meter 3. feet \n"))
    Height = float(input("Enter you Height: \n"))
    if (H_unit == 1):
        return (Height/100)
    elif (H_unit == 2):
        return Height
    elif (H_unit == 3):
        return (round(Height/3.2808399,3))
    else: print("Wrong Input...")
#Call func for Height
Height = convert_H()
#Function to take weight and its unit and convert it into kg stand.
def convert_W():
    W_unit = int(input("Weight: Select your Unit\n 1. kilograms   2. pounds/lbs \n"))
    Weight = float(input("Enter you Weight: \n"))
    if (W_unit == 1):
        return Weight
    elif (W_unit == 2):
        return (round(Weight/2.20462262,3))
    else: print("Wrong Input...")
#Call func for Weight
Weight = convert_W()
#Calc BMI and print
BMI = Weight/(Height * Height)
print("Your Body Mass Index is: ", BMI)
#print condition acc to BMI
if(BMI>0):
    if(BMI<=16):
        print("You're Severely Underweight")
    elif(BMI<=18.5):
        print("You're Underweight")
    elif(BMI<=25):
        print("You're Healthy")
    elif(BMI<=30):
        print("You're Overweight")
    else:
        print("You're Severely Overweight")
else:
    print("Enter Valid Details")