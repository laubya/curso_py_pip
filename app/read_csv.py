import csv

def read_csv(path):
  print('Se está ejecuntando read csv')
  with open(path) as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      countries = {key: value for key, value in iterable}
      data.append(countries)
    return data



#El filtro no me sirve porque se que todos los items contienen la clave que voy a buscar

#El map me sirve, puedo crear una funcion que extraiga los valores que quiero 



if __name__ == '__main__':
  data = csv_read('data.csv')
  print(data)
  