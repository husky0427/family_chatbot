import requests

from api.base_api import BaseApi


class CentralWeatherBureauApi(BaseApi):
    
    BASE_URL = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/'
    

    def get_weather(self):
        dataid = 'F-D0047-077'  # 鄉鎮天氣預報-單一鄉鎮市區預報資料-臺南市未來2天天氣預報
        apikey = 'CWB-7715006B-7F5B-4958-A1DA-D2991B0FC0FC'
        param = {'Authorization': apikey}


        url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/{dataid}"
        res = requests.get(url, params=param)
        return res.content.decode()


if __name__ == "__main__":
    res = get_weather()
    with open('example.json', 'w') as f:
        f.write(res)
    print(res[0])