import sys

'''
RSA Calculator
'''

while True:
    method = input("Encrypt, Decrypt or exit?\n")
    method.strip()
    method.lower()

    if method == "encrypt":
        n = int(input('n'\n))
        e = int(input('e\n'))
        d = int(input('d\n'))
        m = int(input('m\n'))
        result = (m**e) % (n)

        print("c =", result)

    elif method == "decrypt":
        n = int(input('n\n'))
        e = int(input('e\n'))
        d = int(input('d\n'))
        c = int(input('c\n'))

        result = (c**d) % (n)

        print("m =", result)

    elif method == "exit":
        sys.exit(0)
