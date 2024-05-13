from bs4 import BeautifulSoup
import requests as rq
from lxml import etree
import pandas as pd
from openpyxl import load_workbook

#Khoi tao ban dau
url = 'http://giavang.doji.vn/'
response = rq.get(url)
html_content = response.text

#Phan tich HTML
soup = BeautifulSoup(html_content, "html.parser")
tree = etree.HTML(str(soup))
gold_data = []
time = tree.xpath(f"/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div[3]/p/span")
gold_data.append(time[0].text)
for i in range(6):
    # data_name = tree.xpath(f"/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div[3]/table/tbody/tr[{i+1}]/td[1]/span[1]")
    data_buy = tree.xpath(f"/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div[3]/table/tbody/tr[{i+1}]/td[2]/div")
    data_sell = tree.xpath(f"/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div[3]/table/tbody/tr[{i+1}]/td[3]/div")
    # gold_data.append(data_name[0].text)
    gold_data.append(data_buy[0].text)
    gold_data.append(data_sell[0].text)
gold_data = pd.DataFrame([gold_data])
data = pd.read_excel("D:/data/gold_price.xlsx", index_col=None, header=None)
update_data = pd.concat([data, gold_data])
update_data.to_excel("D:/data/gold_price.xlsx", header=False, index=False)