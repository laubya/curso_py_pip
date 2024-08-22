import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('./app/data.csv')
  country = input('Type Country => ')
  
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)

#con este if solucionamos el problema de dualidad, de que se ejecuten todas las funciones al importar el modulo, pero que si se ejecute si se está llamando al archivo principal del modulo desde la terminal
if __name__ == '__main__':
  run()