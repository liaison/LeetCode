
"""

"""
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(s) != len(t)):
            return False
        
        def to_dict(word):
            ret = {}
            for letter in word:
                if letter in ret:
                    ret[letter] +=1
                else:
                    ret[letter] = 1
            return ret
        
        dict_1 = to_dict(s)
        dict_2 = to_dict(t)
        return (dict_1 == dict_2)



if __name__ == "__main__":

    solution = Solution()

    print(solution.isAnagram("abcd", "bcda"))


