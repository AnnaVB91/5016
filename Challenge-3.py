mins = int(input("Enter the number of minutes used this month: "))
txts = int(input("Enter the number of texts sent this month: "))

base_rate = 1500
additional_mins_cost = 25
additional_texts_cost = 15
allowed_minutes = 50
allowed_texts = 50
cost_of_extra_minutes = 0
cost_of_extra_texts = 0
call_centre_fee = 44
tax = 0
subtotal = 0

print("-----------------------------")
print(f"Your base fee is: ${base_rate/100}")

if mins > allowed_minutes:
    cost_of_extra_minutes = (mins - allowed_minutes) * additional_mins_cost
    print(f"Your additional minutes fee is: {cost_of_extra_minutes/100}")

if txts > allowed_texts:
    cost_of_extra_texts = (txts - allowed_texts) * additional_texts_cost
    print(f"Your additional texts fee is: {cost_of_extra_texts/100}")

print(f"Your 111 call centre fee is: ${call_centre_fee/100}")

subtotal = base_rate + cost_of_extra_minutes + cost_of_extra_texts + call_centre_fee
tax = subtotal * 0.05

print(f"Taxes: ${round(tax/100,2)}")
print("-----------------------------")
print(f"Subtotal: ${subtotal/100}")
print(f"Total Charges: ${round((subtotal + tax)/100,2)}")
