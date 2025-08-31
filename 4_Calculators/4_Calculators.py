#this script is converting days into units
#new calculators will be added

import time

def banner():
    print("=" * 40)

def countdown():
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)

#-----------------------------------------------------------------------

def uefi():
    banner()
    print("Hello welcome to the multi-calculator program")
    banner()

    while True:
        print("1. death calculator \n2. day calculator \n3. hour calculator \n4. real capacity drives")
        banner()
        print("Which calculator you wanna use? just write the number")
        user_input = input()
        banner()
        if user_input.lower() == "1":
            print(f"{user_input}. death calculator is functional, booting in 3 seconds")
            banner()
            time.sleep(3)
            deathcalculator()

        elif user_input.lower() == "2":
            print(f"{user_input}. day calculator is functional, booting in 3 seconds")
            banner()
            time.sleep(3)
            daycalculator()

        elif user_input.lower() == "3":
            print(f"{user_input}. hour calculator is functional, booting in 3 seconds")
            banner()
            time.sleep(3)
            hour_calculator()

        elif user_input.lower() == "4":
            print(f"{user_input}. real capacity drives is functional, booting in 3 seconds")
            banner()
            time.sleep(3)
            real_scam()

        else:
            print("This program doesn't exist")
            print("Returning to root in 3 seconds")
            banner()
            time.sleep(3)
            uefi()


def daycalculator(): #converts days into months/weeks/days/hours/minutes/seconds
        try:
            dayspmonth = 30.4167
            hourspday = 24
            dayspweek = 7
            secondspminute = 60
            minutespday = secondspminute * hourspday
            secondspday = secondspminute * secondspminute * hourspday

            banner()
            days_input = input ("How many days do you wanna calculate? ")
            banner()
            days = float(days_input)
            if days < 1:
                print("Value is too low!")
                banner()
            elif days >= 1:
                print(f"You have picked {days} days")
                print("Let's break it down")
                print(f"{days} days = {days / dayspmonth} months")
                print(f"{days} days = {days / dayspweek} weeks")
                print(f"{days} days = {days * 1} days")
                print(f"{days} days = {days * hourspday} hours")
                print(f"{days} days = {days * minutespday} minutes")
                print(f"{days} days = {days * secondspday} seconds")
                banner()
                user_input = input("Do you wanna calculate again? Y/N: ")
                banner()
                if user_input.lower() == "y":
                    daycalculator()
                elif user_input.lower() == "n":
                    print("booting back to root please standby")
                    banner()
                    time.sleep(3)
                    uefi()
                else:
                    print("Try again?")
                    time.sleep(3)
                    daycalculator()

        except ValueError:
            print("Error, restarting program")
            print("Please try again in 3 seconds")
            banner()
            time.sleep(3)
            uefi()


def deathcalculator(): #calculates time till death
        try:
            #user input
            age_input = input ("Enter your age? ")
            how_old = input("How old do you think you gonna be before you die? ")
            banner()
            age = int(age_input)
            old = int(how_old)

            #local variables death program
            days = 365
            hours = 24
            minutes = 60
            seconds = 60
            months = 12
            weeks = 52
            secondsinday = hours * minutes * seconds
            secondsinyear = secondsinday * days
            hoursinyear = hours * days
            minutesinyear = 60 * 24 * days
            death = old - age
            deathmonths = death * months
            deathweeks = death * weeks
            deathhours = death * hoursinyear
            deathminutes = death * minutesinyear
            deathseconds = death * secondsinyear

            print(f"You are {age} years old and you are expecting to live up to the age of {old}")
            print("That means you got")
            banner()
            print(f"{death} years left")
            print(f"{deathmonths} months left")
            print(f"{deathweeks} weeks left")
            print(f"{deathhours} hours left")
            print(f"{deathminutes} minutes left")
            print(f"{deathseconds} seconds left")
            banner()
            user_input = input ("Do you want to calculate again? Y/N: ")
            banner()
            if user_input.lower() == "y":
                banner()
                print("Rebooting Death Calculator in 3 seconds")
                time.sleep(1)
                print("Rebooting in 3")
                time.sleep(1)
                print("Rebooting in 2")
                time.sleep(1)
                print("Rebooting in 2")
                time.sleep(1)
                print("Rebooting in 1")
                banner()
                time.sleep(1)
                deathcalculator()
            elif user_input.lower() == "n":
                print("booting back to root please standby")
                time.sleep(3)
                uefi()
            else:
                print(f"{user_input} is not a valid answer, aborting program troll")
                banner()
                exit()

        except ValueError:
            print("Must be a number")
            print("Please try again in 3 seconds")
            time.sleep(3)
            deathcalculator()

def hour_calculator(): #converts hours into seconds/minutes/hours/days/weeks/months/years
    try:

        user_input = input("How many hours do you want to calculate? > ")
        hours = float(user_input)
        banner()
        print(f"You picked {hours} hours which converts to.")
        banner()
        year = 24 * 365
        print(f"{hours / year} years")
        month = 365 / 12
        monthh = month * 24
        print(f"{hours / monthh} months")
        week = 24 * 7
        print(f"{hours / week} weeks")
        print(f"{hours * 1} hours")
        minute = 60
        print(f"{hours * minute} minutes")
        second = 60 * 60
        print(f"{hours * second} seconds")
        milsecond = 60 * 1000
        print(f"{hours * milsecond} millisecond")
        banner()
        time.sleep(10)
        user_input = input("Do you want to calculate again? Y/N: ")
        if user_input.lower() == "y":
            hour_calculator()

        elif user_input.lower() == "n":
            uefi()
        else:
            print("Not a valid input!")
            user_input = input("Do you want to calculate again? Y/N: ")
            if user_input.lower() == "y":
                hour_calculator()

            elif user_input.lower() == "n":
                uefi()
            else:
                banner()
                print("You had enough chances to do the right thing you f*cker")
                time.sleep(1)
                banner()
                print("Uploading virus to computer")
                for ctr in range(14):
                    print(" " * ctr + "/ಠ 益 ಠ)ノ")
                    time.sleep(0.1)
                exit()

    except ValueError:
        print("Only numbers are a a valid input")
        banner()
        hour_calculator()

def real_scam():

    discrepancy = None
    banner()
    unit = input(str("Enter TB or GB for the advertised unit: "))

    if unit == 'TB' or unit == 'tb':
        discrepancy = 1000000000000 / 1099511627776
    elif unit == 'GB' or unit == 'gb':
        discrepancy = 1000000000 / 1073741824
    else:
        banner()
        print("Please use your brain and pick the right option")
        print("TB or GB")
        banner()
        real_scam()


    advertised_capacity = input(str("Enter the advertised capacity: "))
    advertised_capacity = float(advertised_capacity)
    real_capacity = str(round(advertised_capacity * discrepancy, 2))

    print(f"The actual capacity is {real_capacity} {unit}")
    banner()
    print("Do you want to calculate again?")
    print("1. Yes")
    print("2. No")
    banner()
    user_input = input("> ").lower()
    if user_input == "1":
        real_scam()
    elif user_input == "2":
        print("Shutting down in 3")
        countdown()
        exit()
    elif user_input == "your mom" or user_input == "your momma" or user_input == "ur mom":
        print(f"Actually, {user_input}, so fat, she wears a watch on both wrists...one for each time zone!")
        time.sleep(1)
        print("Please standby")
        time.sleep(1)

    else:
        banner()
        print("Please try again in menu")
        uefi()

if __name__ == "__main__":
    uefi()