from bs4 import BeautifulSoup
import urllib.request as req
import math
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
