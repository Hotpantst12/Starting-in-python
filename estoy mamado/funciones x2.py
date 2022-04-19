

# python program to illustrate

# funtion with main




def getinteger():
    result = int(input('enter integer: '))
    return result

def main():
    print('started')

    # calling the getinteger function and

    # storing its return value in the variable

    output = getinteger()
    

    print(output)

# now we are required to tell python

# for 'main' function existence

if __name__=='__main__':
    main()
