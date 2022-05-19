class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if (divisor == 0 ):
            print("Error !! Divisor can not be zero")
        
        if (dividend == (-2)**31 and divisor == -1):
            return ((2)**31)-1
        
        if (divisor < 0  and dividend < 0 ):
            
            return dividend // divisor
            
        
        if ( dividend < 0  ):
            
            dividend = -1 *dividend
            x = dividend // divisor
            
            return -1 * x
        
        if ( divisor < 0  ):
            
            divisor = -1 *divisor
            x = dividend // divisor
            
            return -1 * x
    
            
        
        return dividend // divisor