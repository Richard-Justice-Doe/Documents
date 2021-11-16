import matplotlib.pyplot as plt
from datetime import datetime, date, time

from numpy.distutils.fcompiler import none


class PlotGraph:
    input_values = []
    date_values = []

    # def _init_(self):
    #     self.date_values: []
    #     self.input_values: []

    def plot_a_graph(self):
        input_ans = input('How many values do you want to input? ')
        for index in range(int(input_ans)):
            values = input('Enter input value %s: ' % (index + 1))
            now = datetime.now()
            self.input_values.append(values)
            self.date_values.append(now)
        plt.plot(self.date_values, self.input_values)
        plt.xlabel('Date-time axis')
        plt.ylabel('values-axis')
        plt.show()
        print(self.date_values)


my_graph = PlotGraph()
my_graph.plot_a_graph()