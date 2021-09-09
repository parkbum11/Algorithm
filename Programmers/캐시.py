def solution(cacheSize, cities):
    answer = 0
    cache = []
    for city in cities:
        city = city.upper()
        if city not in cache:
            if len(cache) >= cacheSize:
                cache.append(city)
                cache.pop(0)
            else:
                cache.append(city)
            answer += 5
        else:
            answer += 1
            index = cache.index(city)
            cache.pop(index)
            cache.append(city)
    print(answer)
    return answer


def solution(cacheSize, cities):
    import collections
    cache = collections.deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time
solution(5, ["SEOUL", "SEOUL", "SEOUL"])