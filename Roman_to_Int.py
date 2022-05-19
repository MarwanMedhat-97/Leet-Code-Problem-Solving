class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1,
        "CM": 900,
        "CD": 400,
        "XC": 90,
        "XL": 40,
        "IX": 9,
        "IV": 4,
        }
        i = 0
        num = 0
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in my_dict:
                num+=my_dict[s[i:i+2]]
                i+=2
            else:
                num+=my_dict[s[i]]
                i+=1
        return num
                
        