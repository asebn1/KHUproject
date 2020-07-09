from bs4 import BeautifulSoup
import urllib.request as req
from start_Employment import startEmployment

#시작 부분 함수
startEmployment()

#홈페이지에서 크롤링으로 값 받아오기
def getEmployment():

    #총 페이지
    count = 17

    #홍페이지 주소. 페이지 마다 count 해주어 게시판 글 모두 긁어옴
    baseurl = 'http://ce.khu.ac.kr/index.php?pg=' + str(count) + '&page=list&hCode=BOARD&bo_idx=3&sfl=&stx='
    res = req.urlopen(baseurl)
    soup = BeautifulSoup(res, 'html.parser')
    
    # 호환되도록 버퍼 -1과 utf8 적용
    f = open('Employment.csv', 'a', -1, "utf-8")
    
    #페이지가 끝날때까지 반복
    while(1):
        baseurl = 'http://ce.khu.ac.kr/index.php?pg=' + str(count) + '&page=list&hCode=BOARD&bo_idx=3&sfl=&stx='
        res = req.urlopen(baseurl)
        soup = BeautifulSoup(res, 'html.parser')
        
        #마지막 페이지일 때 게시글 수가 20개가 아니므로
        if count == 17:
            for i in range(19, 0, -1):
                #번호 삽입
                temp1 = '#board_list >tbody > tr:nth-child(' + str(i) + ') > td:nth-child(1)'
                noticeNum = soup.select(temp1)[0].text
                #제목 삽입
                temp2 = '#board_list > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(2) > a'
                noticeText = soup.select(temp2)[0].text
                #등록일 삽입
                temp3 = '#board_list > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(5)'
                noticeym = soup.select(temp3)[0].text
                print(noticeNum + ',' + noticeText  + ',' + noticeym)
                f.write(noticeNum + ',' + noticeText  + ',' + noticeym + '\n')
   
        else :
            #기본 페이지와 같은 수일때 적용
            for i in range(20, 0, -1):
                #번호 삽입
                temp1 = '#board_list >tbody > tr:nth-child(' + str(i) + ') > td:nth-child(1)'
                noticeNum = soup.select(temp1)[0].text
                #제목 삽입
                temp2 = '#board_list > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(2) > a'
                noticeText = soup.select(temp2)[0].text
                noticeText = noticeText.replace(',','')
                
                #등록일 삽입
                temp3 = '#board_list > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(5)'
                noticeym = soup.select(temp3)[0].text
                print(noticeNum + ',' + noticeText  + ',' + noticeym)
                f.write(noticeNum + ',' + noticeText  + ',' + noticeym + '\n')
        count -= 1
       
        #게시물 끝 도달시 종료
        if count == 0:
            break