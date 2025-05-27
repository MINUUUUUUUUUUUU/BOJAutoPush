import math

def solution(fees, records):
    answer = []
    d_time, d_fee, u_time, u_fee = fees
    in_car = []
    out_car = []
    
    
    car_dic = dict()
    
    for r in records:
        a, b, c = r.split()
        if c == "IN":
            in_car.append([int(b), list(map(int,a.split(":")))]) # 차번호, 입차시간 순
        elif c == "OUT":
            out_car.append([int(b), list(map(int,a.split(":")))]) # 차번호, 입차시간 순
    in_car.sort()
    out_car.sort()
    
    for car in in_car:
        car_num = car[0]
        if car_num not in car_dic:
            car_dic[car_num] = 0
        # print(car_dic)
        in_time = car[1]
        l = len(out_car)
        tmp = -1
        for i in range(l):
            if out_car[i][0] == car_num:
                tmp = i
                break
        if tmp != -1:
            out_time = out_car[i][1]
            out_car = out_car[:i] + out_car[i+1:]
            
            parking_time = (out_time[0] - in_time[0]) * 60 + out_time[1] - in_time[1]
        else:
            parking_time = (23 - in_time[0]) * 60 + 59 - in_time[1]
        # print(parking_time)
        
        car_dic[car_num] += parking_time
            
            
    # print(car_dic)
    total_parking_time = sorted(car_dic.items())
    for t in total_parking_time:
        if t[1] <= d_time:
            answer.append(d_fee)
        else:
            tmp_t = t[1] - d_time
            tmp_fee = d_fee + math.ceil(tmp_t / u_time) * u_fee
            answer.append(tmp_fee)
            
    return answer