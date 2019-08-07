import pandas as pd
from urllib.request import urlopen
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# request => 요청하는거를 웹에 요청한 결과값을 얻어올수 있는 모듈
import requests as req
# 웹에 요청한 결과를 보내주는 모듈
from bs4 import BeautifulSoup


DATA_PATH = '/학부인턴/자료/'
page_data = pd.read_csv(DATA_PATH + 'normal_pages.csv', header = None)
rows = page_data.shape[0]


def get_html(url):
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

    html = ""
    ret = req.get(url, headers=headers, verify=False)

    if ret.status_code == 200:
        html = ret.text

    return html


for j in range(1):
#     url = page_data[0][j]
    url = ("https://www.google.com/search?biw=1440&bih=821&tbm=isch&sa=1&ei=n9E_XaLLH7C9mAXX-LmQDA&q=images&oq=images&gs_l=img.3..0l10.4274.5251..5472...0.0..0.125.752.2j5......0....1..gws-wiz-img.......0i7i30j0i10i19j0i7i30i19.Z31L5tqxfao&ved=0ahUKEwjiluHi8NvjAhWwHqYKHVd8DsIQ4dUDCAY&uact=5")
    html = get_html(url)

        #페이지 status_code 가 200 일때 2XX 는 성공을 이야기함
    bs_object = BeautifulSoup(html,"html.parser")
        # 인스턴스 생성
    # print(bs_object)
    img_data = bs_object.find_all("img")




    temp = []
    for i in enumerate(img_data[1:]):
        #딕셔너리를 순서대로 넣어줌

        # try:
            print(i[1].attrs['src'])
            if '.jpg' in i[1].attrs['src'] or '.bmp' in i[1].attrs['src']:
                if 'https://' in i[1].attrs['src'] or 'http://' in i[1].attrs['src']:

                    print(i[1].attrs['src'])
                    t = urlopen(i[1].attrs['src']).read()
                else:
                    print(url + i[1].attrs['src'])
                    t = urlopen(url + i[1].attrs['src']).read()

                filename = 'page_' + str(j) + '_img_' + str(i[0] + 1) + '.jpg'


                with open('test_img/' + filename, "wb") as f:
                    if t in temp:
                        print("same file passed")
                        continue
                    else:
                        f.write(t)
                        print("Save Success")
                        temp.append(t)

        #
        # except Exception as e:
        #     print(e)



