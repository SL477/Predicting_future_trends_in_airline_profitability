from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV


def gridSearchSVR(X: pd.DataFrame, y: pd.Series) -> None:
    """Run grid search on the SVR data to get the best parameters

    Parameters
    ----------
    X:pd.DataFrame : the training data

    y:pd.Series : the labelled data

    Returns
    -------
    None
    """

    # Grid search parameters
    params = {
        'svr__kernel': ['linear'],  # , 'poly', 'rbf', 'sigmoid']
        'svr__gamma': ['scale'],  # , 'auto']
        'svr__tol': [0.001],  # [0.0001, 0.001, 0.01, 0.1],
        # 'svr__C': [0.01],
        # [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1],
        'svr__epsilon': [0.3],
        # [0.01, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1],
        # 'svr__shrinking': [True], # [True, False],
    }

    # Make pipeline
    pipeSVR = Pipeline([
        ('scaler', StandardScaler()),
        ('svr', SVR())
    ])

    # make gridsearch
    gs = GridSearchCV(pipeSVR, params)

    gs.fit(X, y)

    print(gs.best_score_)
    print(gs.best_params_)
