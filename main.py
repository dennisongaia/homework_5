import en_core_web_lg
import csv
from newsapi import NewsApiClient

npl_eng = en_core_web_lg.load()
newsapi = NewsApiClient(api_key='8fdb404f32c545ce983ef4a4b542bbfd')

temp = newsapi.get_everything(q='coronavirus', language='en', from_param='2021-09-22',
                              to='2021-10-22', sort_by='relevancy')

with open('articles.csv', 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(len(temp['articles'])):
        csvwriter.writerow([temp['articles'][i]])
