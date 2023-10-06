# Establish Machine Learning Model note

_Writed by Vialon17, 01-30-2023_

**General Progress for modelling:**

Understand Data -> Import Data -> EDA(Explore Data Analysis) -> Model -> Evaluation -> Prediction -> Deployment 

----
## Play with Data

### Check Data

The first thing is making ur data visualization,

Classification

Encoding Data

Normalization

Null-value check

Regularization

```python
    df_extra[y_col].value_counts(normalize=True).map("{:.2%}".format).to_frame();
    df_full[unknown_features].describe(percentiles=[.01, .05, .25, .50, .75, .95, .99]);
```

**[Kernel Density Estimation](https://zh.m.wikipedia.org/wiki/%E6%A0%B8%E5%AF%86%E5%BA%A6%E4%BC%B0%E8%AE%A1)**

_In statistics, kernel density estimation (KDE) is the application of kernel smoothing for probability density estimation. <space>--Wiki_
In other words, KDE is used to establish density model for unknown data.
```python
    import seaborn as sns
    import pandas as pd
    data = pd.read_csv('data.csv', index_col = 'id') # we assume there have a data file.
    sns.kdeplot(x = data['day'])
```

```python
    # matplotlib: hide useless data axises.
    for ax in axes.flatten():
    if not ax.get_xlabel():
        ax.set_visible(False)
```

```python
    #about subplots 
    fig, axes = plt.subplots(rows, cols, figsize=(16, 5))
    for col, ax in zip(['Time', 'Amount'], axes):
    sns.histplot(data=df_full,
                 x=col,
                 hue='origin',
                 ax=ax,
                 bins=60)
    plt.tight_layout()
```

matplotlib style available
`ply.style.available` -> list:
['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8', 'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette', 'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook', 'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk', 'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10']

When use `subplots` and `axs. flatten()` in plot seaborn grid, should set parameter `ax` -> `sns.kdeplot(or_x, fill = True, label = 'original', ax = ax)`

Duplicates: We should drop duplicates as this will cause our model to overfit and give us overinflated scores as it will 'learn' the one duplicate and perfectly predict the other.

[Fight with overfitting](https://medium.com/geekculture/how-to-stop-overfitting-your-ml-and-deep-learning-models-bb8324ace80b)
* more data;
* ensemble learning;
* cross validation;
* early stoping(_deep learning_);
* principal component analysis;
* regularization;



Overfitting: The train score will be much larger than the validation score. There will be significant overfitting if the train score is close to 1 (i.e the model has over learnt the training data)
    Solution: Reduce overfitting such as implementing regularization, add data, feature engineering etc

Underfitting: If validation score is much lower than training. i.e there is a significant gap
    Solution: Hyperparameter tuning and feature engineering (quickly improvements would increase the number of epochs and lower learning rate)

```python
    import pandas as pd 
    import numpy as np 
    import matplotlib.pyplot as plt
    import seaborn as sns 
    from sklearn.metrics import log_loss, cohen_kappa_score
    from sklearn.model_selection import train_test_split
    from sklearn.model_selection import KFold, RepeatedStratifiedKFold,StratifiedKFold
    from scipy.stats import boxcox, median_abs_deviation
    from sklearn.preprocessing import StandardScaler, RobustScaler, QuantileTransformer
    from sklearn.feature_selection import VarianceThreshold, mutual_info_classif, RFECV, SelectKBest
    from sklearn.decomposition import PCA

    import shap 
    import lightgbm as lgb
    import catboost as cat
    import xgboost as xgb
    from sklearn.linear_model import RidgeClassifier, LogisticRegression
    from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
    from sklearn.svm import SVC
    from imblearn.over_sampling import SMOTE
```

```python
    model = RandomForestRegressor(n_estimators=300, min_samples_leaf=30, random_state=1)
    model.fit(train[original_features], train[target])

    features_for_pdp = original_features
    fig, axs = plt.subplots(2, 4, figsize=(12, 5))
    plt.suptitle('Partial Dependence', y=1.0)
    PartialDependenceDisplay.from_estimator(model, train[original_features],
                                            features_for_pdp,
                                            pd_line_kw={"color": "red"},
                                            ice_lines_kw={"color": "blue"},
                                            kind='both',
                                            ax=axs.ravel()[:len(features_for_pdp)])
    plt.tight_layout(h_pad=0.3, w_pad=0.5)
    plt.show()
```
In your example, when you call a(2), the function a is executed with temp1=2 and temp2=3 (since temp2 has a default value of 3). Therefore, the output will be 5.

However, when you subsequently call b(temp2=5), you are essentially trying to pass the argument temp2 twice - once as a default value in the original call to a, and once as an explicit keyword argument in the call to b. This will result in a TypeError, since you cannot pass the same argument twice.

If you want to change the value of temp2 when calling b, you can modify the function a to accept keyword arguments using **kwargs, like this:

```python
    def a(temp1, temp2=3, **kwargs):
        if 'temp2' in kwargs:
            temp2 = kwargs['temp2']
        print(temp1 + temp2)       
    b = a(2)
    b(temp2=5)
```
In this modified version of a, the function checks if the keyword argument temp2 was passed, and if so, it overrides the default value of temp2. When you call b(temp2=5) now, the output will be 7, since temp2 is set to 5.