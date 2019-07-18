from urllib.request import urlopen, HTTPError, Request
import requests
from bs4 import BeautifulSoup

# 링크 텍스트
def link_text(bsObj):
    result = ""

    allText = bsObj.findAll("a")

    for link in allText:
        if 'href' in link.attrs:
            # print(link)
            result += link.get_text()

    return result;



# title 텍스트
def title(bsObj):
    if bsObj.head.title is None:
        return None
    else:
        return bsObj.head.title.get_text()


# description 텍스트
def description(bsObj):

    result = ""

    for meta in bsObj.head.find_all('meta'):
        if meta.get('name') == "description":
            result += meta.get('content')

    return result


# 키워드
def keyword(bsObj):

    result = ""

    for meta in bsObj.head.find_all('meta'):
        if meta.get('name') == "keywords":
            result += str(meta.get('content'))

    return result


# 모든 메타데이터
def meta_data(bsObj):

    result = ""
    metadatas = set()

    for meta in bsObj.head.find_all('meta'):
        # print(meta.get('content'))
        metadatas.add(meta.get('content'))

    for data in metadatas:
        result += str(data)

    return result


# http 403 에러
def get_html(url):
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

    html = ""
    ret = requests.get(url, headers=headers)

    if ret.status_code == 200:
        html = ret.text

    return html


# http 에러 검사 후 크롤링
def HTTPerr(url):
    try:
        html = urlopen(url)

    # 403 에러시 헤더 가져오기
    except HTTPError as e:
        # req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        # response = urlopen(req).read()
        # text = response.decode('utf-8')
        # # print(response)
        # print(text)
        # print(e)

        html = get_html(url)
        bsObj = BeautifulSoup(html, "html.parser")

        print("title 결과")
        print("===================================")
        print(title(bsObj))
        print(); print()

        print("링크 텍스트 결과")
        print("===================================")
        print(link_text(bsObj))
        print(); print()

        print("메터데이터 - description")
        print("===================================")
        print(description(bsObj))
        print(); print()

        print("메타데이터 - keywords")
        print("===================================")
        print(keyword(bsObj))
        print(); print()

        print("메타데이터 전체 ")
        print("===================================")
        print(meta_data(bsObj))
        print(); print()

        # print(bsObj)

    else:
        bsObj = BeautifulSoup(html, "html.parser")

        print("title 결과")
        print("===================================")
        print(title(bsObj))
        print(); print()

        print("링크 텍스트 결과")
        print("===================================")
        print(link_text(bsObj))
        print(); print()

        print("메터데이터 - description")
        print("===================================")
        print(description(bsObj))
        print(); print()

        print("메타데이터 - keywords")
        print("===================================")
        print(keyword(bsObj))
        print(); print()

        print("메타데이터 전체 ")
        print("===================================")
        print(meta_data(bsObj))
        print(); print()
        # print(bsObj)




# 실험 사이트

# 한글
# HTTPerr("https://www.korea12.com/")
# HTTPerr("https://www.mtcheat.com/")
HTTPerr("http://10x10bet-kr.com/")
# HTTPerr("https://www.mtpolice888.com/")

# 로그인 화면
# HTTPerr("http://www.ham-jang2.com/")
# HTTPerr("https://go-ast.com/login_.php")
# HTTPerr("https://dajava.net/")
# HTTPerr("https://on.bada8282.com/")
# HTTPerr("https://87toto.com/")


# 인코딩 꺠짐
# HTTPerr("https://totopick.biz/")


# 영어
# HTTPerr("https://www.casinogates.co.uk/")
# HTTPerr("https://thebettingedge.co.uk//")
# HTTPerr("https://www.thisisvegas.com/")
# HTTPerr("https://betonaces.com/")

