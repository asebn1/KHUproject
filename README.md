## KHUproject
Kyunghee University Computer Engineering Notice and Employment Information Analysis Program


1. 주제 선정 이유
텀 프로젝트 주제는 경희대학교 컴퓨터공학과 공지사항 및 취업 정보 분석이다. 경희대학교 학부 학생들은 학교의 공지사항 및 취업 정보를 알고 싶다. 공지사항이 경희톡으로 오기도 하지만 보편화한 지 얼마 되지 않았다. 또한, 알고 싶은 정보가 오지 않을 때도 많기 때문에 직접 찾아보아야 한다. 내가 궁금한 기업의 취업 정보가 언제 전달될지와 공지사항에서는 내가 궁금한 공지사항이 언제 공지될지 예상할 수 있도록 한다. 이전 2015년부터 현재까지의 공지사항 및 취업 정보를 바탕으로 정보를 분석하여 언제 공지되는지 예상할 수 있다.


2.가설 정의
2015년부터 2019년까지 매년 9월마다 가을 프로그래밍 경시대회가 공지된다고 가정하자. 그렇다면, 2020년 9월에도 가을 프로그래밍 경시대회가 공지된다는 것을 유추할 수 있다. 이처럼 주기적으로 공지되는 타이틀 정보를 저장하여 분석한다. 분석된 자료를 통해 앞으로 공지될 공지사항 및 취업 정보를 예측할 수 있다.


3.인터넷을 통한 데이터 획득
경희대학교 SW융합대학 - 컴퓨터공학과 - 공지사항
공지사항은 등록일을 기준으로 하며 번호와 공지 제목이 있다. 등록일과 공지 제목을 통해 달마다 어떤 내용이 공지되는지 분석하여 확인할 수 있다.

경희대학교 SW융합대학 - 컴퓨터공학과 - 취업
취업 정보는 등록일을 기준으로 하며 번호와 제목이 있다. 등록일과 제목을 통해 달마다 어떤 기업의 취업 정보가 공지되는지 분석하여 확인할 수 있다.


파이썬 크롤링을 통해 정보를 csv 파일 형식으로 저장한다. 이후 csv파일을 토대로 내용을 분석한다.

4.분석을 위한 데이터의 가공
<데이터를 수집하고 분석하기 위한 사전 작업>

beautifulSoup4를 설치 (pip install beautifulSoup4)
url을 통해 file을 open하기 위한 urllib 설치 (pip install urllib)
크롤링 데이터를 csv 파일로 저장
1. 공지사항의 정보들을 추출한다. 번호, 제목, 등록일자를 추출한다.
▲ 페이지를 count하여 페이지 끝까지 정보 추출

▲ 공지사항 정보 추출 코드

def getNotice():

#총 페이지
count = 42

#홍페이지 주소. 페이지 마다 count 해주어 게시판 글 모두 긁어옴
baseurl = 'http://ce.khu.ac.kr/index.php?pg=' + str(count) + '&page=list&hCode=BOARD&bo_idx=2&sfl=&stx='
res = req.urlopen(baseurl)
soup = BeautifulSoup(res, 'html.parser')

# 호환되도록 버퍼 -1과 utf8 적용
f = open('Notice.csv', 'a', -1, "utf-8")

#페이지가 끝날때까지 반복
while(1):
    baseurl = 'http://ce.khu.ac.kr/index.php?pg=' + str(count) + '&page=list&hCode=BOARD&bo_idx=2&sfl=&stx='
    res = req.urlopen(baseurl)
    soup = BeautifulSoup(res, 'html.parser')

    if count == 42:

        #마지막 페이지일 때 게시글 수가 20개가 아니므로
        for i in range(12, 1, -1):
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
        for i in range(21, 1, -1):
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


2. 취업정보란의 정보들을 추출한다. 번호, 제목, 등록일자를 추출한다.
▲ 페이지를 count하여 페이지 끝까지 정보 추출

▲ 취업정보란의 정보 추출 코드

#홈페이지에서 크롤링으로 값 받아오기 def getEmployment():

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

3. 크롤링을 통해 저장된 csv의 정보를 활용하여 앞으로 나올 공지사항과 취업정보를 예상한다.
예시)
1-1) 2016년부터 2019년까지 매년 9월 혹은 10월에 KHU 가을 프로그래밍 경시대회 안내가 나오는 것을 확인한다.
1-2) 2020년에도 9월 혹은 10월에 KHU 가을 프로그래밍 경시대회가 나올 수 있음을 예상할 수 있다.

2-1) 2015년부터 2019년까지 매년 4월 삼성 취업설명회 안내가 나오는 것을 취업정보란을 통해 확인한다.
2-2) 2020년에도 4월에 삼성 취업설명회 안내가 나올 수 있음을 예상할 수 있다.

4. 앞선 과정을 통해 얻은 데이터를 이용하여 앞으로 나올 공지사항 혹은 취업 정보를 예상한다.
[3]의 과정을 통해 경희대학교 컴퓨터공학과와 취업정보란을 통해 앞으로 나올 정보를 예상할 수 있다.
구한 csv 파일의 [제목]란을 통해 알아보고자 하는 정보를 string형식으로 입력해 정보를 찾는다.

또한, 검색된 결과에서 등록일을 확인한다. 등록일 사이에 얼만큼의 주기를 가지고 규칙이 있는지 확인한다.
만약 규칙이 있다면, 다음 2020년 이후에도 같은 주기로 비슷한 내용의 공지가 올라올 수 있음을 예상한다.

5. 분석 결과 도출
컴퓨터공학과의 공지사항이 시작된 2015-06-30 부터 2020-05-30까지를 기준으로 공지사항 내용이 수집되었다.
컴퓨터공학과 취업정보란 시작된 2015-06-30 부터 2020-05-30까지를 기준으로 취업정보가 수집되었다.

