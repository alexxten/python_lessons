import requests
from collections import Counter

response = requests.get('https://jsonplaceholder.typicode.com/comments')
comments = response.json()

emails = [i['email'] for i in comments]
# то же, что и строка выше
# email_list = []
# for i in comments:
#     email_list.append(i['email'])

domain_zones = [i.split('.')[-1] for i in emails]
print('Доменные зоны: ', set(domain_zones))
print('Наиболее частая доменная зона', Counter(domain_zones).most_common()[0])

# Не используя Counter
frequency = {dz: domain_zones.count(dz) for dz in set(domain_zones)}
# то же, что и строка выше
# frequency = {}
# for i in set(domain_zones):
#     frequency[i] = domain_zones.count(i)

most_common = sorted(frequency.items(), key=lambda x: x[1])[-1]
print('Наиболее частая доменная зона', most_common)