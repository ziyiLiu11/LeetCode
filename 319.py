class Solution:
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        The idea is for every light bulb (index) in the list, we find out how many times the light bulb is been togglered (number of factor for this index). Then we
        determine if the light bulb is on or off.
        Time Complexity: O(n^2)
        Space Comlexity: O(1)
        """
        _ans = 0
        for num in range(1, n+1):
            counter = num
            toggler = 0
            while counter > 0:
                if num % counter == 0:
                    toggler += 1
                counter -= 1
            if toggler != 0 and toggler % 2 == 1:
                _ans += 1
        return _ans

    def second_try(self, n):
        """
        :type n: int
        :rtype: int
        The trivial method is too slow. By observation, we know that we only need traversal sqrt of n (index) number to computer the times a light bulb been togglered.
        (n =  sqrt(n) * sqrt(n))
        Time Complexity: O(n * sqrt(n))
        Space Comlexity: O(1)
        """
        _ans = 0
        for num in range (1, n+1):
            counter = int(num**0.5)
            toggler = 0
            while counter > 0:
                if num % counter == 0:
                    toggler += 1 if num / counter == counter else 2
                counter -= 1
            if toggler != 0 and toggler % 2 == 1:
                _ans +=1
        return _ans

    def third_try(self, n):
        """
        :type n: int
        :rtype: int
        The method still too slow. For each number, we could either toggler 1 or 2 times each times. The only scenario that the number been toggler 1 times is the number 
        is a perfect square. Eventually, we only need to compute how many perfect square from [1, n].
        Time Complexity: O(1)
        Space Comlexity: O(1)
        """
        return int(n**0.5)