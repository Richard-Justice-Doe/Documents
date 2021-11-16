import statistics

months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN',
 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
year = 2020
temperatureList = []

for month in months:
 if month in ['JAN', 'MAR', 'MAY', 'JUL', 'AUG', 'OCT', 'DEC']:
 length = 31
 elif month in ['APR', 'JUN', 'SEP', 'NOV']:
 length = 30
 else:
 if year // 4 == 0:
 length = 29
 else:
 length == 28

 for day in range(1, length + 1):
 print('DATE:', month, day)
 while True:
 try:
 temperature = float(input('Enter noon temperature: '))
 temperatureList.append(temperature)
 break
 except ValueError:
 print('Invalid input. Try again...')

print()

temperatureList.sort()
lowestTemperature = temperatureList[0]
highestTemperature = temperatureList[-1]
averageTemperature = statistics.mean(temperatureList)

print('Lowest Temperature:', lowestTemperature)
print('Highest Temperature:', highestTemperature)
print('Average Temperature:', averageTemperature)