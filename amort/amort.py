"""SAC PRICE amortization system."""

import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
from matplotlib import style
style.available
style.use('bmh')

def amort(PV, n, i):
    """
    Return a summarize from SAC and PRICE system.

    Keyword arguments:
    PV is present value.
    n is the number of payments.
    i is the interest by month.
    """
    # SAC SYSTEM
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

    # PRICE SYSTEM
    matrixprice = np.zeros(shape=(n + 1, 5))
    # Balance for period Zero
    matrixprice[0, 4] = PV

    # For the  periodo ZERO balance is equal PV
    bal_price = PV
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

    # print output
    heads = ['INTEREST', 'AMORTIZATION', 'PAYMENT']
    print('\n----- PRICE ------------------------')
    b = [np.sum(matrixprice[:, 1:4], axis=0)]
    print(tabulate(b, headers=heads, tablefmt='markdown'))
    a = [np.sum(matrixsac[:, 1:4], axis=0)]
    print('\n----- SAC --------------------------')
    print(tabulate(a, headers=heads, tablefmt='markdown'))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))
    ax1.scatter(np.arange(0, n), matrixprice[1:, 3],
                label='PRICE', color='salmon')
    ax1.scatter(np.arange(0, n), matrixsac[1:, 3],
                label='SAC', color='darkcyan')
    ax1.set_xlabel('Period')
    ax1.set_ylabel('Value')
    ax1.set_title('Payment')
    ax1.legend(loc='best')

    r = np.arange(len(heads))
    w = 0.25
    ax2.bar(r, np.sum(matrixprice[:, 1:4], axis=0),
            width=w, label='PRICE', color='salmon')
    ax2.bar(r + w, np.sum(matrixsac[:, 1:4], axis=0),
            width=w, label='SAC', color='darkcyan')
    ax2.set_xticks(r + w/2,  heads)
    ax2.legend(loc='best')
    ax2.set_title('Totals')
    plt.tight_layout()
    plt.show()


amort(189600, 96, 0.9)
