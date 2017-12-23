## /c/Users/mcse/AppData/Local/Programs/Python/Python36-32/Scripts/pip
## http://maps.googleapis.com/maps/api/geocode/json?address=haifa

## 'https://api.darksky.net/forecast/0d584daf877a4ff2998afe4329840ef9/32.7996897,34.9817565'

import requests

def calc_temp(temp):
    return round((float(temp)-32) * (5/9) , 2)


def dark_req(loc):
    url = "https://api.darksky.net/forecast/0d584daf877a4ff2998afe4329840ef9/"+loc
    resp = requests.get(url)
    if resp.status_code != 200:
        # This means something went wrong.
        raise requests.RequestException('GET ERROR {}'.format(resp.status_code))

    j_resp = resp.json()
    return j_resp


#def get_lat(map_res):


def get_location(city):
    resp = requests.get('http://maps.googleapis.com/maps/api/geocode/json?address='+city)
    if resp.status_code != 200:
        # This means something went wrong.
        raise requests.RequestException('GET ERROR {}'.format(resp.status_code))

    j_map_res = resp.json()
    #print(j_map_res)
    loc_dic = j_map_res["results"]
    loc_dic2 = loc_dic[0]["geometry"]
    loc_dic3 = loc_dic2["location"]
    lat = loc_dic3["lat"]
    lng = loc_dic3["lng"]
    return str(lat)+","+str(lng)



def pretty_print(jres):
   curr_dic = jres["currently"]
   print("Time zine: " + jres["timezone"])
   print("Condition: " + curr_dic["icon"])
   print("humidity: " + str(curr_dic["humidity"]))
   print("windSpeed: " + str(curr_dic["windSpeed"]))
   print("temperature " + str((calc_temp(curr_dic["temperature"])))+ " C ")


if __name__ == '__main__':
    i = 0
    file = open('cities.txt','r')
    line = file.readline()
    cities_arr = line.split(';')
    for x in cities_arr:
        print (str(i)+") "+ x)
        i +=1
    ui_city = input("please select a city : ")
    loca=get_location(cities_arr[int(ui_city)])
    dark_res=dark_req(loca)
    pretty_print(dark_res)







