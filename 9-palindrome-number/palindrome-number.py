class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        
        palindrome = [int(i) for i in str(x)] # 1 0 0
        new_list = palindrome[::-1] # 0 0 1

        if palindrome == new_list:
          return True
        else:
          return False

solution = Solution()

result = solution.isPalindrome(100)
print(result)