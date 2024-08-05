from tqdm import tqdm 
import itertools, random, string, time

startTime = int(time.time())

alphabet = string.printable[:95]
charLength = 4

def generate_password(charLength):
    """
    Generate a random password of specified length.

    Parameters:
    charLength (int): The length of the password to be generated.

    Returns:
    str: A random password of the specified length.
    """
    outString = ''
    while len(outString) < charLength:
        outString += random.choice(alphabet)
    return outString

def bruteForce(pwToBrute):
    """
    Brute force a password by trying all possible combinations of characters.

    Parameters:
    pwToBrute (str): The password to be brute forced.

    Returns:
    tuple: The brute forced password as a tuple of characters. If the password is not found, returns None.

    The function uses a progress bar from the tqdm library to estimate the remaining time.
    It calculates the estimated time based on the position of the first character in the password
    and the length of the password.
    """
    enstimatedTime = int((alphabet.index(pwToBrute[0]) / len(alphabet)) * (len(alphabet) ** len(pwToBrute)))
    pwTuple = tuple(pwToBrute)
    charList = [[x for x in alphabet]] * len(pwToBrute)

    for combination in tqdm(itertools.product(*charList), total = enstimatedTime):
        if combination == pwTuple:
            return combination

if __name__ == '__main__':
    randPw = generate_password(charLength)
    print('Random password: ', randPw)
    result = bruteForce(randPw)
    endTime = int(time.time())
    print(f'Bruteforced password {result} in {endTime - startTime} seconds')
    