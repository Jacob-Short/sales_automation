from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.generic import View

import requests
import pandas as pd
import json
import time


@login_required(login_url='/login/')
def homepage_view(request):

    url = "https://www.walmart.com/cp/api/get-deals-list?prg=desktop&dealsId=christmas-gifts&ps=60&page=2&sort=new&shelf_id=61381&shelfType=manual"

    headers = {
      'authority': 'www.walmart.com',
      'cache-control': 'max-age=0',
      'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
      'sec-ch-ua-mobile': '?0',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'sec-fetch-site': 'none',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-user': '?1',
      'sec-fetch-dest': 'document',
      'accept-language': 'en-US,en;q=0.9',
      'cookie': 'location-data=89131%3ALas%20Vegas%3ANV%3A%3A1%3A1|2l3%3B%3B6.19%2C284%3B%3B7%2C43e%3B%3B7.65%2C422%3B%3B8.64%2C3cj%3B%3B9.1%2C200%3B%3B9.44%2C1f2%3B%3B10.48%2C2tj%3B%3B11.46%2C2vk%3B%3B11.52%2C423%3B%3B11.82||7|1|1xj2%3B16%3B10%3B14.4; DL=89131%2C%2C%2Cip%2C89131%2C%2C; TB_Latency_Tracker_100=1; TB_Navigation_Preload_01=1; TB_DC_Flap_Test=0; vtc=dvJyX6TDoY0dsQWRSQ7u3k; bstc=dvJyX6TDoY0dsQWRSQ7u3k; mobileweb=0; xpa=U20On; _pxhd=7gKyvdgiRKHq2h/Q0VBw5EMjqSHrf1G48lb-NUEP2RXJllPgDA0E5YLtN--rUWMDbG2GsnHdMIYXFCdZnEXX/g==:q2J8dQ4d2EgXy0HcGIKhBEYzeU6g/lWq5DD5v9rFeF5peQIo9Vc7Q4sVY81Q9pepYuT7DtRpNZQch8j6qROJKkP4azcGy0dsUD7b-np3Ty8=; TBV=7; cart-item-count=0; _pxvid=6885c3d3-14fa-11ec-980c-51667954566e; tb_sw_supported=true; xpm=1%2B1631582626%2BdvJyX6TDoY0dsQWRSQ7u3k~%2B0; TB_SFOU-100=1; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1631583336085@firstcreate:1631582626998"; next-day=1631658600|true|false|1631707200|1631583336; TS01b0be75=01538efd7cff405aea6302c135cf8ca970d72343945a593c04228f5e5b57a3d91924e9148073e0e06099a5ffe8c2cfa67be5339092; TS013ed49a=01538efd7cff405aea6302c135cf8ca970d72343945a593c04228f5e5b57a3d91924e9148073e0e06099a5ffe8c2cfa67be5339092; DL=89131%2C%2C%2Cip%2C89131%2C%2C; TS013ed49a=01538efd7cff405aea6302c135cf8ca970d72343945a593c04228f5e5b57a3d91924e9148073e0e06099a5ffe8c2cfa67be5339092; bstc=dvJyX6TDoY0dsQWRSQ7u3k; com.wm.reflector="reflectorid:0000000000000000000000@lastupd:1631583373457@firstcreate:1631582626998"; mobileweb=0; vtc=dvJyX6TDoY0dsQWRSQ7u3k; xpa=U20On; xpm=1%2B1631582626%2BdvJyX6TDoY0dsQWRSQ7u3k~%2B0; TS01b0be75=01538efd7cff405aea6302c135cf8ca970d72343945a593c04228f5e5b57a3d91924e9148073e0e06099a5ffe8c2cfa67be5339092; _pxhd=TFy7/oFvpgGqnu-TWfPgnTvi9rNJsUFFwSwM/qOk/eFyoKT8cTDXA3xua/N4MN/YL0W/mV2iS3bJzLbjWtklwQ==:hxYLpdvn3e7IcM14C78i4wL3uziFYArvcdZuK2KiiINaPDCHsV-dxk/R6gXdnCXBoPQgWDdcoES2WEFtGYknEP5UR6OvxZhKtcz3H4hTZS8=',
      'sec-gpc': '1'
    }

    products = pd.DataFrame([])

    # only going through first 2 pages for dev
    for page in range(1,2):
        url = f"https://www.walmart.com/cp/api/get-deals-list?prg=desktop&dealsId=christmas-gifts&ps=60&page={page}&sort=new&shelf_id=61381&shelfType=manual"
        response = requests.get(url, headers=headers)
        data = json.loads(response.text)
        df_products = products.append(pd.json_normalize(data['items']), ignore_index=True)
        products = data['items']
        time.sleep(1)
        print(f'Getting page {page}....')

    # df_products.to_csv('walmart-products.csv')
    # breakpoint()
    context = {'products': products[:10]}
    return render(request, 'homepage.html', context)


class ApiView(View):
    '''connects to api to retrive food items'''
    
    def get(self, request):
        pass


    def post(self, request):
        pass
