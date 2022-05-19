def get_longest_prefix_in_two_strings(str1 , str2):
        prefix = ""
        for i, o in zip(str1, str2):

            if i == o:
                prefix += i
            else:
                break
        return prefix


class Solution:
    
    
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        longest_common = strs[0]
        
        for string in strs:
            
            longest_common = get_longest_prefix_in_two_strings( longest_common , string )
        
        return longest_common
            