# Sum of Digits of String After Convert
# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def _digit_sum(n: int) -> int:
            s: int = 0
            while n != 0:
                s = s + (n % 10)
                n = n // 10
            return s

        def _transform(s: str) -> int:
            result: int = 0
            for c in reversed(s):
                d: int = ord(c) - ord("a") + 1
                if d < 10:
                    result = 10 * result + d
                else:
                    result = 100 * result + d

            return result

        n: int = _transform(s)

        for _ in range(k):
            n = _digit_sum(n)

        return n
