file = open("Dictionary")
Dictionary = {}
for line in file:
    Dictionary[line [3]] = line[0:3]

def main():
    userInput = input("Enter anything: ")
    end = ""
    for word in userInput:
        for letter in word:
            if letter in Dictionary:
                end += Dictionary[letter]
            else:
                end += letter
    print(end)

main()