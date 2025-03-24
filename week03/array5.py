def duplicate(city):
    result = list()
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2: # 문자열 길이 비교 ( 중복값 확인 )
                result.append(city)

    return result


cities = ['Incheon', 'Incheon', 'Incheon', 'Seoul', 'Seoul', 'Suwon']

cities.append('Gimpo')
cities.append('Seoul')

print(cities)
print(set(duplicate(cities)))
