import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    
    answer = []
    today_dt = datetime.datetime.strptime(today, '%Y.%m.%d')
    
    for i in terms:
        a, b = i.split() #a는 약관이름 #b는 약관유효달수
        
        t = 0
        while t < len(privacies):
            c, d = privacies[t].split()
            c_dt = datetime.datetime.strptime(c, '%Y.%m.%d')
            if d == a:
                #현재 날짜가 개인정보 수집일자 + 유효기간보다 크다면 파기
                if today_dt >= c_dt + relativedelta(months=int(b)):
                    answer.append(t+1)
            t += 1
    answer.sort()
    return answer