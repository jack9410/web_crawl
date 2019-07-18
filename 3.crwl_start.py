from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "html.parser")

# 위키백과 페이지 링크 목록
# for link in bsObj.find_all("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# 다른 위키백과 항목 링크
# for link in bsObj.find("div", {"id":"bodyContent"}).find_all("a", href=re.compile("^(/wiki/)((?!:).)*$")):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# 전체 사이트 크롤링

# 데이터 수집
# pages = set()
# def getLinks(pageURL):
#     html = urlopen("http://en.wikipedia.org"+pageURL)
#     bsObj = BeautifulSoup(html, "html.parser")
#     for link in bsObj.find_all("a", href=re.compile("^(/wiki/)")):
#         if link.attrs['href'] not in pages:
#             # 새 페이지 발견
#             newPage = link.attrs['href']
#             print(newPage)
#             pages.add(newPage)
#             getLinks(newPage)
#
#
# getLinks("")
#
# 무작위 외부링크 따라가기
import datetime
import random
from urllib.parse import urlparse
from urllib.request import HTTPError
# def httpError(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         print(e)


random.seed(datetime.datetime.now())

# 페이지에서 발견되 내부 링크 모두 목록으로 만든다
def getInternalLinks(bsObj, includeURL):
    internalLinks = []
    # /로 시작되는 모든 링크를 찾습니다.
    for link in bsObj.find_all("a" , href = re.compile("^(/|.*"+includeURL+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


# 페이지에서 발견된 외부 링크 모두 목록으로 만든다
def getExternalLinks(bsObj, excludeURL):
    externalLinks = []

    for link in bsObj.find_all("a", href = re.compile("^(http|www)((?!"+excludeURL+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


def getRandomExternalLink(startingPage):
    # httpError(startingPage)
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
    # print(urlparse(startingPage).netloc)
    # print(externalLinks)

    if len(externalLinks) == 0:
        domain = urlparse(startingPage).scheme + "://" + urlparse(startingPage).netloc
        internetLinks = getInternalLinks(bsObj, domain)
        print(startingPage)
        return getRandomExternalLink(domain + internetLinks[random.randint(0, len(internetLinks) - 1)])


    else:

        return externalLinks[random.randint(0, len(externalLinks) - 1)]


def followExternalOnly(startingPage):
    externalLink = getRandomExternalLink(startingPage)
    print("Random external link is: " + externalLink)
    followExternalOnly(externalLink)


followExternalOnly("http://oreilly.com")


