import requests
from bs4 import  BeautifulSoup as bs
import pandas as pd
import json
import time,random
from fake_useragent import UserAgent 


ua = UserAgent()

headers = {
    'User-Agent': ua.random
}

url_all=[]
for page in range(1,50):
                  
    url_python = f'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=15&asc=0&page={page}&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1'
    response_python = requests.get(url_python, headers=headers)
    soup_python = bs(response_python.text,'lxml')
    for n in range(len(soup_python.find_all('a',class_='js-job-link'))):
        url=soup_python.find_all('a',class_='js-job-link')[n].get('href').replace('//','')
        url_all.append(url)
    time.sleep(random.uniform(1,3))
print(len(url_all))

# 去除重複id
job_id_raw=[i.split('/')[2][0:5] for i in url_all]
job_ids=list(set(job_id_raw))
print(len(job_ids))


cookies_job = cookies = {
    'luauid': '1964508915',
    '__auc': '2ffd5851181f67ab01429b62000',
    '_hp2_id.3192618648': '%7B%22userId%22%3A%222613995236300847%22%2C%22pageviewId%22%3A%225034120837818358%22%2C%22sessionId%22%3A%22522628905601960%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D',
    '_ga_TTXLT7SQ8E': 'GS1.1.1670983084.3.0.1670983086.58.0.0',
    '_ga_5VZ9E4NXCM': 'GS1.1.1670983084.2.0.1670983086.0.0.0',
    '_ga_WYQPBGBV8Z': 'GS1.1.1673319073.4.1.1673319085.48.0.0',
    '_hjSessionUser_1597014': 'eyJpZCI6ImQ1Nzk3ZmU5LTM4OWUtNTQ4Ni04ZTk0LTM1NWIyNDEyM2U4OSIsImNyZWF0ZWQiOjE2NzY1MTYzMDQ3MDEsImV4aXN0aW5nIjpmYWxzZX0=',
    '_ga_D4915X27HH': 'GS1.1.1676516304.3.1.1676516378.0.0.0',
    'dtCookie': 'v_4_srv_1_sn_FF799C56ACC0BE963DE6FA059AA66E4B_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_0',
    'job_same_ab': '1',
    '_gcl_au': '1.1.270214325.1681636417',
    '_gid': 'GA1.3.1618553978.1681636418',
    '_ga': 'GA1.4.945879444.1657697642',
    'c_job_algo_exp_poc': 'A',
    'c_job_algo_exp_date_poc': 'E',
    '_clck': 'hmi8wo|1|fau|0',
    '_clsk': 'zahcwy|1681694781818|1|1|u.clarity.ms/collect',
    '_hjSessionUser_642678': 'eyJpZCI6ImNlZjhhMjllLWU4MDItNWQzZC04MGE2LWZjMjIwOGU2MzZlNiIsImNyZWF0ZWQiOjE2ODE2OTUzMDc4ODAsImV4aXN0aW5nIjpmYWxzZX0=',
    '_hjMinimizedPolls': '829535',
    '_hjDonePolls': '829535%2C829535',
    'TS016ab800': '01180e452d680d2784aefbfddd8d9af9b7dd0d79fdb5747d928c22ab61d927be8f5932a590835fb82a6ac0f9f104befec1ee0e663031029f08f2db209a0b882909e95a9bdc30b124599df7059b36e600c9a1995f9b3aaeff0f86ba54108f730964921663c0',
    '_dc_gtm_UA-15276226-1': '1',
    'c_job_view_job_info_nabi': '7xykm%2C2007001004',
    '_ga': 'GA1.1.945879444.1657697642',
    'lup': '1964508915.4623532291991.5035849152215.1.4640712161167',
    'lunp': '5035849152215',
    '_ga_WYQPBGBV8Z': 'GS1.4.1681694777.6.1.1681698007.44.0.0',
    '_ga_FJWMQR9J2K': 'GS1.1.1681694777.9.1.1681698007.44.0.0',
    '_ga_W9X1GB1SVR': 'GS1.1.1681694777.9.1.1681698007.44.0.0',
}


rs = requests.Session()
data_all=[]
for job_id in job_ids:
    headers_job = headers = {
    'Connection': 'keep-alive',
    'Referer': f'https://www.104.com.tw/job/{job_id}?jobsource=jolist_a_relevance',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    }
    
    url_job = f'https://www.104.com.tw/job/ajax/content/{job_id}'
    response_job = rs.get(url_job, cookies=cookies_job, headers=headers_job)
    data = response_job.json()
    data_all.append(data)
time.sleep(random.uniform(1,5))

print(len(data_all))


job_id = [i['data']['header']['analysisUrl'].split('/')[-1] for i in data_all]
jobname = [i['data']['header']['jobName'] for i in data_all]
date_ = [i['data']['header']['appearDate'] for i in data_all]
edu = [i['data']['condition']['edu'] for i in data_all]
department = [','.join(i['data']['condition'] ['major']) for i in data_all]
companyname = [i['data']['header']['custName'] for i in data_all]
salary = [i['data']['jobDetail']['salary'] for i in data_all]
region = [i['data']['jobDetail']['addressRegion'][0:3] for i in data_all]
skills = [','.join([b['description'] for b in i['data']['condition']['specialty']]) for i in data_all]
job_description = [i['data']['jobDetail']['jobDescription'].replace('\n','').replace('\n1','').replace('\n2','').replace('\n3','').replace('\n4','').replace("'","").replace('\r4','').replace('\r2','') for i in data_all]
welfare = [i['data']['welfare']['welfare'].replace('\n','').replace('\r','').replace('\u3000','').replace('\t','').replace("'","") for i in data_all]

salaryannual = []
for i in data_all:
    salary_min=i['data']['jobDetail']['salaryMin']
    if salary_min < 24000:
        salaryannual.append('0')
    elif salary_min>=24000 and salary_min<=200000:
        salaryannual.append(salary_min * 14)
    else:
        salaryannual.append(salary_min)

df_jobs ={}
df_jobs['job_id']=job_id
df_jobs['jobname']=jobname
df_jobs['date_']=date_
df_jobs['edu']=edu
df_jobs['department']=department
df_jobs['companyname']=companyname
df_jobs['salary']=salary
df_jobs['region']=region
df_jobs['skills']=skills
df_jobs['job_description']=job_description
df_jobs['welfare']=welfare
df_jobs['salaryannual']=salaryannual


df_pythonjobs = pd.DataFrame(df_jobs)
df_pythonjobs.to_csv("job_all.csv",encoding='utf-8', index=False)