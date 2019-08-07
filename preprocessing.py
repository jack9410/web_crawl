import gambling
from bs4 import BeautifulSoup
import pandas as pd
import urllib3
import csv
import codecs
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def page_text(url):

    html = gambling.get_html(url)
    bsObj = BeautifulSoup(html, "html.parser")

    title = gambling.title(bsObj)
    link_text = gambling.link_text(bsObj)
    # keyword = gambling.keyword(bsObj)
    # description = gambling.description(bsObj)
    meta_data = gambling.meta_data(bsObj)

    # return (title + link_text + keyword + description+ meta_data)
    return (title + link_text + meta_data)

# print(page_text("https://www.korea12.com/"))

DATA_PATH = '/학부인턴/자료/'
page_data = pd.read_csv(DATA_PATH + '도박.csv', header = None)
rows = page_data.shape[0]

# for i in range(rows):
#     print('https://' + page_data[0][i])


# def debug_all():
#
#     success = 0
#     error = 0
#
#     for i in range(rows):
#         url = 'https://' + page_data[0][i]
#         try:
#             page_text(url)
#             success += 1
#             print('success! = ', success)
#
#         except requests.exceptions.ConnectionError:
#             print("Connection Error")
#
#         except requests.exceptions.SSLError:
#             print("SSL Error")
#
#         except Exception as e:
#             print(e)
#             error += 1
#             print(url)
#             print('에러 인덱스 =', i)
#
def debugging(k):
    print('https://' + page_data[0][k])
    print(page_text('https://' + page_data[0][k]))



def write_csv():

    success = 0
    error = 0
    csvFile = open(DATA_PATH + "text_data_2.csv", 'w+')

    try:
        writer = csv.writer(csvFile)


        for i in range(224,rows):

            url = 'https://' + page_data[0][i]
            try:
                writer.writerow((page_text(url),))
                success += 1
                print("page", i+1, " success")

            except requests.exceptions.ConnectionError:
                print("page", i+1,"Connection Error")

            except requests.exceptions.SSLError:
                print("page", i+1,"SSL Error")

            except Exception as e:
                print(e)
                error += 1
                print(url)
                # print('에러 인덱스 =', i)

    finally:
        csvFile.close()
    print('total = ', error + success)
    print('success =', success)
    print('error =', error)


write_csv()
# 224번까지함


# debugging(224)
# debug_all()

# print('에러 개수 = ', error)
