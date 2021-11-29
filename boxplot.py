import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class BoxPlot:
    def __init__(
        self,
        title,
        x_label,
        y_label,
    ):
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.data = pd.DataFrame()
    

    def add_data(self, data, label):
        self.data[label] = data

    def show(self):
        sns.boxplot(data=self.data)
        plt.title(self.title)
        plt.xlabel(self.x_label)
        plt.ylabel(self.y_label)
        plt.show()

