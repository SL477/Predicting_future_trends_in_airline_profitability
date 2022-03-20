import pandas as pd
import matplotlib.pyplot as plt
from yellowbrick.cluster import SilhouetteVisualizer
from sklearn.cluster import KMeans


def clustering(num_clusters: int, suppressOutput: bool, df: pd.DataFrame, subset:list) -> float:
    """This creates an interactive altair graph after using kmeans to cluster up
    the price of fuel, PC1 and PC2
    Bravely this modifies the dataframe in memory

    Parameters
    ----------
    num_clusters:int : number of clusters to use

    suppressOutput:bool : show output or not

    df:pd.DataFrame : The dataframe to use and modify

    subset:list : A subset of the dataframe's columns to pass to the cluster

    Returns
    -------
    float
        Silhoute Score

    """
    # using https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html

    kmeans = KMeans(n_clusters=num_clusters, random_state=42)

    # using https://www.scikit-yb.org/en/latest/api/cluster/silhouette.html
    # I changed to using the silhouette visualiser from yellowbrick's library to get
    vis = SilhouetteVisualizer(kmeans, colors='yellowbrick')
    vis.fit(df[subset])

    df['cluster'] = kmeans.labels_

    # Plot PCA1 against price, as PC1 explains 85% of the variation, colour by the cluster
    if suppressOutput:
        plt.clf()
        # clear the silhouette plot from matplotlib's library
        # so that it doesn't mess up the next function
    return vis.silhouette_score_
