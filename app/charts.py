import matplotlib.pyplot as plt


def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}bar_chart.png')  # Guardar el gráfico en lugar de mostrarlo
  plt.close()

def generate_pie_chart(name, labels, values):
  print('Generando pie chart')
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.savefig(f'./imgs/{name}_pie_chart.png')  # Guardar el gráfico en lugar de mostrarlo
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c', 'd', 'e']
  values = [10, 20, 80, 70, 95]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)

