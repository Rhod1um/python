import requests
from bs4 import BeautifulSoup

url = "https://www.jobindex.dk/jobsoegning/it/storkoebenhavn"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

results = soup.find_all('div', class_="PaidJob")

for result in results:
    company = result.find('div', class_="jix-toolbar-top__company")
    link_company = result.find_all("a")[0]["href"]
    title = result.find('h4')
    location = result.find('span', class_="jix_robotjob--area")
    #btn btn-sm btn-secondary
    link_apply = result.find_all("a", class_="btn btn-sm btn-secondary")[0]["href"]
    #btn-list__element d-none d-md-inline
    link_see_job = result.find_all("a")[0]["href"]
    print(company.text)
    print(link_company)
    print(title.text)
    print(location)
    print(link_see_job)


