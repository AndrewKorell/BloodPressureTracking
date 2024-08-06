# Blood Pressure Tracking

The purpose here is to create a full stack implementation of a blood pressure tracker. I am aming for Django and Go as two different versions of the back-end.. Maui for mobile, and mostly likely Angular as a web front-end.

We also need the ability to cache data locally. 

# Features 

1. Allow user to create an account.
2. Record DateTime, Systolic Pressure, Diastolic Pressure, Pulse and a Note 
3. Evaluate if the current reading is Normal, Elevated, or State1 or Stage2 of hypertension 
4. Display data in chart and table form 
5. Create a report to share over email 
6. Manage stored data
7. Access data by mobile or webbrowswer
8. Notify User that blood pressure needs to be checked 
9. Ask user to check both arms on first check, and keep as reference 

# Screens 

- Login
- Signup
- Log Blood Pressure
- Show History as Table / Chart

# Setup 

Location of backend. 

# BP Model 

uint8_t Systolic   
uint8_t Diastolic 
uint8_t Pulse 
DateTime DateTime 
vchar(200) Note (I usually use this to say that it was after a big meal, while on vacation, or anything context that might explain a change in pressure)

We're not going to store evaluations of the blood pressure. Those will be calculated in real time.  

# Background 

I will let the Mayo clinic deal with the details. 
https://www.mayoclinic.org/diseases-conditions/high-blood-pressure/in-depth/blood-pressure/art-20050982


