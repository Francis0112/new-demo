


class Factor:


    def factorial(num):
        if num==1:
            return 1
        else:
            return num * Factor.factorial(num-1)


a = Factor
print(a.factorial(7))