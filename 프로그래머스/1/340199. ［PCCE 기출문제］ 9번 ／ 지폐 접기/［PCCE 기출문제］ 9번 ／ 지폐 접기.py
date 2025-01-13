def solution(wallet, bill):
    answer = 0
    wallet.sort(reverse=True)
    bill.sort(reverse=True)
    
    while wallet[0] < bill[0] or wallet[1] < bill[1]:
        bill[0] = bill[0] // 2
        bill.sort(reverse=True)
        answer += 1
    
    return answer