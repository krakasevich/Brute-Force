import random, string

alphabet = string.printable[:95]
charLength = 3

def generate_password(charLength):
    outString = ''
    while len(outString) < charLength:
        outString += random.choice(alphabet)
    return outString

if __name__ == '__main__':
    randPw = generate_password(charLength)
    print('Random password: ', randPw)