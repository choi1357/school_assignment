import sys # 입력 받기 기능을 위해 추가
import datetime # 날짜 비교, 오늘 날짜 구하기를 위해 추가
import requests # Web Data를 읽어오기 위해 추가 (Naver DataLab)
import webbrowser # 브라우저를 호출하기 위해 추가

def ReadOption(): # 첫번째 선택지 기능 호출
    f = sys.stdin
    while (True):
        print('┌────────────────────────┐\n│Naver 급상승 검색어 조회│\n└────────────────────────┘')
        print('1. 기본값으로 조회하기(옵션:기본, 나이:전체)\n2. 옵션을 선택하여 조회하기\n3. 종료')
        print('입력 : ', end='')
    
        selectNo = f.readline().strip() # 입력한 선택지를 읽어옴
        if (selectNo == '1'): #1일 경우, 날짜만 입력 받는 함수 호출
            ReadOptionFirst()
        elif (selectNo == '2'): #2일 경우, 날짜 및 모든 option을 입력 받는 함수 호출
            ReadOptionSecond()
        elif (selectNo == '3'): # 3일 경우, While문을 탈출하여 프로그램 종료
            break
        else: # 1~3 중에 없으면, 에러 메시지 노출
            print('존재하지 않는 선택지입니다.\n')

def ReadOptionFirst(): # 날짜만 입력 받고, option은 기본값으로 설정하여 requests 함수 호출
    optionDate, optionTime = InputDate() # 날짜, 시간
    RequestData(optionDate, optionTime, '0', '0', '0', '0', '0', 'all') # option을 0으로 입력하여 Requests 호출
  
def ReadOptionSecond(): # 날짜 및 모든 option을 입력 받은 후, requests 호출
    optionDate, optionTime = InputDate() # 날짜, 시간
    optionIssue = InputIssueLevel() # 이슈별 묶어보기 Level
    optionEvent = InputEventLevel() # 이벤트·할인 Level
    optionCurrent = InputCurrentLevel() # 시사 Level
    optionEnter = InputEnterLevel() # 엔터 Level
    optionSports = InputSportsLevel() # 스포츠 Level
    age = Inputage() # 나이대
    RequestData(optionDate, optionTime, optionIssue, optionEvent, optionCurrent, optionEnter, optionSports, age) # Requests 호출

def InputDate(): # 날짜 입력
    f = sys.stdin
    while (True):
        try:
            print('날짜 입력(예:2020-01-17 00:00) : ', end='')
            optionDate, optionTime = f.readline().strip().split() # 날짜와 시간을 입력 받음 (띄어쓰기로 구분)
            if (datetime.datetime.strptime(optionDate,'%Y-%m-%d') < datetime.datetime.strptime('2020-01-17','%Y-%m-%d')): # 입력 받은 날짜가 2020-01-17 이전인지 체크
                print('2020-01-17 이전으로 조회할 수 없습니다\n')
            else:
                optionFullDate = optionDate + ' ' + optionTime # 날짜 비교를 위해 하나의 텍스트로 병합 (날짜 + 시간)
                if (datetime.datetime.strptime(optionFullDate,'%Y-%m-%d %H:%M') > datetime.datetime.strptime(datetime.datetime.today().strftime('%Y-%m-%d %H:%M'),'%Y-%m-%d %H:%M')): # 입력 받은 날짜가 현재 날짜보다 미래인지 체크
                    print('미래의 시간은 조회할 수 없습니다.\n')
                else: # 어디에도 해당되지 않는다면, While문 종료
                    break
        except ValueError: # 예외처리 : 입력 받은 날짜의 형식이 올바르지 않은 경우 (반드시 0000-00-00 00:00 형태로 입력 받아야 함)
            print('날짜 형식이 올바르지 않습니다.\n')

    return optionDate, optionTime # 날짜와 시간 반환

def InputIssueLevel(): # '이슈별 묶어보기' option > Level 설정
    f = sys.stdin
    while (True):
        print('이슈별 묶어보기 Level(0~4) : ', end='')
        optionIssue = f.readline().strip() # Level 입력 받음
        if (optionIssue.isdecimal()): # 0 이상의 정수인지 체크
            if (int(optionIssue) >= 0 and int(optionIssue) <= 4): # 0~4 중에서 입력했다면, While문 종료
                break
            else:
                print('0 ~ 4만 입력할 수 있습니다.\n')
        else:
            print('0 ~ 4만 입력할 수 있습니다.\n')
        
    return optionIssue # '이슈별 묶어보기' Level 반환

