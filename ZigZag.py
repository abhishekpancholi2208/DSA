class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a=['']*numRows
        i=0
        f=0
        flag=False
        
        while i<len(s):
            if f%numRows==0 and i>0:
                flag=not flag
                if flag==True:
                    f-=1
                else:
                    f+=1
            if flag==False:
                print(f)
                a[f]+=s[i]
                f+=1
            else:
                f-=1
                print(f)
                a[f]+=s[i]
                
            i+=1
            
