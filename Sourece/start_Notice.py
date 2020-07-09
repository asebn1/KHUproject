from bs4 import BeautifulSoup
import urllib.request as req

#시작 부분 csv에서 번호 / 제목 / 등록일 넣어줌
def startNotice():
    start = "번호, 제목, 등록일\n"
    f = open('Notice.csv', 'w', -1, "utf-8")
    f.write(start)
    f.close()