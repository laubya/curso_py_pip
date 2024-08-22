def get_population(country):
  print('Entró a buscar la población del país')
  country_population = {
    '1970': int(country['1970 Population']), 
    '1980': int(country['1980 Population']), 
    '1990': int(country['1990 Population']),
    '2000': int(country['2000 Population']),
    '2010': int(country['2010 Population']),
    '2015': int(country['2015 Population']),
    '2020': int(country['2020 Population']), 
    '2022': int(country['2022 Population']) 
  } 
  print(country_population)
  labels = list(country_population.keys())
  values = list(country_population.values())
  print(labels)
  print(values)
  return labels, values

def population_by_country(data, country):
  print('Entró a buscar el pais')
  result = list(filter(lambda i: i['Country/Territory'] == country, data))
  print(result)
  return result