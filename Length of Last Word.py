def lenof(strword):

    arr = strword.split(' ')
    leng = len(arr)
    lastword = arr[leng-1]
    print("the last word is: %s and its length is: %d"%(lastword,len(lastword)))


def reverswords(strwords):

    arr = strwords.split(' ')
    revarr =[]
    leng = len(arr)
    while leng > 0:
        revarr.append(arr[leng-1])
        leng -= 1
    print (" ".join(revarr))

def multistr(num1,num2):
    mul = int(num1)*int(num2)
    return str(mul)


if __name__ == '__main__':
    lenof("hello world babushkin ilan")
    reverswords("hello world babushkin ilan")
    print(multistr("10","12"))
