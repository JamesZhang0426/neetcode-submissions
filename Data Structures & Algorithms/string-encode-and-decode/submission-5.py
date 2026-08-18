class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        toreturn = ""
        for i in range(len(strs)):
            toreturn+= str(len(strs[i]))+"#"+strs[i]
        return toreturn 


    def decode(self, s: str) -> List[str]:
        toreturn = []
        if len(s) == 0:
            return []
    
        i = 0

        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1 
            
            lenght = int(s[i:j])

            toreturn.append(s[j+1:j+1+lenght])

            i = j+1+lenght
        return toreturn


            
            

