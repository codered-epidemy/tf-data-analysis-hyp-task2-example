import pandas as pd
import numpy as np
from scipy.stats import anderson_

chat_id = 191207196 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.1
    return anderson_ksamp([x, y]).pvalue < alpha
