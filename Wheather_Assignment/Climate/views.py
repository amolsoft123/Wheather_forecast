import json

from django.shortcuts import render
import requests

# Create your views here.

def display_wheather(request):
    print("in dispaly wheather function")
    data = requests.get("https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmin/ranked/England.txt")
    # print(data.text)
    # whather_data = data.text
    # json_data = json.loads(data.text)
    # print(json_data)
    return render(request,"index.html")


def get_wheather_data(request):
    if request.method == 'POST':
        print("in get wheather data api")
        order_stat = request.POST["stat"]
        # year_order_stat =request.POST["year_order_stat"]
        region = request.POST["region"]
        parameter =request.POST["parameter"]
        print(region)
        print(parameter)
        print(order_stat)
        BASE_URL = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/"
        CALL_URL = BASE_URL + parameter + "/" + order_stat +"/" + region +".txt"
        print(CALL_URL)
        data = requests.get(CALL_URL)
        whather_data = data.text
    return render(request, "display_wheather.html", {"whather_data": whather_data})
