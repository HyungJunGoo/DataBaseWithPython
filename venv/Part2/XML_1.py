# 메모리에서 XML의 XDM 트리 처리하기

import xml.etree.ElementTree as ET

# 파이썬 객체를 메모리에 로딩하여, XML 스트링 (XDM 트리)로 변환.

newDict = {
    'PLAYER' : [
        {'PLAYER_ID': '2007001', 'PLAYER_NAME': '정병지', 'TEAM_ID': 'K03', 'E_PLAYER_NAME': 'JOENG, BYUNGJI', 'NICKNAME': None, 'JOIN_YYYY': '2011', 'POSITION': 'GK', 'BACK_NO': 1, 'NATION':None, 'BIRTH_DATE': '1980-08-04', 'SOLAR': '1', 'HEIGHT': 184, 'WEIGHT': 77},
        {'PLAYER_ID': '2007020', 'PLAYER_NAME': '서동명', 'TEAM_ID': 'K01', 'E_PLAYER_NAME': 'SEO, DONGMYUNG', 'NICKNAME': None, 'JOIN_YYYY': '2012', 'POSITION': 'GK', 'BACK_NO': 1, 'NATION':None, 'BIRTH_DATE': '1984-03-05', 'SOLAR': '1', 'HEIGHT': 196, 'WEIGHT': 94},
        {'PLAYER_ID': '2007045', 'PLAYER_NAME': '김운재', 'TEAM_ID': 'K02', 'E_PLAYER_NAME': 'KIM, WOONJAE', 'NICKNAME': None, 'JOIN_YYYY': '2014', 'POSITION': 'GK', 'BACK_NO': 1, 'NATION':None, 'BIRTH_DATE': '1990-08-22', 'SOLAR': '1', 'HEIGHT': 188, 'WEIGHT': 79}
    ]
}

# XDM 트리 생성
tableName = list(newDict.keys())[0]  # PLAYER
tableRows = list(newDict.values())[0]

rootElement = ET.Element('Table')
rootElement.attrib['name'] = tableName

for row in tableRows:
    rowElement = ET.Element('Row')
    rootElement.append(rowElement)
    # rowElement = ET.SubElement(rootElement, 'Row'), 위의 두 분장과 동일

    for columnName in list(row.keys()):
        if row[columnName] == None:
            rowElement.attrib[columnName] = ''
        else:
            if type(row[columnName]) == int:
                rowElement.attrib[columnName] = str(row[columnName])
            else:
                rowElement.attrib[columnName] = row[columnName]

# XDM 트리를 콘솔에 출력

ET.dump(rootElement)
print()

#####################################################################################
# XML 스트링을 XDM 트리로 메모리에 로딩하여, 파이선 객체로 변환

xmlString = '''
    <Table name="PLAYER">
        <Row PLAYER_ID="2007001" PLAYER_NAME="정병지" TEAM_ID="K03" E_PLAYER_NAME="JOENG, BYUNGJI" NICKNAME="" JOIN_YYYY="2011" POSITION="GK" BACK_NO="1" NATION="" BIRTH_DATE="1980-08-04" SOLAR="1" HEIGHT="184" WEIGHT="77" />
        <Row PLAYER_ID="2007020" PLAYER_NAME="서동명" TEAM_ID="K01" E_PLAYER_NAME="SEO, DONGMYUNG" NICKNAME="" JOIN_YYYY="2012" POSITION="GK" BACK_NO="1" NATION="" BIRTH_DATE="1984-03-05" SOLAR="1" HEIGHT="196" WEIGHT="94" />
        <Row PLAYER_ID="2007045" PLAYER_NAME="김운재" TEAM_ID="K02" E_PLAYER_NAME="KIM, WOONJAE" NICKNAME="" JOIN_YYYY="2014" POSITION="GK" BACK_NO="1" NATION="" BIRTH_DATE="1990-08-22" SOLAR="1" HEIGHT="188" WEIGHT="79" />
    </Table>
'''

# XML 스트링을 XDM 트리로 메모리에 로딩
rootElement = ET.fromstring(xmlString)

# XDM 트리를 파이썬 객체로 변환
players = []
for childElement in rootElement:
    print(childElement.tag, childElement.attrib)
    players.append(childElement.attrib)

print()
print(players)
print()

newDict = {}
newDict[list(rootElement.attrib.values())[0]] = players
print((newDict))