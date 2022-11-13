loginDetails = {'anna': 'anna1991', 'bob': 'xxl', 'sam': 'howmuchisthefish'}

print('# Welcome! You have three attempts to enter your login details.')

attempt = 0
while attempt < 3:
    user_name = input('Username: ')
    password = input('Password: ')
    success = False
    for key, value in loginDetails.items():
        if (key == user_name and value == password):
            success = True
            break
        if (key == user_name and value != password):
            print(f"Password for {user_name} is incorrect. Try again.")
    attempt += 1
    if not success:
        if attempt < 3:
            print('Login was not successful. Try again.')
        else:
            print('Sorry, that was your third attempt!')
    else:
        break

if success:
    print('-----------------------')
    print('Logged in successfully!')
