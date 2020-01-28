from bs4 import BeautifulSoup
from requests import get

headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

web_md = 'https://www.webmd.com/drugs/2/search?type=drugs&query=acyclovir'
response = get(web_md, headers=headers) # gets the html of the search result
soup = BeautifulSoup(response.text, 'lxml')

for a in soup.find_all('a', text='acyclovir', href=True):
    print("Found the URL:", a['href'])
    found_drug = 'https://www.webmd.com' + a['href']
    print('found drug url: ', found_drug)


# Found the URL: /drugs/2/drug-941-9069/acyclovir/details