# Minimum Operations to Make Array Equal
# https://leetcode.com/problems/minimum-operations-to-make-array-equal/


class Solution:
    def minOperations(self, n: int) -> int:
        # Example: odd n
        #   n = 3: [1, 3, 5];               2 = 2
        #   n = 5: [1, 3, 5, 7, 9];         4 + 2 = 6
        #   n = 7: [1, 3, 5, 7, 9, 11, 13]; 6 + 4 + 2 = 12
        #   . . .

        # Example: even n
        #   n = 2: [1,3];           1 = 1
        #   n = 4: [1,3,5,7];       3 + 1 = 4
        #   n = 6: [1,3,5,7,9,11];  5 + 3 + 1 = 9
        #   . . .

        if n % 2 == 0:
            # For n = 2k
            #   1 + 3 + 5 + ... + (2k-1) = k^2
            return (n // 2) ** 2

        else:
            # For n = 2k+1
            #   2 + 4 + 6 + ... + 2k = k*(k+1)
            return n // 2 * (n // 2 + 1)
