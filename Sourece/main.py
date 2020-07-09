from bs4 import BeautifulSoup
import urllib.request as req
from Get_Employment import getEmployment
from Get_Notice import getNotice
from analysis_notice import analysisNo
from analysis_employment import analysisEm

#공지사항 홈페이지에서 받기
getNotice()

#취업 정보 홈페이지에서 받기
getEmployment()

#공지사항 정보 예측 
analysisNo()

#취업 정보 예측
analysisEm()