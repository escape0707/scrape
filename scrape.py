url = "https://bp.pep.com.cn/jc/ptgzkcbzsyjks/"

from os.path import isfile
if not isfile("./html.txt"):
    from urllib.request import Request, urlopen
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0"})
    http_response = urlopen(req)
    with open("html.txt", "wb") as f:
        f.write(http_response.read())
else:
    with open("html.txt", "rb") as f:
        http_response = f.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(http_response, "html.parser")
category_collection = soup.find_all("div", class_="con_list_jcdzs2020")

with open("urls.txt", "w", encoding="utf-8") as f:
    for category in category_collection:
        category_name = str(category.div.h4.string)
        book_collection = category.find_all("li", class_="fl js_cp")
        for book in book_collection:
            book_name = str(book.h6.a.string)
            download_link = url + book.div.find_all("a", class_="btn_type_dl")[0]["href"][2:]

            f.write(download_link)
            f.write(f"\n  dir=./pdf/{category_name}\n")
            f.write(f"  out={book_name}.pdf\n")
