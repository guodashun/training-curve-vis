import math
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame

class CurveVis():
    def __init__(
        self, 
        csv_file, 
        x_label  = 'step(s)', 
        y_label  = 'loss',
        labels   = ['curve1'],
        smooth_k = 5
    ) -> None:
        self.x_label = x_label
        self.y_label = y_label
        self.smooth_k = smooth_k
        
        if isinstance(csv_file, str):
            csv_file = [csv_file]
        assert len(csv_file) == len(labels), f"Invalid num of labels: {len(csv_file)} for csv_files but {len(labels)} for labels"

        for i in range(len(csv_file)):
            data = self._load_training_data(csv_file[i])[:238]
            data = self._smooth_data(data, self.smooth_k)
            data = self._index_data(data)
            self._add_curve(data, labels[i])


    def _load_training_data(self, csv_file):
        return pd.read_csv(csv_file)["Value"].to_numpy()
        
        
    def _load_some_other_data():
        # TODO
        pass
        
    @staticmethod
    def _smooth_data(data, k=5):
        raw_data = data.copy()
        sz = len(raw_data)

        # padding
        for i in range(int(k/2)):
            raw_data = np.insert(raw_data, 0, raw_data[0])
            raw_data = np.insert(raw_data, -1, raw_data[-1])
        sm_data = []
        # for i in range(k-1, sz):
        #     sm_data_i = []
        #     for j in range(k-1, -1, -1):
        #         sm_data_i.append(raw_data[i-j])
        #     sm_data.append(sm_data_i)
        for i in range(int(k/2), sz+int(k/2)):
            sm_data_i = []
            for j in range(-int(k/2), int(k/2)):
                sm_data_i.append(raw_data[i+j])
            sm_data.append(sm_data_i)
        return np.array(sm_data)

    @staticmethod
    def _index_data(data):
        sz = len(data)
        id_data = []
        for i in range(sz):
            for j in data[i]:
                id_data.append([i, j])
        return id_data

    def _add_curve(self, raw_data, curve_label):
        data = DataFrame(raw_data, columns=['x', 'y'])
        ax = sns.lineplot(x='x', y='y', linestyle='solid', linewidth=2, markersize=6, data=data, label=curve_label)

    def show(self):
        plt.xlabel(self.x_label, fontsize=14)
        plt.ylabel(self.y_label, fontsize=14)
        plt.show()
