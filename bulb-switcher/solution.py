#!/usr/bin/python3
from math import floor, sqrt

class Solution:
    def getDivisorsNum(self, i: int) -> int: 

        div_num = 0
        for j in range(1, floor(sqrt(i))+1): 
            if i%j == 0:
                if j*j == i:
                    div_num += 1
                else:
                    div_num += 2
        return div_num

    def bulbSwitch(self, n: int) -> int: 

        on_bulbs_count = 0

        # Depending on the number given as input, different
        # solution approaches are used. First, as a slower
        # technique (appr. O(n^(2/3))), is applied to 
        # small numbers, for example, n < 100. Second, with
        # linear complexity, is applied for bigger ns.
        if (n < 100):
            # idea: odd number of divisors => bulb will be on
            for i in range(1, n+1):
                if self.getDivisorsNum(i)%2:
                    on_bulbs_count += 1
        else:
            # idea: the situation shows that only the bulbs with
            # numbers being squares of 1, 2, 3, etc. will be
            # turned on at the end of a process
            squares = [i**2 for i in range(1, floor(sqrt(n))+1)]
            on_bulbs_count = len(list(squares))

        return on_bulbs_count
