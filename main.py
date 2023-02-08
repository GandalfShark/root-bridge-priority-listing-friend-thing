# quick program to build a list of root bridge priority numbers
# and then check if the number is valid

count = 0
# the counter for the numbers
rbp_numbers = []
# blank list to hold the numbers generated

def checkinRBP():
    # print(rbp_numbers) -- test code commented out
    number = input('enter a value to check if it is  a valid bridge priority value.\n>')
    try:
        number = int(number)
    except ValueError:
        print('That is not a number yah dingus!')
    if number in rbp_numbers:
        print('yup.')
    else:
        print('Nope.')


while count < 61440:
    rbp_numbers.append(count)
    count += 4096
rbp_numbers.append(61440)
# build the list of bridge priority values

while True: # TODO make this a gameified interface
    checkinRBP()
    u_quitingYN = input('Q or q to quit.\nENTER to continue')
    if u_quitingYN in ['Q', 'q', 'quit', 'exit', 'die']:
        break

print('Smell ya later.')

