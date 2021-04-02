print('WELCOME TO SCALES BANK!')
print('Swipe your card to begin')
userPin = 1234
atm_pin =input('enter your pin')
if userPin == atm_pin:
    import datetime
    now = datetime.datetime.now()
    print("current date and time is:")
    print(now.strftime("%y-%m-%d %H:%M:%S"))
    print('please choose a transaction.')
    print('1. withdraw cash')
    print('2. deposit cash')
    print('3. view balance')
    print('4. file complaint')
    print('5. quit')
else:
    atm_pin = input('enter your pin')
    
    
transaction = '1', '2', '3', '4', '5',               
trans = input(transaction)
if trans == ('1'):
        print('how much would you like to recieve')
selectedAmount = ('10', '20', '30', '40' '\n')
withdraw = input(selectedAmount)
if(withdraw in selectedAmount):
        print('here is your cash.')
else:
    withdraw = input(selectedAmount)

if trans == ('2'):
    deposit = ('100', '200', '300')
    enter = input(deposit)
    print('how much would you like to deposit? \n')
    if(enter in deposit):
        print('money deposited, thank you for your business.')
else:
    enter = input(deposit)
        

if trans == ('3'):
    print('$1,200')

elif trans == ('4'):
    print('what is your complaint?')            