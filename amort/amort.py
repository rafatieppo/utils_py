# =================================================================
#                                        Rafael Tieppo
#                                        rafaeltieppo@yahoo.com.br
#                                        2018-04-19
#  Cálculo Sistemas de Amortização SAC, PRICE
# =================================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

PV = 59675  # present value
n = 22     # months
i = 0.8    # interest month (%)

# ------------------------------------------------------------
# SAC SYSTEM
# ------------------------------------------------------------

# create matrix
matrixsac = np.zeros(shape=(n + 1, 5))
matrixsac
# Balance for period Zero
matrixsac[0, 4] = PV

# For the  periodo ZERO balance is equal PV
bal_sac = PV

# assign amort
amort_sac = PV / n

# SAC calculation - fill table
for s in range(1, n + 1, 1):
    int_sac = bal_sac * (i / 100)
    pay_sac = amort_sac + int_sac
    bal_sac = bal_sac - amort_sac
    matrixsac[s, 0] = s
    matrixsac[s, 1] = int_sac
    matrixsac[s, 2] = amort_sac
    matrixsac[s, 3] = pay_sac
    matrixsac[s, 4] = bal_sac

dfsac = pd.DataFrame(
    {"PERIOD": matrixsac[:, 0],
     "INTEREST": matrixsac[:, 1],
     "AMORTIZATION": matrixsac[:, 2],
     "PAYMENT": matrixsac[:, 3],
     "BALANCE": matrixsac[:, 4]})

dfsac.sum()
dfsac
# ------------------------------------------------------------
# PRICE SYSTEM
# ------------------------------------------------------------

# create matrix
matrixprice = np.zeros(shape=(n + 1, 5))
matrixprice
# Balance for period Zero
matrixprice[0, 4] = PV

# For the  periodo ZERO balance is equal PV
bal_price = PV
bal_price
# PAYMENT is constant
pay_price = (PV * i/100) / (1 - (1 / (1 + i/100)**n))
pay_price
# PRICE calculation - fill table
for s in range(1, n + 1, 1):
    int_price = bal_price * (i / 100)
    pay_price = pay_price
    amort_price = pay_price - int_price
    bal_price = bal_price - amort_price
    matrixprice[s, 0] = s
    matrixprice[s, 1] = int_price
    matrixprice[s, 2] = amort_price
    matrixprice[s, 3] = pay_price
    matrixprice[s, 4] = bal_price
    print(amort_price)


dfprice = pd.DataFrame(
    {"PERIOD": matrixprice[:, 0],
     "INTEREST": matrixprice[:, 1],
     "AMORTIZATION": matrixprice[:, 2],
     "PAYMENT": matrixprice[:, 3],
     "BALANCE": matrixprice[:, 4]})

print(dfprice)
dfprice.sum()
print(dfsac)
dfsac.sum()
