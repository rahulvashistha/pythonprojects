from datetime import datetime
from playsound import playsound
#Print current time
print("Current Time: ", datetime.now())
#Validation Function
def validate_time(alarm_time):
    if len(alarm_time) != 11:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 12:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:5]) > 59:
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            return "Invalid SECOND format! Please try again..."
        else:
            return "ok"
while True:
#Take input and validate it
    alarm_time = input("Enter Alarm Time: 'HH:MM:SS AM/PM' \n")

    validate = validate_time(alarm_time)
    if validate != "ok":
        print(validate)
    else:
        print("Setting up Alarm...")    
        break 

#Slice and assign the input string
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()

while True:
#Assign the current time values
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_second = now.strftime("%S")
    current_period = now.strftime("%p")   
#Check the current and alarm time
    if(alarm_period == current_period):
        if(alarm_hour == current_hour):
            if(alarm_minute == current_minute):
                if(alarm_second == current_second):
#Display msg and play sound
                    print("Wake Up!")
                    playsound('aud1.mp3')
                    break