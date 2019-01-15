'''
 *
 * Copyright (C) Rajdeep Roy Chowdhury 2019 <rrajdeeproychowdhury@gmail.com>
 *
 * You may redistribute it and/or modify it under the terms of the
 * GNU General Public License, as published by the Free Software
 * Foundation; either version 2 of the License, or (at your option)
 * any later version.
 *
 * MathsFormula is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 *
'''

import math

class Logic:
    def __init__(self):
        self.formula=dict()
        self.formula['sin2X']='sine 2 x is equals to 2 sine X cos X'
        self.formula['cos2X']='cos 2 x is equals to cos square x minus sine square x, or 1 minus 2 sine square x, or 2 cos square x minus 1'
        self.formula['tan2X']='tan 2 x is equals to 2 tan X whole divided by 1 minus tan square x'
        self.formula['sin3x']='sine 3 x is equals to 3 sine x minus 4 sine cube x'
        self.formula['cos3x']='cos 3 x is equals to 4 cos cube x minus 3 cos x'
        self.formula['tan3x']='tan 3 x is equals to3 tan x minus tan cube x whole divided by 1 minus 3 tan square x'
    def sine(self,value):
        '''Returns sine of an angle (in degrees)'''
        return math.sin(value*(22/7)/180)
    def cosine(self,value):
        '''Returns cosine of an angle (in degrees)'''
        return math.cos(value*(22/7)/180)
    def tangent(self,value):
        '''Returns tangent of an angle (in degrees)'''
        return math.tan(value*(22/7)/180)
    def factorial(self,n):
        '''Returns factorial of n'''
        result = 1
        for i in range(1,n+1):
            result=result*i
        return result
    def sumOfNaturalNumbers(self,n):
        '''Return sum of n natural numbers'''
        return n*(n+1)//2

# For local debugging purposes only
if __name__=='__main__':
    logic=Logic()
    for i in logic.formula.keys():
        print(i)
    # logic.cosine(10)