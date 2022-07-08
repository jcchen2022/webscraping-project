import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/Johnny\Desktop/chromedriver_win32/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
driver.quit()

for a in soup.findAll(attrs='css-ytumd6 e1kk1ckf0'):
    name = a.find('h5')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='css-u5vyh2 e15x7lld2'):
    date = b.find('p')
    if date not in results:
        other_results.append(date.text)

df = pd.DataFrame({'Names': results, 'Dates': other_results})
df.to_csv('names.csv', index=False, encoding='utf=8')