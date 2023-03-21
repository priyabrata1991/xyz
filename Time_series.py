import numpy as np
from statsmodels.tsa.arima.model import ARIMA
def ARMA_Hyp(a):
#    try:
        MD=MD=ARIMA(a[-1],order=(a[:3]))
        result=MD.fit()
        return result.aic
#    except:
#        return np.nan

