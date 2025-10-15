#print("--- Movie Ticket Pricer ---")
#a=int(input("Please enter your age: "))
#if a<=12:
#    print("You fall into the 'Children' category")
#    print("Ticket price: $8")
#elif a>=65:
#    print("You fall into the 'Seniors' category")
#    print("Ticket price: $10")
#else:
#    print("you fall into the 'Adults' category")
#    print("Ticket price: $15")

print("--- Running Total Calculator ---")
total=0
while True:
    users_input=input("Enter a number or 'done': ")
    if users_input=='done':
        break
    total += float(users_input)
print("--- Final Calculation ---")
print(f"The final sum of all numbers is: {total}")