from bs4 import BeautifulSoup

with open('empty.html','r') as html_file:          # open the file and read its content ,html_file is the variable
	content = html_file.read()
soup = BeautifulSoup(content,'lxml')

# ********************
#tags = soup.find_all('h5')  # find searches for the firt elemtn then it stop the execution to find all the tags use'find_all istead'
#for course_tags in tags :
	#print(course_tags.text) can be done ******

course_cards = soup.find_all('div',class_='card')
for course in course_cards:
	course_name = course.h5.text
	course_price = course.a.text.split()[-1] # -1 for last element
	print(course_name)
	print(course_price)
	print("*************************")
	print(f'{course_name} costs  {course_price}')