1) Notice : 공지사항
2) Employment : 취업정보

2) 획득 데이터 csv는 다음과 같이 저장된다.
[공지사항] notice.csv 파일로 저장

번호, 제목, 등록일
1 2015-1학기 졸업능력인증 신청접수 안내 2015-06-30
2 [LINC+] 2015학년도 1학기 경희대학교 창업동아리 2015-07-18
3 [LINC+] Microsoft Learning Program(MLP) 교육과정 2015-07-18
4 [중요] 전자정보대학관내 마스크 필수 착용 협조 2015-07-20
5 [중요] 이태원 클럽 방문 내/ 외국인 검역 협조 2015-08-15
6 2015-1학기 국제 생활관(우정원, 제2기숙사) 입사 2015-08-17

.
.
.


-공지사항 예시-


-취업정보 예시-



1) 공지사항 분석
1) 공지사항을 분석한다.
궁금한 공지 내용(ex. 프로그래밍)을 검색하면 그 공지가 언제를 주기로 공지되는지를 확인한다.

2) 분석 내용을 가공한다.
주기 확인 후 사용자에게 2020년을 기준으로 공지될것이라 예상되는 날짜를 제공한다.

1)과 2)를 각기 구현한 코드는 다음과 같다.

def analysisNo():

#기존 공지사항의 월 저장
list = []
#도출된 예상될 공지사항 월 저장
list2 = []
f = open('Notice.csv', 'r', -1, 'utf8')
i = 0
sch = input("예측할 공지사항 명을 입력하세요 : ")
count = 0
while(i<900):
    i += 1
    temp = f.readline()
    if sch in temp:
        count += 1
        #뒤에서 부터 검색 : ,의 인덱스 반환함
        idx = temp.rfind(',')
        list.append(temp[idx+6:idx+8])

sum=0
if count == 0:
    print("검색된 결과가 없습니다.")   
    return 0
else:
    if (len(list) < 5):
        print("적은 정보로 예상할 수 없습니다.")
    else:
        for i in range(0, len(list)-1):
            sum += abs(int(list[i+1]) - int(list[i]))
        #반올림 
        prediction = round(sum/(len(list)-1))
        num = int(list[len(list)-1])
        while(1):
            num += prediction
            if num > 17 and num <= 24:
                # 2019년 기준 자료를 2020년으로 바꿔줌 
                list2.append('2020-'+str(num-12))
            elif num>24:
                break

        print("앞으로 나올것으로 예측될 '"+ sch + "' 관련 공지사항은 다음과 같은 날짜로 예상됩니다.")
    print(list2)
2) 취업정보 분석
1) 취업정보를 분석한다.
궁금한 취업 정보(ex. 삼성)를 검색하면 그 공지가 언제를 주기로 공지되는지를 확인한다.

2) 분석 내용을 가공한다.
주기 확인 후 사용자에게 2020년을 기준으로 공지될것이라 예상되는 날짜를 제공한다.

1)과 2)를 각기 구현한 코드는 다음과 같다.

def analysisEm():

#기존 취업정보의 월 저장
list = []
#도출된 예상될 공지사항 월 저장
list2 = []
f = open('Employment.csv', 'r', -1, 'utf8')
i = 0
sch = input("예측할 취업정보 명을 입력하세요 : ")
count = 0

#현재 약 300개의 취업정보이므로 적당한 400
while(i<400):
    i += 1
    temp = f.readline()
    if sch in temp:
        count += 1
        #뒤에서 부터 검색 : ,의 인덱스 반환함
        idx = temp.rfind(',')
        list.append(temp[idx+6:idx+8])

sum=0
if count == 0:
    print("검색된 결과가 없습니다.")   
    return 0
else:
    if (len(list) < 5):
        print("적은 정보로 예상할 수 없습니다.")
    else:
        for i in range(0, len(list)-1):
            sum += abs(int(list[i+1]) - int(list[i]))
        #반올림 
        prediction = round(sum/(len(list)-1))
        num = int(list[len(list)-1])
        while(1):
            num += prediction
            if num > 17 and num <= 24:
                # 2019년 기준 자료를 2020년으로 바꿔줌 
                list2.append('2020-'+str(num-12))
            elif num>24:
                break

        print("앞으로 나올것으로 예측될 '"+ sch + "' 관련 공지사항은 다음과 같은 날짜로 예상됩니다.")
    print(list2)
6. 데이터 분석 결과 및 결론
▲ 경희대학교 컴퓨터공학과의 공지사항 및 취업 정보 데이터를 추출하고 가공한다. 정보를 분석하여 앞으로 공지될 공지사항 및 취업 정보를 예측하고 달마다 공지되는 양을 파악한다.

1) 공지사항
예측할 공지사항 명을 입력하세요 : 가을 프로그래밍
앞으로 나올것으로 예측 된 '가을 프로그래밍' 관련 공지사항은 다음과 같은 날짜로 예상됩니다.
['2020-09']


2) 취업 정보
예측할 취업정보 명을 입력하세요 : 삼성
앞으로 나올것으로 예측 된 '삼성' 관련 공지사항은 다음과 같은 날짜로 예상됩니다.
['2020-06', '2020-08', '2020-10', '2020-12']


기존 2015-2019년 사이에 쌓인 데이터를 기준으로 앞으로 공지될 공지날짜를 예측하여 결과값으로 나타낸다.
7. 참고문헌 및 자료
경희대학교 컴퓨터공학과 공지사항:http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=2
경희대학교 컴퓨터공학과 취업정보:http://ce.khu.ac.kr/index.php?hCode=BOARD&bo_idx=3
BeautifulSoup를 활용: https://freeharmony.tistory.com/64
