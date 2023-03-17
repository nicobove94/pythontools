def diffchecker(str1, str2):
    differences = []

    for i, (char1, char2) in enumerate(zip(str1, str2)):
        if char1 != char2:
            differences.append((i, char1, char2))

    return differences

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    if len(string1) != len(string2):
        print("The two strings have different lengths.")
        return

    differences = diffchecker(string1, string2)

    if not differences:
        print("No differences found")
    else:
        print("Differences found:")
        for index, char1, char2 in differences:
            print(f"Position {index}: '{char1}' != '{char2}'")

if __name__ == "__main__":
    main()