def InputEventLevel(): # '이벤트·할인' option > Level 설정
    f = sys.stdin
    while (True):
        print('이벤트·할인 Level(0~4) : ', end='')
        optionEvent = f.readline().strip() # Level 입력 받음
        if (optionEvent.isdecimal()): # 0 이상의 정수인지 체크
            if (int(optionEvent) >= 0 and int(optionEvent) <= 4): # 0~4 중에서 입력했다면, While문 종료
                break
            else:
                print('0 ~ 4만 입력할 수 있습니다.\n')
        else:
            print('0 ~ 4만 입력할 수 있습니다.\n')        

    return optionEvent # '이벤트·할인' Level 반환

def InputCurrentLevel(): # '시사' option > Level 설정
    f = sys.stdin
    while (True):
        print('시사 Level(0~4) : ', end='')
        optionCurrent = f.readline().strip() # Level 입력 받음
        if (optionCurrent.isdecimal()): # 0 이상의 정수인지 체크
            if (int(optionCurrent) >= 0 and int(optionCurrent) <= 4): # 0~4 중에서 입력했다면, While문 종료
                break
            else:
                print('0 ~ 4만 입력할 수 있습니다.\n')
        else:
            print('0 ~ 4만 입력할 수 있습니다.\n')        
        
    return optionCurrent # '시사' Level 반환

def InputEnterLevel(): # '엔터' option > Level 설정
    f = sys.stdin
    while (True):
        print('엔터 Level(0~4) : ', end='')
        optionEnter = f.readline().strip() # Level 입력 받음
        if (optionEnter.isdecimal()): # 0 이상의 정수인지 체크
            if (int(optionEnter) >= 0 and int(optionEnter) <= 4): # 0~4 중에서 입력했다면, While문 종료
                break
            else:
                print('0 ~ 4만 입력할 수 있습니다.\n')
        else:
            print('0 ~ 4만 입력할 수 있습니다.\n')        
                
    return optionEnter # '엔터' Level 반환

def InputSportsLevel(): # '스포츠' option > Level 설정
    f = sys.stdin
    while(True):
        print('스포츠 Level(0~4) : ', end='')
        optionSports = f.readline().strip() # Level 입력 받음
        if (optionSports.isdecimal()): # 0 이상의 정수인지 체크
            if (int(optionSports) >= 0 and int(optionSports) <= 4): # 0~4 중에서 입력했다면, While문 종료
                break
            else:
                print('0 ~ 4만 입력할 수 있습니다.\n')
        else:
            print('0 ~ 4만 입력할 수 있습니다.\n')        
                       
    return optionSports # '스포츠' Level 반환

def Inputage(): # 나이대 입력
    f = sys.stdin
    while(True):
        print('나이대(10, 20, 30, 40, 50, all) : ', end='')
        age = f.readline().strip() # 나이대를 입력 받음
        if (age == '10' or age == '20' or age == '30' or age == '40' or age =='50' or age == 'all'): # 10,20,30,40,50,all 중에서 입력했을 경우에만 While문 종료
            break
        else:
            print('10, 20, 30, 40, 50, all 중에서 입력해야 합니다.\n')

    if (age != 'all'): # 나이대가 숫자인 경우, 뒤에 s 붙임 (requests에서 파라미터가 원하는 값을 만들기 위해)
        age = age + 's'
    return age # 나이 반환

def RequestData(optionDate, optionTime, optionIssue, optionEvent, optionCurrent, optionEnter, optionSports, age): # Requests 호출
    params = { # Requests 파라미터
        'datetime': optionDate + "T" + optionTime + ':00', # 날짜 + 시간 (0000-00-00T00:00:00)
        'groupingLevel': optionIssue, # '이슈별 묶어보기' Level (0 ~ 4)
        'marketing': int(optionEvent) - 2, # '이벤트·할인' Level (-2 ~ 2)
        'news': int(optionCurrent) - 2, # '시사' Level (-2 ~ 2)
        'entertainment': int(optionEnter) - 2, # '엔터' Level (-2 ~ 2)
        'sports': int(optionSports) - 2, # '스포츠' Level (-2 ~ 2)
        'age': age # 나이
    }

    headers = { # Requests 헤더
        'referer': 'https://datalab.naver.com/keyword/realtimeList.naver', # referer = 크롬에서 뽑아 낸 값
        'user-agent': 'chrome' # user-agent = 크롬
    }

    url = 'https://datalab.naver.com/keyword/realtimeList.naver' # 네이버 DataLab > 급상승 검색어 URL

    try:
        res = requests.get(url,params=params,headers=headers) # GET, Requests 호출
        if (res.status_code == 200): # 성공했을 경우 (status_code 200 = 성공)
            PrintResult(res.text) 
        else:
            print('웹에서 응답하지 않습니다.(status_code : ' + str(res.status_code))
    except requests.ConnectionError: # 예외처리 : 네트워크 연결 여부 체크
        print('네트워크가 연결되어 있지 않습니다.')

