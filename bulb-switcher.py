#!/usr/bin/python3
class Solution:
    def getDivisorsNum(self, i: int) -> int: 

        if i == 1: return 1;
        # taking trivial solutions (1 and i)
        div_num = 2
        for j in range(2, i): 
            if i%j == 0:
                div_num += 1
        return div_num

    def bulbSwitch(self, n: int) -> int: 

        # odd number of divisors => bulb will be on
        on_bulbs_count = 0
        for i in range(1, n+1):
            if self.getDivisorsNum(i)%2:
                on_bulbs_count += 1

        return on_bulbs_counts