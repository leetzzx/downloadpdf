import requests
def getinfo(productId):
    url = "https://mat.jwsmed.com/JARVIS-SERVITIZATION-REST/servitization/shop/product/detail"
    params = {
        "productId":"80"
    }
    jsbody = {}
    response = requests.get(url=url,params=params)
    if response.status_code == 200:
        data = response.json()
        if data['data']['specifications'] != []:
            specificaton = data['data']["specifications"][0]
            jsbody['name'] = specificaton['name']
            jsbody['url'] = data['data']["specifications"][0]['url']
            return jsbody
        else:
            print("no specification")
    else:
        print("get data failed")

product1 = getinfo(50) 
url = product1['url']
