from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'http://icsd.kisti.re.kr/icsd/icsd_view1.jsp?num=6696&pg=0&opcode=1&keyword=Si+and+C+and+N+and+O&element_cnt1=&element_cnt2=&element=&element_sub1=&element_sub2=&element_ox1=&element_ox2='
html = urlopen(url) 
bsObj = BeautifulSoup(html, "html.parser")
main_news = bsObj.find("table")