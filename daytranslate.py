dic_days_trans = {
}
flag = True
# initiate a dictionary
def ini_dic(transarr):
    i=0
    for i in range(len(transarr)):
        tarr = transarr[i].split(":")
        dic_days_trans[tarr[0]] = tarr[1].rstrip()


#prints the translation according to the user selection
def print_trans(dic):
    i = 0
    selecarr = []
    if flag:
        for x in dic.keys():
            print (str(i) +") "+x)
            selecarr.append(x)
            i += 1
        uleng_input = input("please select the language you want to translate : ")
        try:
            print (dic[selecarr[int(uleng_input)]])
        except:
            print("no such language ")
    else:
        print ("no such day")




if __name__=="__main__":
    while True:
        uday_input = input("please select a day : ")

        if uday_input == "quit":
            break
        # open translation file  and initiate a dictionary according the day the user typed
        #file = open("day_dic.txt", "r")
        dic_days_trans={}
        flag = True
        with open('day_dic.txt', 'r') as f:
            for lines in f:
                temp_arr = lines.split(";")
                if temp_arr[0] == uday_input:
                    arr_trans=temp_arr[1].split(",")
                    ini_dic(arr_trans)
            if len(dic_days_trans) == 0:
                flag = False

        print_trans(dic_days_trans)



