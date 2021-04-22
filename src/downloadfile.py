import requests

url = 'https://automatetheboringstuff.com/files/rj.txt'

reponse = requests.get(url=url)

print("Status Code: " + str(reponse.status_code))

file = open('data/romeonjuliet.txt', 'wb')

for chunk in reponse.iter_content(100000):
    file.write(chunk)

file.close()
