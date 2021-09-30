file = open("Dictionary")
Dictionary = {}
for line in file:
    Dictionary[line[0:3]] = line[3]

def main():
    userCode = input("Enter the secretCode: ")
    message = ""
    Temp = ""
    for i in userCode:
        if " " in i:
            message += " "
            continue
        Temp += i
        if len(Temp) == 3:
            if Temp in Dictionary:
                message += Dictionary[Temp]
                Temp = ""
    print(message)

main()