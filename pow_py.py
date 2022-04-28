class Power:
    def __init__(self,x,n):
        self.x=x
        self.n=n

    def calculate(self):
        print(self.x**self.n)


x=int(input('Enter x:'))
n=int(input('Enter n:'))
pow=Power(x,n)
pow.calculate()