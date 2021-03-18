#https://www.youtube.com/watch?v=z_eALBTtQTk&ab_channel=AsimCode
num_tickets = input("How many tickets you need ?")
try:
    num_tickets = int(num_tickets)
except ValueError:
    print("Please try again!")
else:
    print(f"You need {num_tickets} tickets")
