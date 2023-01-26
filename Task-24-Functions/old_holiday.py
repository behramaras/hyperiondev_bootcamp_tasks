# The function takes the number of nights a user will be staying at a hotel as an argument.
# Returns multiplying the hotel charge per night by the number of nights.

def hotel_cost(num_nights):
    per_night_charge = 40

    return per_night_charge * num_nights

# The function takes a city name as an argument. Returns the flight cost based on the options.

def plane_cost(city):

    if city.lower() == "new york":
        fly_cost = 200

    elif city.lower() == "paris":
        fly_cost = 100

    elif city.lower() == "berlin":
        fly_cost = 80

    elif city.lower() == "antalya":
        fly_cost = 40

    else:
        fly_cost = 50

    return fly_cost

# The function takes the number of days the car will be hired for as an argument.
# Multiplies the daily charge with the number of days and returns the result as total cost.

def car_rental(num_days):
    daily_charge = 10

    return daily_charge * num_days

# The functions takes 3 arguments and passes them to the indented functions and calculates the total cost of the holiday.
# Properly prints out all the details about the holiday.

def holiday_cost(num_nights, city, num_days):

    hotel = hotel_cost(num_nights)
    
    plane = plane_cost(city)

    car = car_rental(num_days)

    total = hotel + plane + car

    print (f"""
        The cost of the flight to {city.title()}: £{plane}\n
        The total cost of the hotel stay in {city.title()} for {num_nights} nights: £{hotel}\n
        The cost of the car rental for {num_days} days: {car}\n
        The total cost of the holiday: £{total}\n
                        ---------
    """)

holiday_cost(7, "Antalya", 5)
holiday_cost(5, "Paris", 1)
holiday_cost(4, "Berlin", 2)

