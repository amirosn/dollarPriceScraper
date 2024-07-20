import requests
import json
import pandas as pd
import math
#getting the total number of pages and saving the data of the first page to a dataFrame 
startIndex = 0
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0'}
searchLink = f'https://api.tgju.org/v1/market/indicator/summary-table-data/price_dollar_rl?lang=fa&order_dir=asc&order_dir=&draw=1&columns[0][data]=0&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=1&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=2&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=3&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=4&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=true&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=5&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=6&columns[6][name]=&columns[6][searchable]=true&columns[6][orderable]=true&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=7&columns[7][name]=&columns[7][searchable]=true&columns[7][orderable]=true&columns[7][search][value]=&columns[7][search][regex]=false&start={startIndex}&length=30&search=&order_col=&from=&to=&convert_to_ad=1&_=1719124946646'
searchText = requests.get(url=searchLink, headers=header).text
jason= json.loads(searchText)
totalPages = math.ceil(jason['recordsTotal']/30)
data = jason['data']
df = pd.DataFrame(data, columns =['بازگشایی','کمترین','بیشترین','پایانی','میزان تغییر','درصد تغییر','تاریخ میلادی','تاریخ شمسی'])
#saving the data to an excel file
for i in range(1,totalPages):
    searchLink = f'https://api.tgju.org/v1/market/indicator/summary-table-data/price_dollar_rl?lang=fa&order_dir=asc&order_dir=&draw=1&columns[0][data]=0&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=true&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=1&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=true&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=2&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=true&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=3&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=true&columns[3][search][value]=&columns[3][search][regex]=false&columns[4][data]=4&columns[4][name]=&columns[4][searchable]=true&columns[4][orderable]=true&columns[4][search][value]=&columns[4][search][regex]=false&columns[5][data]=5&columns[5][name]=&columns[5][searchable]=true&columns[5][orderable]=true&columns[5][search][value]=&columns[5][search][regex]=false&columns[6][data]=6&columns[6][name]=&columns[6][searchable]=true&columns[6][orderable]=true&columns[6][search][value]=&columns[6][search][regex]=false&columns[7][data]=7&columns[7][name]=&columns[7][searchable]=true&columns[7][orderable]=true&columns[7][search][value]=&columns[7][search][regex]=false&start={i*30}&length=30&search=&order_col=&from=&to=&convert_to_ad=1&_=1719124946646'
    searchText = requests.get(url=searchLink, headers=header).text
    jason= json.loads(searchText)
    data = jason['data']
    df2 = pd.DataFrame(data, columns =['بازگشایی','کمترین','بیشترین','پایانی','میزان تغییر','درصد تغییر','تاریخ میلادی','تاریخ شمسی'])
    df = pd.concat([df,df2], axis=0, ignore_index=True)
df.to_excel(f'C:/Users/Amir/Desktop/tgju/dollarPricess.xlsx', sheet_name='Sheet')
