# F(0) = 0, F(1) = 1
class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1: return n
        num1=0
        num2=1
        while n>1:
            tmp=num2
            num2=num1+num2
            num1=tmp
            n-=1
        return num2


def main(n: int):
    print(Solution().fib(n))
    return 0

if __name__ == "__main__":
    main(4)
