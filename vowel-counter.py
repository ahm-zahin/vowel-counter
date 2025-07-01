print('Welcome to the vowel counter program')
while True:
    c=int(input('choose 1 to continue or 2 to exit: '))
    if c == 1:
        print()
        sen=str(input('enter sentence:  '))
        sen=sen.lower() 
        for punc in ['!', '?', ':', ';', '-', '_', '(', ')', '"', "'", '@', '#', '$', '%', '^', '&', '*', '+', '=', '<', '>', '/', '\\']:
            sen = sen.replace(punc, '')
        count=0
        counta=0
        counte=0
        counti=0
        counto=0
        countu=0
        for letter in sen:
            if letter in 'a':
                counta += 1
            elif letter in 'e':
                counte += 1
            elif letter in 'i':
                counti += 1
            elif letter in 'o':
                counto += 1
            elif letter in 'u':
                countu += 1
        print()
        print(f'the number of vowels is {counta + counte + counti + counto + countu}')
        if counta> 0:
            print(f'the letter a appeared {counta} times')
        if counte > 0:
            print(f'the letter e appeared {counte} times')
        if counti > 0:
            print(f'the letter i appeared {counti} times')
        if counto > 0:
            print(f'the letter o appeared {counto} times')
        if countu > 0:
            print(f'the letter u appeared {countu} times')

    elif c == 2:
        print(f'{c} is pressed, we are exiting...')
        break
    else:
        print('invalid input, please enter 1 or 2')
        continue