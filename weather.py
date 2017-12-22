## /c/Users/mcse/AppData/Local/Programs/Python/Python36-32/Scripts/pip
## http://maps.googleapis.com/maps/api/geocode/json?address=haifa
import requests

def calc_temp(temp):
    return round((float(temp)-32) * (5/9) , 2)


def pretty_print(jres):
   curr_dic = jres["currently"]
   print("Time zine: " + jres["timezone"])
   print("Condition: " + curr_dic["icon"])
   print("humidity: " + str(curr_dic["humidity"]))
   print("windSpeed: " + str(curr_dic["windSpeed"]))
   print("temperature " + str((calc_temp(curr_dic["temperature"])))+ " C ")

   #print(curr_dic)



resp = requests.get('https://api.darksky.net/forecast/0d584daf877a4ff2998afe4329840ef9/32.7996897,34.9817565')
if resp.status_code != 200:
    # This means something went wrong.
    raise requests.RequestException('GET ERROR {}'.format(resp.status_code))

j_resp = resp.json()
pretty_print(j_resp)


