from bs4 import BeautifulSoup
 
import time
import requests

print(" put some skills you are not familier with")

unfamilier_skill= input('>')
print(f'Filtering out {unfamilier_skill}')

def find_jobs():
	html_text= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
	soup =BeautifulSoup(html_text,'lxml')
	print("**********************************")
	jobs = soup.find_all('li',class_= 'clearfix job-bx wht-shd-bx') # incase the website has many pages , only contents of first page will be displayed which has this class

	for job in jobs:
		job_company = job.find('h3', class_='joblist-comp-name')
		published_days= job.find('span',class_="sim-posted")
		if 'few' in published_days.text:
			skills =  job.find('span', class_="srp-skills")
			more_info = job.header.h2.a['href']
			if unfamilier_skill not in skills.text :
				with open('jobss.txt','w') as file_jobss:
					file_jobss.write(skills.text)
					file_jobss.write(published_days.text)
					file_jobss.write(job_company.text.replace(" ",""))
					file_jobss.write(more_info)

if __name__ == '__main__':
	while True :
		find_jobs()
		time_wait =  10
		print(f'Waiting {time_wait} minutes')
		time.sleep(time_wait*60)


