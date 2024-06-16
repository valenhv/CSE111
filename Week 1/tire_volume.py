# Student: Valentina Hernandez Vera
# EXCEEDING REQUIREMENTS: Using if-elif-else statements, I added the possibility for the user to share their phone number or email address so he or she can be notified of the results of this program's survey. Said information is stored in volumes.txt

import math
from datetime import datetime

def volume_calc(w, a, d):
    v = (math.pi * pow(float(w),2) * float(a) * (float(w) * float(a) + 2540 * float(d))) / 10000000000
    return v

print("Welcome to the Car Tire Survey! We are collecting information from our customers so we can improve our products.")
print("Please, enter the values of a tire you would like to buy:")
print("Enter the width of the tire in mm (ex 205)")
w = input(">>")
print("Enter the aspect ratio of the tire (ex 60)")
a = input(">>")
print("Enter the diameter of the tire in inches (ex 15)")
d = input(">>")

v = volume_calc(w,a,d)

print(f"The approximate volume is {v:.2f} liters.")
print("What is the price, in American dollars, that you would be willing to pay for this tire?")
print("Please enter a value using numbers.")
price = input(">>")

ans_yes = ["Y", "YES"]
ans_no = ["N", "NO"]
phone_num = "N/A"
email_address = "N/A"

print("Would you like to know about the results of this survey? This includes if your tire was accepted and commercialized.")
print("Please answer with 'yes' or 'no' (or alternatively, 'y' or 'n').")
ans = input(">>")
if ans.upper() in ans_yes:
    print("Please select to which one of these options we should let you know about the results:")
    print("Type A for PHONE NUMBER")
    print("Type B for E-MAIL")
    choice = input(">>")
    if choice.upper() == "A":
        print("Please enter your phone number. Include your national code. Example: +54 11 50 1234:")
        phone_num = input(">>")
    elif choice.upper() == "B":
        print("Please enter your e-mail address. Example: name@mailservice.com")
        email_address = input(">>")
    else:
        print("Invalid input. Please try again.")
elif ans.upper() in ans_no:
    print("Understood. You will not be personally notified of any results.")
else:
    print("Invalid input. Please try again.")

print("We have added this information in our system. Our employees will revise it. Thank you for participating!")

current_date_and_time = datetime.now()
with open("Week 1/volumes.txt", mode="at") as volumes_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {w}, {a}, {d}, {v:.2f}, U$D{float(price):.2f}, {phone_num}, {email_address}", file=volumes_file)