#import pandas as pd
import numpy as np

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #df = pd.DataFrame(board)
        arr = np.array(board)
        #print(arr)
        for i in range(9):
            x=[]
    
            if (i == 0):
                array = arr[0:3,0:3].flatten()
            
                for v in array :
                    if(v in x and v!='.'):
                        return False
                    else:
                        x.append(v)
            if (i == 1):
                array = arr[0:3,3:6].flatten()
                for v in array :
                    if(v in x and v!='.'):
                        return False
                    else:
                        x.append(v)
    
            if (i == 2):
                array = arr[0:3,6:9].flatten()
                for v in array:
                    if(v in x and v!='.'):
                        return False
                    else:
                        x.append(v)
            if (i == 3):
                array = arr[3:6,0:3].flatten()
                for v in array:
                    if(v in x and v!='.'):
                        return False
                    else:
                        x.append(v)
            if (i == 4):
                array = arr[3:6,3:6].flatten()
                for v in array:
                    if(v in x and v!='.'):
                        return False
                    else:
                        x.append(v)
            if (i == 5):
                array = arr[3:6,6:9].flatten()
                for v in array:
                    if(v in x and v!='.'):
                        return False
                    else:
                        x.append(v)
            if (i == 6):
                array = arr[6:9,0:3].flatten()
                for v in array :
                    if(v in x and v!='.'):
                        return False
                    else:
                        x.append(v)
            if (i == 7):
                array = arr[6:9,3:6].flatten()
                for v in array:
                    if(v in x and v!='.'):
                        return False
                    else:
                        x.append(v)
                
            if (i == 8):
                array = arr[6:9,6:9].flatten()
                for v in array:
                    if(v in x and v!='.'):
                        return False
                    else:
                        x.append(v)
    
            x.clear()
            for v in board[:][i]:
                
                if(v in x and v!='.'):
                    return False
                else :
                    x.append(v)
    
    
    
            x.clear()
            y=arr[:,i]
            
            
            for v in y:
                #print("v = " , v)
                if v in x and v!='.':
                    return False
                else :
                    x.append(v)
            x.clear()
        return True
                    
            
            
        