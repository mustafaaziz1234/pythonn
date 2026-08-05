passenger_name = "Aarav"
destination = "Goa"
ticket_price = 850.50
number_of_tickets = 3
is_available = True

print("passenger name:" , passenger_name)
print("Destination:" , destination)
print("Ticket price:" , ticket_price)
print("Availablity of tickets", is_available)

print(type(passenger_name))
print(type(destination))
print(type(ticket_price))
print(type(is_available))

#arthimetic calculations

total_cost = ticket_price * number_of_tickets
discount = 100
final_cost = total_cost - discount

print("\nTotal cost of tickets: Rs" , total_cost)
print("Discount : Rs", discount)
print("Final cost of tickets: Rs" , final_cost)
print("Double ticket price: Rs" , ticket_price * 2)
print("Increased ticket price after increase of 50Rs: Rs" , ticket_price + 50)
print("Half ticket price: Rs" , ticket_price/2)

#COMPARISONS

print("\nIs ticket price under 1000" , ticket_price<1000 )
print("Are more than 2 tickets booked?" ,  number_of_tickets > 2)
print("Is destination Goa?:" , destination == "Goa")
print("Is the final cost above Rs 2000?" , final_cost > 2000)
 #STRING OPERATIONS 
 
travel_message = passenger_name + " is traveling to " + destination + "."

print("\n Travel message:" , travel_message)
print("passenger name" , passenger_name.lower())
print("Destination:" , destination.upper())
print("First letter of destination:" , destination[0])
print("length of passengers name:" , len(passenger_name))

#swapping part
m = 700
e = 900
print("\n Before swapping morning ticket = " , m)
print("\nbefore swapping evening ticket = " , e)

e ,m = m , e 

print("\nMorning ticket price after swapping =" , m)
print("\nevening ticket price after swapping = " , e)

#final summary
print("\n--------------------")
print("passenger summary")
print("--------------------")
print("\nPassenger name:" , passenger_name)
print("Destination:" , destination)
print("Tickets booked:" , number_of_tickets)
print("final amount = Rs", final_cost)
print("Booking confirmed? :", is_available)

