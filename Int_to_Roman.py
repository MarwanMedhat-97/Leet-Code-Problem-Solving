class Solution:
    def intToRoman(self, num: int) -> str:
        
        x=""
        while num > 0:
            #print(num)
            if(num - 1000 >= 0):
                x+='M'
                num = num - 1000
            elif(num - 900 >= 0 ):
                x+='CM'
                num = num - 900
            elif(num - 500 >= 0 ):
                x+='D'
                num = num - 500
            elif(num - 400 >= 0 ):
                x+='CD'
                num = num - 400
            elif(num - 100 >= 0 ):
                x+='C'
                num = num - 100
            elif(num - 90 >= 0 ):
                x+='XC'
                num = num - 90
            elif(num - 50 >= 0 ):
                x+='L'
                num = num - 50
            elif(num - 40 >= 0 ):
                x+='XL'
                num = num - 40
            elif(num - 10 >= 0 ):
                x+='X'
                num = num - 10
            elif(num - 9 >= 0 ):
                x+='IX'
                num = num - 9
            elif(num - 5 >= 0 ):
                x+='V'
                num = num - 5
            elif(num - 4 >= 0 ):
                x+='IV'
                num = num - 4
            else:
                x+='I'
                num = num - 1
        return x
            
            
        
            
            
        
        
        