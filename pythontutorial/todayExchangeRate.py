%%writefile todayExchangeRate.py
#매직키, 항상 상단에 있어야 함 + wirtefile 파일로 만들어줌
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res,"html.parser")

results = soup.select("span.value")
print("달러 =",results[0].string+"원")
print("위안 =",results[3].string+"원")
print("유로 =",results[2].string+"원")

input("엔터를 누르면 종료합니다.")
