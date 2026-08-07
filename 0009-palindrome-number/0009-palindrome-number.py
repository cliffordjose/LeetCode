class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers are never palindromes
        if x < 0:
            return False

        # Numbers ending in 0 are not palindromes,
        # except 0 itself
        if x % 10 == 0 and x != 0:
            return False

        reversed_num = 0

        while x > reversed_num:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10

        # Even number of digits
        if x == reversed_num:
            return True

        # Odd number of digits
        return x == reversed_num // 10