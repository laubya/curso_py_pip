import utils
import read_csv
import charts
import pandas as pd

def run():
  '''
  #De esta manera se lee el csv sin la librería pandas 
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda i: i['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''
  df = pd.read_csv('data.csv')
  continent = input('Type Continent => ')
  df = df[df['Continent']== continent]

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  print(countries)
  print(percentages)
  charts.generate_pie_chart(continent, countries, percentages)

  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

#con este if solucionamos el problema de dualidad, de que se ejecuten todas las funciones al importar el modulo, pero que si se ejecute si se está llamando al archivo principal del modulo desde la terminal
if __name__ == '__main__':
  run()