'''
This module caluates payouts for equity holders under a progressive equity scheme.
The goal of progressive equity is to allow founders and early employees
to share some of the wealth earned through a large exit with other employees
once a pre-set "financial independence number" is achieved.

In an exit, any earnings over that financial independence number are taxed (usually at 50%)
and put back into a redistribution pool. The monies in the pool are distributed
to the other employees that have not hit the financial independence number
based on their equity share.

No employee may receive a total payout of more than the financial independence
number in the redistribution round.

If there are any funds leftover in the pool after the redistribution round,
those funds are distributed to all the founders and employees based on their
equity share.

'''

import pandas as pd
from collections import defaultdict

def check_equity_balance(equity_holders):
    '''
    Checks to ensure that the equity values inputted add up to 1.

    '''
    total_equity = 0
    for data in equity_holders.values():
        equity = data[0]
        total_equity += equity

    if total_equity != 1:
        print("Error in equity input. Total equity does not add up to 1. \n"
              "Total equity = ", total_equity, '.')
        return False
    else:
        return True

def round_1(equity_holders, exit_price, fin_independence, tax ):
    '''
    Calulates payouts from the first round of distribution.
    Any equity holders that exceed the finanical independence number contributes
    a portion of the excess funds (usually 50%) into a pool.

    '''
    pool = 0

    for name, data in equity_holders.items():
        equity_percent = data[0]
        subject_progressive = data[1]
        payout = (equity_percent * exit_price)
        if subject_progressive == False:
            equity_holders[name][4] = payout

        else:
            if payout > fin_independence:
                tax = ((payout - fin_independence) / 2)
                pool += tax
                payout -= tax
                equity_holders[name][4] = payout
                equity_holders[name][2] = True
            else:
                equity_holders[name][4] = payout
    return pool, equity_holders

def redistribution_denominator(pool, equity_holders, fin_independence):
    '''
    Calculates denominator used to determine proportion of pool to be distributed
    to each elibible employee.

    '''
    equity_denominator = 0
    for name, data in equity_holders.items():
        equity = data[0]
        triggered = data[2]
        employed = data[3]
        if triggered == False and employed == True:
            equity_denominator += equity

    return equity_denominator


def distribute_pool(pool, equity_holders, fin_independence, equity_denominator):
    '''
    Distribute monies in pool to employees that have not reached financial
    independence number.

    '''
    distributed_funds = 0
    for name, data in equity_holders.items():
        equity = data[0]
        triggered = data[2]
        employed = data[3]
        payout = data[4]
        if triggered == False and employed == True:
            max_redistribution = (equity / equity_denominator * pool + payout)
            fin_independence_gap = fin_independence - payout
            redistribution = min(fin_independence_gap, max_redistribution)
            distributed_funds += redistribution
            equity_holders[name][4] = payout + redistribution
            equity_holders[name][2] = True

    pool -= distributed_funds

    return pool, equity_holders

def final_distribution(equity_holders, pool):
    '''
    If all employees have reached financial independence then any remaining
    funds are distributed pro-rata to all employees and founders.


    '''
    equity_denominator = 0
    for name, data in equity_holders.items():
        equity = data[0]
        progressive = data[1]
        employed = data[3]
        if progressive == True and employed == True:
            equity_denominator += equity

    for name, data in equity_holders.items():
        equity = data[0]
        progressive = data[1]
        employed = data[3]
        payout = data[4]
        if progressive == True and employed == True:
            distribution = equity / equity_denominator * pool
            equity_holders[name][4] += distribution

    return equity_holders


def redistribution (equity_holders, pool, fin_independence):
    '''

    '''
    equity_denominator = redistribution_denominator(pool, equity_holders, fin_independence)

    if equity_denominator > 0:
        pool, equity_holders = distribute_pool(pool, equity_holders, fin_independence, equity_denominator)
        print("Pool: ", pool)
        print(equity_holders)
        if pool > 0:
            redistribution(equity_holders, pool, fin_independence)
            return equity_holders
        else:
            return equity_holders

    else:
        equity_holders = final_distribution(equity_holders, pool)
        return pool, equity_holders


def progressive_payout(exit_price, fin_independence, equity_holders, tax):
    '''
    '''

    check_equity_balance(equity_holders)

    pool, equity_holders = round_1(equity_holders, exit_price, fin_independence, tax)
    print("Pool: ", pool)
    print(equity_holders)

    if pool > 0:
        equity_holders = redistribution(equity_holders, pool, fin_independence)
        return pool, equity_holders

    else:
        return equity_holders

-------------------------------------------------------------------------------
if __name__ == '__main__':
