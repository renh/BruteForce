#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Hao Ren <renh.cn@gmail.com>
#
# Distributed under terms of the LGPLv3 license.

"""
Brute force integer arithmetic practices
    only positive integers supported currently.
    will update to broader domains if this version DOES help ...

"""
from __future__ import print_function
import numpy as np
import random

dict_operators = {
    '+' : '+',
    '-' : '-',
    '*' : '\\times',
    '/' : '\\div'
}

gray = '#c7d1cb'

def gen_expression(lb, hb, ops, negative):
    n1 = random.randint(lb, hb)
    n2 = random.randint(lb, hb)
    op = random.choice(ops)
    if op == '+': 
        expression = (n1, op, n2)
    elif op == 'x': 
        expression = (n1, '\\times', n2)
    elif op == '-':
        expression = (n2, op, n1) if (n2 > n1 and not negative)  else (n1, op, n2)
    elif op == '/':
        n1 *= n2
        expression = (n1, '\\div', n2)
        # divided by zero is not excluded.
        # kids should be familiar with this sigularity
    else:
        raise ValueError('operator not supported')
    return expression
    




if __name__ == '__main__':
    import argparse
    from datetime import datetime
    import matplotlib.pyplot as plt

    parser = argparse.ArgumentParser()
    parser.add_argument('-L', '--lowerbound', help='Lower bound of the operands',
                        default = 1, type=int)
    parser.add_argument('-U', '--upperbound', help='Upper bound of the operands',
                        default= 19, type=int)
    parser.add_argument('-p', '--operators',
                        help='String of the set of operators, e.g. "+-*/" means ' +
                        'summation, substraction, multiplication, and division are' +
                        ' allowed', default='+-')

    parser.add_argument('-n', '--negative', help='Allow negative results',
                        action='store_true')
    args = parser.parse_args()

    LB = args.lowerbound
    HB = args.upperbound
    negative = args.negative
    ops = args.operators

    exps = []
    while len(exps) < 50:
        expression = gen_expression(LB, HB, ops, negative)
        if expression in exps:
            continue
        else:
            exps.append(expression)
        
    
    # generate pdf with matplotlib
    fig = plt.figure()
    fig.set_size_inches(8.27, 11.7) # hard coded A4 paper, portrait
    ax = plt.Axes(fig, [0, 0, 1, 1])

    fig.add_axes(ax)

    ax.set_xlim([0, 210])
    ax.set_ylim([0, 297])
    ax.set_xticks([-1])
    ax.set_yticks([-1])

    ax.text(20, 275, "Name: ________________", fontsize=16)
    ax.text(190, 275, "Score: __________/100", ha='right',fontsize=16)

    ax.plot([105,105], [20,270], color=gray, ls='-', lw='0.75')
    #ax.plot([20,190], [20,20], color=gray, ls='-', lw='0.75')
    ax.plot([20,190], [270,270], color=gray, ls='-', lw='0.75')
    ax.plot([20,20], [20,270], color=gray, ls='-', lw='0.75')
    ax.plot([190,190], [20,270], color=gray, ls='-', lw='0.75')

    for line in range(25):
        bottom_line = 270 - (line+1) * 10
        ax.plot([20,190],[bottom_line,bottom_line], color=gray, ls='-', lw='0.75')
        exp1, exp2 = exps[line*2:(line+1)*2]
        str1 = r"{:4d}  ${:s}$ {:3d}  $=$".format(*exp1)
        str2 = r"{:4d}  ${:s}$ {:3d}  $=$".format(*exp2)
        ax.text(25, bottom_line+1, str1, fontsize=14,
                va='bottom', ha='left', family='serif')
        ax.text(110, bottom_line+1, str2, fontsize=14,
                va='bottom', ha='left', family='serif')
    dt_str = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    ax.text(190,10, "Created at {}".format(dt_str), ha='right')

    plt.savefig('exercises.pdf')


    


