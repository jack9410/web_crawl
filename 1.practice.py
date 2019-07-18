from urllib.request import urlopen
from urllib.request import HTTPError
from bs4 import BeautifulSoup
try:
    html = urlopen("http://www.python.org/about")

#http 에러 예외
except HTTPError as e:
    print(e)


bsObject = BeautifulSoup(html,"html.parser")

# 웹문서 전체 출력
#print(bsObject)

# 타이틀 가져오기
# print(bsObject.head.title)

# 메타 데이터 가져오기
# for meta in bsObject.head.find_all('meta'):
#     print(meta.get('content'))

# 원하는 태그 내용 가져오기

# meta 태그중 name 속성 description
# print(bsObject.head.find("meta", {"name":"description"}))

# 태그의 content 내용
# print(bsObject.head.find("meta", {"name":"description"}).get('content'))

# a 태그로 둘러싸인 텍스트와 a태그의 href 속성 출력
# html = urlopen("http://www.naver.com")
# bsObject = BeautifulSoup(html, "html.parser")
#
# for link in bsObject.find_all('a'):
#     print(link.text.strip(), link.get("href"))

# print(bsObject.html.h1)

# http 에러, none 객체 처리
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObject = BeautifulSoup(html.read(), "html.parser")
        title = bsObject.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.naver.com")

if title == None:
    print("Title could not be found")
else:
    print(title)