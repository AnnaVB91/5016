rate = float(input("Enter the conversion rate between NZD and USD: "))
direction = input("Enter 'to' or 'from': ")
amount = float(input("Enter the amount you wish to convert: "))


def convert(rate, direction, amount):
    result = float
    if direction == "to":
        result = amount * rate
    else:
        result = amount * (1 / rate)
    return result


exchange_rate = convert(rate, direction, amount)

print('--------------------------------------------------------------------------')
print(f"The amount of currency when converted {exchange_rate} NZD is: {direction}")
