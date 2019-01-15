'''
 *
 * Copyright (C) Rajdeep Roy Chowdhury 2019<rrajdeeproychowdhury@gmail.com>
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