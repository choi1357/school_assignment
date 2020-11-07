import sys

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
        print('1. 기본값으로 조회하기(옵션:기본, 나이:전체)\n2. 옵션을 선택하여 조화하기\n3. 종료')
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
    print('날짜 입력(예:2020-01-01 13:10:00) : ', end='')
    optionDate, optionTime = f.readline().strip().split()   
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
    return age

def RequestData(optionDate, optionTime, optionIssue, optionEvent, optionCurrent, optionEnter, optionSports, age):
    # 준비중 (request 영역)
    print('준비중인 기능')

def main():
    ReadOption()

main()
