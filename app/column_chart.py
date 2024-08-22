import read_csv
import charts

def run():
  labels = []
  values = []
  data = read_csv.read_csv('./app/data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  labels = list(map(lambda x: x['Country/Territory'], data))
  values = [float(item['World Population Percentage']) for item in data]
  print(labels)
  print(values)
  charts.generate_pie_chart(labels, values)
  
if __name__ == '__main__':
  run()