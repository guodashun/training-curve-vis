# Training-Curve-Vis

Visualize the training curve from the *.csv file *(tensorboard format)*.

## Feature

- Custom labels
- Curve smoothing
- Support for multiple curves

##### Single curve

| tensorboard                                                  | ours                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="./imgs/single_tb.png" alt="single_tb" style="zoom:33%;" /> | <img src="./imgs/single_sns.png" alt="single_sns" style="zoom: 45%;" /> |

##### Multiple curves
| tensorboard                                                  | ours                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| <img src="./imgs/multi_tb.png" alt="multi_tb" style="zoom:33%;" /> | <img src="./imgs/multi_sns.png" alt="multi_sns" style="zoom: 45%;" /> |

## Usage

```bash
$ pip install -r requirements.txt
```

And then,

```python
from curve_vis import CurveVis
cv = CurveVis(
	csv_file = ["a.csv", "b.csv"]
    labels = ["curve1", "curve2"]
)
cv.show()
```

