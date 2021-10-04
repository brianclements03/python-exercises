# 1. movies
In [4]: price = 3

In [5]: lm = 3

In [6]: bb = 5

In [7]: h = 1

In [8]: total_price = (lm + bb + h) * price

In [9]: total_price
Out[9]: 27
# 2.  working for a contractor
google_pay = 400
amazon_pay = 380
facebook_pay = 350
google_hours = 6
amazon_hours = 4
facebook_hours = 10
total_pay = (google_pay * google_hours) + (amazon_pay * amazon_hours) + (facebook_pay * facebook_hours)
total_pay
# 3. student enrollment
class_is_full = True
schedule_conflict = False
can_enroll = not class_is_full and not schedule_conflict
can_enroll
# 4. product offer
items_purchased = 1
offer_expired = False
premium_member = False
premium_member_override = items_purchased >= 2 or premium_member
premium_member_override
product_offer = premium_member_override and not offer_expired
product_offer
# 5. Use the following code to follow the instructions below:
username = 'codeup'
password = 'notastrongpassword'
# Create a variable that holds a boolean value for each of the following conditions:
#the password must be at least 5 characters
pw_long_enough = len(password) >= 5
pw_long_enough
#the username must be no more than 20 characters
u_n_short_enough = len(username) <= 20
u_n_short_enough
#the password must not be the same as the username
not_same = str(password) != str(username)
not_same
#bonus neither the username or password can start or end with whitespace
no_extra_spaces = username == username.strip() and password == password.strip()
no_extra_spaces
satisfactory_combo = pw_long_enough and u_n_short_enough and not_same
satisfactory_combo

# A list of dictionaries approach to the contractor exercise from https://ds.codeup.com/python/data-types-and-variables/

# Setup a list of dictionaries
# Each dictionary contains the client, rate, and amount of consulting hours
clients = [
    {
        "client": "Google",
        "rate": 400,
        "hours": 6,
    },
    {
        "client": "Amazon",
        "rate": 380,
        "hours": 4,
    },
    {
        "client": "Facebook",
        "rate": 350,
        "hours": 10,
    }
]

# programmatically determine the number of clients (the number of dictionaries on the list)
number_of_clients = len(clients)

# Set hours and compensation to zero
total_hours = 0
total_compensation = 0

# Iterate through each client
for client in clients:
    # Increase total_hours worked by the hours for each client
    total_hours += client["hours"]

    # calculate the rate * hours for each client
    client_subtotal = client["rate"] * client["hours"]

    print(f"After working {client['hours']} for {client['client']} at a rate of ${client['rate']} per hour, I earned ${client_subtotal}.")

    # update that subtotal to the total_compensation variable
    total_compensation += client_subtotal


print("---")
print(f"After working a grand total of {total_hours} for {number_of_clients} clients, I now have to pay taxes on ${total_compensation}.")