def SplitRankData(requestsText, rank): # 읽어온 requestsText를 기반으로 Split 작업
    splitdata = requestsText.split('<span class=\"item_num\">' + str(rank) + '</span>')[1] # '<span class=\"item_num\">'을 기준으로 뒤 Text
    splitdata = splitdata.split('<span class=\"item_title\">')[1] # '<span class=\"item_title\">'을 기준으로 뒤 Text
    splitdata = splitdata.split('</span>')[0] # '</span>' 기준으로 앞 Text
    return splitdata # Split으로 뽑아 낸 키워드 반환

def PrintResult(requestsText): # 급상승 검색어 읽어오기
    rankdata = {}
    try:
        requestsText = requestsText.split('<div class=\"ranking_box\">')[1] # 1차적으로 requestsText를 반토막 냄 (SplitRankData 처리 효율을 향상시키기 위해 Text Size 줄임)
        print('────────────────────────────────────────────────────────────────────────')
        for i in range(1, 21): # 1부터 20까지 급상승 검색어의 키워드 추출
            rankdata[i] = SplitRankData(requestsText,i)
            if (rankdata[i] != '-'): # 해당 순위에 키워드가 있다면 출력
                print(str(i) + '. ' + rankdata[i])
        print('────────────────────────────────────────────────────────────────────────')
        AfterOption(rankdata) 
    except IndexError: # 예외처리 : Split 작업이 불가능한 requestsText인지 체크 (PC 시간을 조작하여 미래 시간을 입력하는 경우 방지)
        print('데이터를 불러올 수 없습니다. 날짜를 확인해주세요.')

def AfterOption(rankdata): # 2번째 선택지 기능 호출
    f = sys.stdin
    while (True):
        print('1. 네이버에서 검색하기\n2. 처음으로 돌아가기\n입력 : ',end='')
        selectNo = f.readline().strip() # 선택지를 입력 받음
        if (selectNo == '1'): # 1인 경우, 순위 검색 호출
            Search(rankdata)
            break
        elif (selectNo == '2'): # 2인 경우, 처음 화면으로 돌아감 (첫번째 선택지 기능)
            break
        else: # 1~2가 아니라면, 에러 메시지 노출
            print('존재하지 않는 선택지입니다.\n')

def Search(rankdata): # 순위 검색
    f = sys.stdin
    while (True):
        print('검색할 순위(0 : 처음으로 돌아가기) : ',end='')
        rank = f.readline().strip() # 순위를 입력 받음

        if (rank.isdecimal()): # 순위가 0 이상의 정수인 경우
            if (rank == '0'): # 0을 입력했다면, 처음 화면으로 돌아감
                break
            OpenBrowser(int(rank), rankdata) # 브라우저 열기 호출
        else:
            print('존재하지 않는 순위입니다. 0이상의 숫자만 입력해주세요.\n')

def OpenBrowser(rank, rankdata): # 브라우저 열기
    if (rank > 0 and rank < 21): # 입력 받은 순위가 1 ~ 20에 포함되는지 체크
        if (rankdata[rank] != '-'): # 해당 순위에 키워드가 있는 경우
            webbrowser.open('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=' + rankdata[rank]) # 해당 순위의 키워드를 네이버 검색 화면에서 호출 (브라우저 열기)
        else:
            print('해당 순위에 검색어가 존재하지 않습니다.\n')
    else:
        print('존재하지 않는 순위입니다.(입력 가능 : 1 ~ 20)\n')

def main(): # 메인 함수
    ReadOption()

main() # 프로그램 시작
