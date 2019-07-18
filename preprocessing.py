import gambling
from bs4 import BeautifulSoup

def page_text(url):

    html = gambling.get_html(url)
    bsObj = BeautifulSoup(html, "html.parser")

    title = gambling.title(bsObj)
    link_text = gambling.link_text(bsObj)
    keyword = gambling.keyword(bsObj)
    description = gambling.description(bsObj)
    meta_data = gambling.meta_data(bsObj)

    return (title + link_text + keyword + description+ meta_data)

print(page_text("https://www.korea12.com/"))