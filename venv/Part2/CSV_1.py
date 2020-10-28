import csv

players = [
    ['2007001', '정병지', 'K03', 'JEONG, BYUNGJI', '', '2011', 'GK', '1', '', '1980-08-04', '1', '184', '77'],
    ['2007020', '서동명', 'K01', 'SEO, DONGMYUNG', '', '2012', 'GK', '21', '', '1984-04-05', '1', '196', '94'],
    ['2007035', '김운재', 'K02', 'KIM, WOONJAE', '', '', 'GK', '1', '', '1983-12-04', '1', '182', '82'],
    ['2007067', '정광수', 'K02', 'JEONG, GWANGSOO', '', '', 'GK', '41', '', '1987-10-03', '1', '182', '79'],
    ['2007106', '정이섭', 'K05', 'JEONG, ISUB', '쾌남', '2012', 'GK', '45', '', '1984-06-04', '1', '185', '78']
]

# CSV 파일에 쓰기

f = open('players.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)

for row in players: # wr.writerows(players)와 동일한 결과
    wr.writerow(row)

f.close()

# CSV 파일에서 읽기
f = open('players.csv', 'r', encoding='utf-8')
players = list(csv.reader(f))

for row in players:
    print(row)

print()

f.close()

##################################

# with open은 파일을 자동으로 닫아줌. 즉, close()가 필요 없다
with open('anotherPlayers.csv', 'w', encoding='utf-8', newline='') as f:
    wr = csv.writer(f)
    wr.writerows(players)

with open('anotherPlayers.csv', 'r', encoding='utf-8') as f:
    players = list(csv.reader(f))

for row in players:
    print(row)