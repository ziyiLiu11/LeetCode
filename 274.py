class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        Ideas: Since we need at least h paper that citations is at least h and the order of the citation doesn't matter, we could sort the citation and start at the bottom 
        to check what is the maximum number for h index
        Time Complexity: O(nlogn)
        Space Complexity: O(1)
        """
        citations.sort()
        size = len(citations)
        for num in citations:
            if num >= size:
                return size
            size -=1
        return 0

    def second_try(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        Ideas: Using bucket sort insead we could do better 
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        size = len(citations)
        my_bucket = [0] * (size+1)
        for num in citations:
            if num >= size:
                my_bucket[size] += 1
            else:
                my_bucket[num] += 1
        sum = 0
        for index in range(size, 0, -1):
            sum += my_bucket[index]
            if sum >= index:
                return index
        return 0
                
        