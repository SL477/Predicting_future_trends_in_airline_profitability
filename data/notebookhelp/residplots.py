import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import pandas as pd


def residual_plots(y_true: pd.Series, y_pred: pd.Series) -> None:
    """This is to make graphs of the residuals

    Parameters
    ----------
    y_true:pd.Series : the original labels

    y_pred:pd.Series : the predicted labels

    Returns
    -------
    None
    """
    print('RMSE', mean_squared_error(y_true, y_pred, squared=False))
    # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html

    residuals = y_true - y_pred

    # Plot hist of residuals
    plt.hist(residuals)
    plt.title('Histograms of residuals')
    plt.xlabel('Error Bins')
    plt.ylabel('Count')
    plt.show()

    # plot true against predicted
    plt.scatter(y_true, y_pred)

    # Work out min and max for the straight line
    minx, maxx = min(y_true), max(y_true)
    miny, maxy = min(y_pred), max(y_pred)

    minn = min(minx, miny)
    maxn = max(maxx, maxy)

    plt.plot([minn, maxn], [minn, maxn])
    plt.title("True against predicted")
    plt.xlabel("True")
    plt.ylabel("Predicted")
    plt.show()
