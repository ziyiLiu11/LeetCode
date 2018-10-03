class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import re
        mylist = re.findall(r'\w+', paragraph.lower())
        print(mylist)
        ban = set(banned)
        from collections import Counter
        c = Counter()
        for i in mylist:
            if i not in ban:
                c[i]+=1
        return c.most_common(1)[0][0]

    def secondtry(self, paragraph, banned):
        """
        the filter portion could be simplify using regular expression
        """
        import re
        mylist = re.findall(r'\w+', paragraph.lower())
        print(mylist)
        ban = set(banned)
        from collections import Counter
        return Counter(w for w in mylist if w not in ban).most_common(1)[0][0]



