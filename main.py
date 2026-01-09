import pandas as pd
import numpy as np
import math


def user_input ():
    #Heading
    print("===Airline Manager Tycoon===")
    print("--=Seat Configuration=--")
#Airplane Information
    airplane_name = input("Enter your airplane name: ")
    speed = int(input("Input the airplane speed (km/h): "))
#2) Enter max plane's cap
    print("\n--- Seat Capacity ---")
    e_cap = int(input("Enter Max E Capacity: ")) #Input your maximum economy seat
    b_cap = int(input("Enter Max B Capacity: ")) #Input your maximum business seat
    f_cap = int(input("Enter Max F Capacity: ")) #Input your maximum first seat
    max_cap = e_cap

    print("\n--- Route Info ---")
    designated_route = input("Enter your route: ")
    distance = int(input("Input route distance: "))

    #1) Enter route's demand
    print("\n--- Route Demand ---")
    e_dmd = int(input("Enter E demand for this route: "))
    b_dmd = int(input("Enter B demand for this route: "))
    f_dmd = int(input("Enter F demand for this route: "))

    #route ticket price
    print("\n--- Ticket Price ---")
    e_price = int(input("Enter E price for this route ($): "))
    b_price = int(input("Enter B price for this route ($): "))
    f_price = int(input("Enter F price for this route ($): "))

    return {
        "speed": speed, "distance": distance, "e_dmd": e_dmd, "b_dmd": b_dmd, "f_dmd": f_dmd,
        "e_price": e_price, "b_price": b_price, "f_price": f_price,
        "e_cap": e_cap, "b_cap": b_cap, "f_cap":f_cap, "max_cap": max_cap
    }

#3) demand ratio
def dmd_ratio(e_dmd, b_dmd, f_dmd):
    e_rat = e_dmd/e_dmd
    b_rat = b_dmd/e_dmd
    f_rat = f_dmd/e_dmd
    return (e_rat, b_rat, f_rat)

#4)seat weight
def cap_ratio (e_cap, b_cap, f_cap):
    e_weight = e_cap/e_cap
    b_weight = e_cap/b_cap
    f_weight = e_cap/f_cap
    return(e_weight, b_weight, f_weight)

#5) calculate max scale
def max_point(e_rat, b_rat, f_rat, e_weight, b_weight, f_weight, max_cap):
#insert ratio to the formula
    max_rat = (e_rat*e_weight) + (b_rat*b_weight) + (f_rat*f_weight)

    max_scale = max_cap / max_rat
    return (max_rat, max_scale)


#6)calculate seating configuration
def seat (b_rat, f_rat, max_scale, max_cap, b_weight, f_weight,e_dmd, b_dmd, f_dmd):
#calculate b and f
    b_seat = round(b_rat * max_scale,0)
    f_seat = round(f_rat * max_scale,0)

#calculate e seat
    e_seat = math.floor(max_cap - (b_weight * b_seat) - (f_weight * f_seat))

    e_left = e_dmd - (e_seat*2)
    b_left = b_dmd - (b_seat*2)
    f_left = f_dmd - (f_seat*2)

    return (e_seat, b_seat, f_seat, e_left, b_left, f_left)


def frequencies(distance, speed):
 
    flight_time = ((distance / speed) * 2) + 2

    hours = int(flight_time)
    minutes = flight_time % 1

    if minutes <= 0.05: minutes = 0
    elif minutes <= 0.25: minutes = 15
    elif minutes <= 0.5: minutes = 30
    elif minutes <= 0.75: minutes = 45
    else: 
        hours += 1
        minutes +=0

    return_time = f"{hours} h {minutes} m"

    return return_time

#revenue
def revenue (e_seat, b_seat, f_seat, e_price, b_price, f_price):
    
    e_rev_flight = e_seat * e_price
    b_rev_flight = b_seat * b_price
    f_rev_flight = f_seat * f_price

    total_rev_flight = e_rev_flight + b_rev_flight + f_rev_flight

    return total_rev_flight

def main():
#Call all function
    data = user_input()

#plane ratio
    e_rat, b_rat, f_rat = dmd_ratio(data["e_dmd"], data["b_dmd"], data["f_dmd"])
    e_weight, b_weight, f_weight = cap_ratio (data["e_cap"], data["b_cap"], data["f_cap"])
    max_rat, max_scale = max_point(e_rat, b_rat, f_rat, e_weight, b_weight, f_weight, data["max_cap"])

#seating
    e_seat, b_seat, f_seat, e_left, b_left, f_left = seat(b_rat, f_rat, max_scale, data["max_cap"], b_weight, f_weight, data["e_dmd"], data["b_dmd"], data["f_dmd"])

#freq
    return_time = frequencies(data["distance"], data["speed"])
#rev
    total_rev_flight = revenue (e_seat, b_seat, f_seat, data["e_price"], data["b_price"], data["f_price"])
#6)done

    print("\n === RESULTS ===")

    print("\n--- Seat Configuration ---")
    print("Economy Class: ", e_seat)
    print("Business Class: ", b_seat)
    print("First Class: ", f_seat)

    print("\n--- Seat Remaining ---")
    print("Economy Class: ", e_left)
    print("Business Class ", b_left)
    print("First Class ", f_left)

    print("\n Return Time: ",return_time)

    print("\n Total Revenue per Flight ($) : ", total_rev_flight)

main()
