# Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/


from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def _transform(i: int) -> str:
            if i % 15 == 0:
                return "FizzBuzz"
            elif i % 3 == 0:
                return "Fizz"
            elif i % 5 == 0:
                return "Buzz"
            else:
                return str(i)

        return [_transform(i) for i in range(1, n + 1)]
