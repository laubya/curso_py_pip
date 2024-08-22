import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.show()
  plt.savefig('bar_chart.png')  # Guardar el gráfico en lugar de mostrarlo

def generate_pie_chart(labels, values):
  print('Entró a generar la graficación')
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()
  plt.savefig('bar_chart.png')  # Guardar el gráfico en lugar de mostrarlo

if __name__ == '__main__':
  labels = ['a', 'b', 'c', 'd', 'e']
  values = [10, 20, 80, 70, 95]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)

