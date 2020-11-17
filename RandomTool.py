import random

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
