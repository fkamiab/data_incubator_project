from statsmodels.compat.python import lrange, string_types, lzip, range
import numpy as np
from patsy import dmatrix

from statsmodels.regression.linear_model import OLS
from statsmodels.sandbox.regression.predstd import wls_prediction_std
from statsmodels.graphics import utils
from statsmodels.nonparametric.smoothers_lowess import lowess
from statsmodels.tools.tools import maybe_unwrap_results

def plot_fit(results, exog_idx, y_true=None, ax=None, **kwargs):
    """Plot fit against one regressor.

    This creates one graph with the scatterplot of observed values compared to
    fitted values.

    Parameters
    ----------
    results : result instance
        result instance with resid, model.endog and model.exog as attributes
    x_var : int or str
        Name or index of regressor in exog matrix.
    y_true : array_like
        (optional) If this is not None, then the array is added to the plot
    ax : Matplotlib AxesSubplot instance, optional
        If given, this subplot is used to plot in instead of a new figure being
        created.
    kwargs
        The keyword arguments are passed to the plot command for the fitted
        values points.

    Returns
    -------
    fig : Matplotlib figure instance
        If `ax` is None, the created figure.  Otherwise the figure to which
        `ax` is connected.

    Examples
    --------
    Load the Statewide Crime data set and perform linear regression with
    `poverty` and `hs_grad` as variables and `murder` as the response
plot
    >>> import statsmodels.api as sm
    >>> import matplotlib.pyplot as plt

    >>> data = sm.datasets.statecrime.load_pandas().data
    >>> murder = data['murder']
    >>> X = data[['poverty', 'hs_grad']]

    >>> X["constant"] = 1
    >>> y = murder
    >>> model = sm.OLS(y, X)
    >>> results = model.fit()

    Create a plot just for the variable 'Poverty':

    >>> fig, ax = plt.subplots()
    >>> fig = sm.graphics.plot_fit(results, 0, ax=ax)
    >>> ax.set_ylabel("Murder Rate")
    >>> ax.set_xlabel("Poverty Level")
    >>> ax.set_title("Linear Regression")

    >>> plt.show()

    .. plot:: plots/graphics_plot_fit_ex.py

    """

    fig, ax = utils.create_mpl_ax(ax)

    exog_name, exog_idx = utils.maybe_name_or_idx(exog_idx, results.model)
    results = maybe_unwrap_results(results)

    #maybe add option for wendog, wexog
    y = results.model.endog
    x1 = results.model.exog[:, exog_idx]
    x1_argsort = np.argsort(x1)
    y = y[x1_argsort]
    x1 = x1[x1_argsort]

    #ax.plot(x1, y, 'bo', label=results.model.endog_names)
    ax.plot(x1, y, 'bo', label='Data')
    if not y_true is None:
        ax.plot(x1, y_true[x1_argsort], 'b-', label='True values')
    title = 'Fitted values versus %s' % exog_name

    prstd, iv_l, iv_u = wls_prediction_std(results)
    #ax.plot(x1, results.fittedvalues[x1_argsort], 'D', color='r', label='fitted', **kwargs)

    ax.plot(x1, results.fittedvalues[x1_argsort], color='r', label='Linear Regression Fit', **kwargs)


    #ax.vlines(x1, iv_l[x1_argsort], iv_u[x1_argsort], linewidth=1, color='k', alpha=.7)
    #ax.fill_between(x1, iv_l[x1_argsort], iv_u[x1_argsort], alpha=0.1,
    #                    color='k')
    #ax.set_title(title)
    ax.set_xlabel(exog_name)
    ax.set_ylabel(results.model.endog_names)
    ax.legend(loc='best', numpoints=1)

    return fig
