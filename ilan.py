def addsum(a: int, b: int) -> int:
    return a + b


def print_list(arr):
    for i in arr:
        print(i)


def printdic(dic):
    for x in dic.keys():
        print(dic[x])


def namepr(fname):
    name = fname.split(" ")
    if len(name) == 2:
        print("your first name is:" + name[0])
        print("your last name is :" + name[1])
    else:
        print("this is not a good name")


if __name__ == '__main__':
    student = {
        "name": "ilan",
        "id": 33611542,
        "mail": "ilanbabu@gmail.com"
    }
    print(addsum(3, 4))
    print_list(["ilan", "the", "king"])
    printdic(student)
    try:
        lastname = student["last"]
    except KeyError:
        print("can't find key")

    while True:
        uname = input("please enter your full name:")
        if uname != "exit":
            namepr(uname)
        else:
            break
