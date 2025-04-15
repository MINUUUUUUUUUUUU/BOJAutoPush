from itertools import product

discount = []
data = [10,20,30,40]

def dfs(temp, depth):
        if depth == len(temp):
            discount.append(temp[:])
            return
        for d in data:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d

def solution(users, emoticons):
    answer = []
    
    dfs([0] * len(emoticons), 0)
    
    max_users_cnt = 0
    max_sales = 0
    
    for i in range(len(discount)):
        temp_users_cnt = 0
        temp_sales = 0
        
        for user in users:
            temp_amount = 0
            for j in range(len(emoticons)):
                if discount[i][j] >= user[0]:
                    temp_amount += emoticons[j] * ((100 - discount[i][j]) / 100)
                if temp_amount >= user[1]:
                    temp_users_cnt += 1
                    break
                if j == len(emoticons) - 1:
                    temp_sales += temp_amount
        
        if temp_users_cnt >= max_users_cnt:
            if temp_users_cnt == max_users_cnt:
                if temp_sales > max_sales:
                    max_sales = temp_sales
            elif temp_users_cnt > max_users_cnt:
                max_users_cnt = temp_users_cnt
                max_sales = temp_sales

            
    answer.append(max_users_cnt)
    answer.append(max_sales)
    return answer