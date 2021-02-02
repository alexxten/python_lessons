import requests
from bs4 import BeautifulSoup

response = requests.get(
    url=(
        'https://kartaslov.ru/%D1%86%D0%B8%D1%82%D0%B0%D1%82%D1%8B-%D0%B8%D0%B7-%'
        'D1%80%D1%83%D1%81%D1%81%D0%BA%D0%BE%D0%B9-%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D'
        '0%B8%D0%BA%D0%B8/%D1%81%D0%BE-%D1%81%D0%BB%D0%BE%D0%B2%D0%BE%D0%BC/%D1%82%D1%8E%D0%BB%D'
        '0%B5%D0%BD%D1%8C'
    ),
)

html_doc = response.text

soup = BeautifulSoup(html_doc, 'html.parser')
quotations_div = soup.find_all('div', attrs={'class': 'v2-sentence-box'})
qsource_div = soup.find_all('div', attrs={'class': 'v2-sentence-source'})

result = []
for q, s in zip(quotations_div, qsource_div):
    result.append(q.text.replace(s.text, ''))

# f = open('quotations.txt', 'w')
# f.writelines(result)
# f.close()

# контекстный менеджер
with open('quotations.txt', 'w') as f:
    f.writelines(result)

with open('quotations.txt', 'r') as f:
    text_from_file = f.read()
    text_from_file_ = f.readlines()

print(type(text_from_file))
print(type(text_from_file_))




