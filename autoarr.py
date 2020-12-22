if __name__ == "__main__":
    pass

total = 0
hif = '-'
space = ' '
req =[]

def autotitle(list):
    global total
    for i in range(len(list)):
        if type(list[i]) == int:
            total += list[i]*2
        else:
            total +=len(list[i])
            req.append(len(list[i])+(list[i+1])*2)
            total += 1
    total += 1
    print(hif*total)
    for i in range(len(list)):
        if i%2 == 0:
            print('|'+space*list[i+1], end='')
            print(list[i], end='')
            print(space*list[i+1], end='')
    print('|')
    print(hif*total)



def autoarr(list):
    print('|',end='')
    for i in range(len(list)):
        print(f"{list[i]}{space*(req[i]-len(str(list[i])))}|",end='')

    print()
    print(hif*total)
        