from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

# print(bsObj.find_all("span"))

# 특정 태그 클래스 텍스트 추출
# nameList = bsObj.find_all("span", {"class":"red"})
# for name in nameList:
#     print(name.get_text())

# find() find_all()
# color_list = bsObj.find_all("span", {"class":{"green","red"}})
# for color in color_list:
#     print(color.get_text())

# 특정 텍스트 횟수
# nameList = bsObj.find_all(text="the prince")
# print(len(nameList))

# 트리이동
# 자식과 자손

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "html.parser")

# print(bsObj)

# 테이블에 들어있는 제품 행 목록
# for child in bsObj.find("table", {"id":"giftList"}).children:
#     print(child)

# 테이블에 첫번째 타이틀행을 제외한 모든 제품행
# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
#     print(sibling)

# 부모 다루기
print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
