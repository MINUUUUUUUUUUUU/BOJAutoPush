def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    for city in cities:
        
        if city.upper() in cache:
            cache.remove(city.upper())
            cache.append(city.upper())
            answer += 1
        
        # 캐시 안에 값이 없으면
        if city.upper() not in cache:
            cache.append(city.upper())
            answer += 5
            
        # 캐시 사이즈 초과시 첫번째 값 제외  
        if len(cache) > cacheSize:
            cache.pop(0)
        
        
    return answer