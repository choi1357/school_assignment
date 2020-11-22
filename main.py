import sys
import datetime
import requests
import webbrowser

"""
검색에 필요한 옵션

optionDate
optionTime
optionIssue
optionEvent
optionCurrent
optionEnter
optionSports
age
"""

def ReadOption():
    f = sys.stdin
    while (True):
        print('┌────────────────────────┐\n│Naver 급상승 검색어 조회│\n└────────────────────────┘')
        print('1. 기본값으로 조회하기(옵션:기본, 나이:전체)\n2. 옵션을 선택하여 조회하기\n3. 종료')
        print('입력 : ', end='')
    
        selectNo = f.readline().strip()
        if (selectNo == '1'):
            ReadOptionFirst()
        elif (selectNo == '2'):
            ReadOptionSecond()
        elif (selectNo == '3'):
            break
        else:
            print('존재하지 않는 선택지입니다.\n')

def ReadOptionFirst():
    optionDate, optionTime = InputDate()
    RequestData(optionDate, optionTime, '0', '0', '0', '0', '0', 'all')
  
def ReadOptionSecond():
    optionDate, optionTime = InputDate()
    optionIssue = InputIssueLevel()
    optionEvent = InputEventLevel()
    optionCurrent = InputCurrentLevel()
    optionEnter = InputEnterLevel()
    optionSports = InputSportsLevel()
    age = Inputage()
    RequestData(optionDate, optionTime, optionIssue, optionEvent, optionCurrent, optionEnter, optionSports, age)

def InputDate():
    f = sys.stdin
    while (True):
        print('날짜 입력(예:2020-01-17 13:10) : ', end='')
        optionDate, optionTime = f.readline().strip().split()
        if (datetime.datetime.strptime(optionDate,'%Y-%m-%d') < datetime.datetime.strptime('2020-01-17','%Y-%m-%d')):
            print('2020-01-17 이전으로 조회할 수 없습니다')
        else:
            break
    return optionDate, optionTime 

def InputIssueLevel():
    f = sys.stdin
    print('이슈별 묶어보기 Level(0~4) : ', end='')
    optionIssue = f.readline().strip()
    return optionIssue

def InputEventLevel():
    f = sys.stdin
    print('이벤트·할인 Level(0~4) : ', end='')
    optionEvent = f.readline().strip()
    return optionEvent

def InputCurrentLevel():
    f = sys.stdin
    print('시사 Level(0~4) : ', end='')
    optionCurrent = f.readline().strip()
    return optionCurrent

def InputEnterLevel():
    f = sys.stdin
    print('엔터 Level(0~4) : ', end='')
    optionEnter = f.readline().strip()
    return optionEnter

def InputSportsLevel():
    f = sys.stdin
    print('스포츠 Level(0~4) : ', end='')
    optionSports = f.readline().strip()
    return optionSports

def Inputage():
    f = sys.stdin
    print('나이대(10, 20, 30, 40, 50, all) : ', end='')
    age = f.readline().strip()
    if (age != 'all'):
        age = age + 's'
    return age

def RequestData(optionDate, optionTime, optionIssue, optionEvent, optionCurrent, optionEnter, optionSports, age):
    params = { 
        'datetime': optionDate + "T" + optionTime + ':00',
        'groupingLevel': optionIssue,
        'marketing': int(optionEvent) - 2,
        'news': int(optionCurrent) - 2,
        'entertainment': int(optionEnter) - 2,
        'sports': int(optionSports) - 2,
        'age': age
    }

    headers = {
        'referer': 'https://datalab.naver.com/keyword/realtimeList.naver',
        'user-agent': 'chrome'
    }

    url = 'https://datalab.naver.com/keyword/realtimeList.naver'
    res = requests.get(url,params=params,headers=headers)
    PrintResult(res.text)  

def SplitRankData(requestsText, rank):
    splitdata = requestsText.split('<span class=\"item_num\">' + str(rank) + '</span>')[1]
    splitdata = splitdata.split('<span class=\"item_title\">')[1]
    splitdata = splitdata.split('</span>')[0]
    return splitdata

def PrintResult(requestsText):
    rankdata = {}
    requestsText = requestsText.split('<div class=\"ranking_box\">')[1]
    print('────────────────────────────────────────────────────────────────────────')
    for i in range(1, 21):
        rankdata[i] = SplitRankData(requestsText,i)
        if (rankdata[i] != '-'):
            print(str(i) + '. ' + rankdata[i])
    print('────────────────────────────────────────────────────────────────────────')
    AfterOption(rankdata)

def AfterOption(rankdata):
    f = sys.stdin
    while (True):
        print('1. 네이버에서 검색하기\n2. 처음으로 돌아가기\n입력 : ',end='')
        selectNo = f.readline().strip()
        if (selectNo == '1'):
            Search(rankdata)
            break
        elif (selectNo == '2'):
            break
        else:
            print('존재하지 않는 선택지입니다.\n')

def Search(rankdata):
    f = sys.stdin
    while (True):
        print('검색할 순위(0 : 처음으로 돌아가기) : ',end='')
        rank = f.readline().strip()

        if (rank.isdecimal()):
            if (rank == '0'):
                break
            OpenBrowser(int(rank), rankdata)
        else:
            print('존재하지 않는 순위입니다. 0이상의 숫자만 입력해주세요.\n')

def OpenBrowser(rank, rankdata):
    if (rank > 0 and rank < 21):
        if (rankdata[rank] != '-'):
            webbrowser.open('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=' + rankdata[rank])
        else:
            print('해당 순위에 검색어가 존재하지 않습니다.\n')
    else:
        print('존재하지 않는 순위입니다.(입력 가능 : 1 ~ 20)\n')

def main():
    ReadOption()

main()
