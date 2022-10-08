class Solution(object):
    @classmethod
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<-2**31 or x>=2**31:
            return 0 
        flag = 0
        if x < 0:
            flag=1
        x=abs(x)
        list_x=list(str(x))
        reversed_num = 0
        count=0
        for digit in list_x:
            reversed_num= reversed_num+(10**count)*int(digit)
            count += 1
        if flag == 1:
            reversed_num = -reversed_num
        if reversed_num<-2**31 or reversed_num>=2**31:
            return 0 
        return reversed_num

x =  1534236469
sol=Solution.reverse(x)
print(sol)
        
            