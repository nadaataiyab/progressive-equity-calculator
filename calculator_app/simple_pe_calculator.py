'''
Simple Progressive Equity Calculator:
-------------------------------------
Calculates payouts for equity holders under a progressive equity scheme.

The goal of progressive equity is to allow founders and early employees
to share some of the wealth earned through a large exit with other employees
once a pre-set "financial independence number" is achieved.

In an exit, any earnings over that financial independence number are taxed (usually at 50%)
and put back into a kicker pool. The monies in the pool are distributed
to the remaining employees (who have not been taxed) on a pro-rata basis.

Employees that are no longer with the company will not be eligible to receive
monies distributed from the kicker pool.

'''

import pandas as pd
from collections import defaultdict

EQUITY_HOLDERS_DEFINITIONS = ['Equity Percent [0]',
                              'Subject to Progressive [1]',
                              'Triggered [2]',
                              'Employed [3]',
                              'Payout [4]',
                              'Standard Payout [5]']

# THESE FUNCTIONS ARE NOT USED IN THE WEB APP
def check_equity_balance(equity_holders):
    '''
    Checks to ensure that the equity values inputted add up to 1. If equity
    does not add up to 1, then error message will be displayed and user
    will be asked to re-enter equity numbers.

    '''
    total_equity = 0
    for data in equity_holders.values():
        equity = data[0]
        total_equity += equity

    if total_equity != 1:
        message = ("ERROR ENTERING EQUITY - Total equity = " + str(total_equity))
        return message
    else:
        message = ("Total equity = " + str(total_equity))
        return message
#
# def print_basic_info(exit_price, fin_independence, tax, equity_holders):
#     '''
#     '''
#     print("Exit Price: ", exit_price)
#     print("Financial Independence Number: ", fin_independence)
#     print("Equity Tax: ", tax)
#     print("Equity Holders Definitions: ")
#     for item in EQUITY_HOLDERS_DEFINITIONS:
#         print("    ", item)
#
# def print_equity_holders(equity_holders):
#     for name, data in equity_holders.items():
#         print(name, ": ", data)


def round_1(equity_holders, exit_price, fin_independence, tax):
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
        equity_holders[name][5] = payout

        if subject_progressive == False:
            equity_holders[name][4] = payout

        else:
            if payout > fin_independence:
                pool_contribution = ((payout - fin_independence) * tax)
                pool += pool_contribution
                payout -= pool_contribution
                equity_holders[name][4] = payout
                equity_holders[name][2] = True
            else:
                equity_holders[name][4] = payout
    #print("Round 1")
    #print("Pool: ", pool)
    #print_equity_holders(equity_holders)

    return pool, equity_holders

def redistribution_denominator(pool, equity_holders, fin_independence):
    '''
    Calculates denominator and recipients to receive redistribution funds
    from pool.

    '''
    equity_denominator = 0
    recipients = []
    for name, data in equity_holders.items():
        equity = data[0]
        triggered = data[2]
        employed = data[3]
        if triggered == False and employed == True:
            equity_denominator += equity
            recipients.append(name)

    return equity_denominator, recipients


def distribute_pool(pool, equity_holders, fin_independence,
                    equity_denominator, recipients):
    '''
    Distribute monies in pool to employees that have not reached financial
    independence number.

    '''
    distributed_funds = 0

    for name in recipients:
        equity = equity_holders[name][0]
        payout = equity_holders[name][4]
        redistribution = equity / equity_denominator * pool
    #    max_redistribution = (equity / equity_denominator * pool)
    #    fin_independence_gap = fin_independence - payout
    #    redistribution = min(fin_independence_gap, max_redistribution)
    #    distributed_funds += redistribution
        equity_holders[name][4] = payout + redistribution

    #    if (payout + redistribution) > fin_independence:
    #        equity_holders[name][2] = True

    #pool -= distributed_funds
    #print("Redistribution Round")
    #print("Pool: ", pool)
    #print_equity_holders(equity_holders)

    return pool, equity_holders

# def final_distribution(equity_holders, pool):
#     '''
#     If all employees have reached financial independence then any remaining
#     funds are distributed pro-rata to all employees and founders.
#
#
#     '''
#     equity_denominator = 0
#     recipients = []
#     for name, data in equity_holders.items():
#         equity = data[0]
#         progressive = data[1]
#         employed = data[3]
#         if progressive == True and employed == True:
#             equity_denominator += equity
#             recipients.append(name)

    # for name in recipients:
    #     equity = equity_holders[name][0]
    #     payout = equity_holders[name][4]
    #     distribution = equity / equity_denominator * pool
    #     equity_holders[name][4] += distribution
    #
    # print("Final Round")
    # print("Pool", pool)
    # print_equity_holders(equity_holders)
    #
    # return equity_holders


# def redistribution_rounds(equity_holders, pool, fin_independence):
#     '''
#
#     '''
#     equity_denominator, recipients = redistribution_denominator(pool, equity_holders, fin_independence)
#
#     if equity_denominator > 0 and pool > 0:
#         pool, equity_holders = distribute_pool(pool, equity_holders, fin_independence,
#                                                        equity_denominator, recipients)
#
#         if pool > 0:
#             equity_holders = final_distribution(equity_holders, pool)
#
#         else:
#             return equity_holders
#
#     elif equity_denominator == 0 and pool > 0:
#         equity_holders = final_distribution(equity_holders, pool)
#         return equity_holders
#
#     else:
#         return equity_holders



def progressive_payout(exit_price, fin_independence, equity_holders, tax):
    '''
    '''
    #Check that equity numbers were entered correctly
    # if check_equity_balance(equity_holders) == True:
    #
    #     #Print basic information
    #     print_basic_info(exit_price, fin_independence, tax, equity_holders)



    #Check that equity numbers were entered correctly
    message = check_equity_balance(equity_holders)

    #Round 1 of payout distributions
    pool, equity_holders = round_1(equity_holders, exit_price,
                                               fin_independence, tax)
    #If monies have been paid into pool, do redistribution rounds

    if pool > 0:
        equity_denominator, recipients = redistribution_denominator(pool, equity_holders,
                                                             fin_independence)

        pool, equity_holders = distribute_pool(pool, equity_holders, fin_independence,
                            equity_denominator, recipients)

        return message, pool, equity_holders

    else:
        return message, pool, equity_holders




#-------------------------------------------------------------------------------
# if __name__ == '__main__':
#
#     exit_price = 200
#     fin_independence = 15
#     tax = .5
#
#     equity_holders_definitions = ['Equity Percent [0]', 'Subject to Progressive [1]', 'Triggered [2]',
#                                  'Employed [3]', 'Payout [4]', 'Standard Payout [5]']
#
#     equity_holders = {'angel1' :  [.1, False, False, False, 0, 0 ],
#                      'venture1':  [.1, False, False, False, 0, 0],
#                      'founder1':  [.25, True, False, True, 0, 0],
#                      'founder2':  [.25, True, False, True, 0, 0],
#                      'employee1': [.1, True, False, True, 0, 0],
#                      'employee2': [.1, True, False, False, 0, 0],
#                      'employee3': [.05, True, False, True, 0, 0],
#                      'employee4': [.05, True, False, False, 0, 0]}
#
#     message, pool, equity_holders = progressive_payout(exit_price, fin_independence,
#                                         equity_holders, tax)
#
#     print(message)
#
#     print(pool)
#
#     for name, data in equity_holders.items():
#           print(name, ':', data)
