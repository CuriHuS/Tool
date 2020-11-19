import random
import os # for .exe

def Whois(Range, Number): #Range = Total people, Number = Choice people number
    List = []
    while True:
        iR= random.randrange(1, Range+1)
        if Number != 1:
            if len(List) == 0:
                List.append(iR)
                continue
            elif len(List) == Number:
                break
            else:  # Already a person                
                if List.count(iR) == 0:
                    List.append(iR)
                    continue
                else:
                    continue
        else:
            List.append(iR)
            break

    List.sort()
    return List
    print(List)

    
# Below is the code for Pyinstaller
# Variable "phone_list" is total list for command "whois"
# Variable "Lucky" is selected object in total list, "phone_list".
A = str(input("Please enter 1 to proceed."))

if A == "1":
    f = open('# Your file(.py) path', 'r', encoding='utf-8') # I made with csv file
    csvrd = csv.reader(f)
    phone_list = []

    for line in csvrd:
        phone_list.append(line)

    f.close()
    print(phone_list)

    Lucky = Whois(73,5)
    for i in range(0,5):
        print(phone_list[Lucky[i]])

else:
    print("Error")

os.system('pause')
