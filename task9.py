weather = {
    'city': 'Москва',
    'temperature': 20
}
print(weather)
print(weather['city'])

weather['temperature'] = weather['temperature'] - 5
print(weather)

print(weather.get('country'))
print(weather.get('country', 'Россия'))

weather['name'] = '27.05.2019'
print(weather)
print(len(weather))