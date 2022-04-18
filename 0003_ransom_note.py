class Solution:
    def canConstruct(ransomNote: str, magazine: str) -> bool:
        # create a dictionary to store the values of the magazine
        magazine_dict = {}
        # loop through the magazine
        for i in range(len(magazine)):
            # check if the current letter is in the dictionary
            if magazine[i] in magazine_dict:
                # if it is, add 1 to the value
                magazine_dict[magazine[i]] += 1
            else:
                # if it isn't, add the letter to the dictionary with a value of 1
                magazine_dict[magazine[i]] = 1
        # loop through the ransom note
        for i in range(len(ransomNote)):
            # check if the current letter is in the dictionary
            if ransomNote[i] in magazine_dict:
                # if it is, subtract 1 from the value
                magazine_dict[ransomNote[i]] -= 1
                # if the value is 0, remove the letter from the dictionary
                if magazine_dict[ransomNote[i]] == 0:
                    del magazine_dict[ransomNote[i]]
            else:
                # if it isn't, return False
                return False
        # return True if the loop completes
        return True


print(Solution.canConstruct("aa", "aab"))
