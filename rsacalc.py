import sys


while True:
    method = input("Encrypt, Decrypt or exit?\n")
    method.strip()

    if method == "encrypt":
        p = int(input('p\n'))
        q = int(input('q\n'))
        e = int(input('e\n'))
        d = int(input('d\n'))
        m = int(input('m\n'))
        result = (m**e) % (p*q)

        print("c =", result)

    elif method == "decrypt":
        p = int(input('p\n'))
        q = int(input('q\n'))
        e = int(input('e\n'))
        d = int(input('d\n'))
        c = int(input('c\n'))

        result = (c**d) % (p*q)

        print("m =", result)

    elif method == "exit":
        sys.exit(0)
