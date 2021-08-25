def machine():
    # creating key strings
    keys = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !'
    # auto generating the vaules of strings
    # value will be generted by taking last to first
    # concatinated with the rest of the string
    values = keys[-1] + keys[0:-1]

    # creating two dictionaries
    encrytDict = dict(zip(keys, values))
    decryptDict = dict(zip(values, keys))

    # user input
    message = input("Enter your secret message: ")
    mode = input("Crypto Mode : Encode(E) OR Decode(D)")

    #encode and decode
    if mode.upper() == 'E':
        newMessage = ''.join([encrytDict[letter]
                              for letter in message])
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter]
                              for letter in message])
    else:
        print("Please try again, wrong choice entered")

    return newMessage


print(machine())