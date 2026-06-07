class Pattern:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()
    
    def pattern2(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            print()

    def pattern3(self, n):
        for i in range(n):
            for j in range(i+1):
                print(j+1, end="")
            print()

    def pattern4(self, n):
        for i in range(n):
            for j in range(i+1):
                print(i+1, end="")
            print()

    def pattern5(self, n):
        for i in range(n):
            for j in range(n-i):
                print("*", end="")
            print()

    def pattern6(self, n):
        for i in range(n):
            for j in range(n-i):
                print(j+1, end="")
            print()
    
    def pattern7(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end="")
            for j in range(2*i+1):
                print("*", end= "")
            for j in range(n-i-1):
                print(" ", end="")
            print()
   
    def pattern8(self, n):
        for i in range(n):
            for j in range(i):
                print(" ", end="")
            for j in range(2*n-(2*i+1)):
                print("*", end="")
            for j in range(i):
                print(" ", end="")
            print()

    def pattern9(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end="")
            for j in range(2*i+1):
                print("*", end="")
            print()

        for i in range(n-1):
            for j in range(i+1):
                print(" ", end="")
            for j in range(2*n-(2*i+3)):
                print("*", end="")
            print()

    def pattern10(self, n):
        # Upper half
        for i in range(n):
            for j in range(i + 1):
                print("*", end="")
            print()

        # Lower half
        for i in range(n - 1):
            for j in range(n - i - 1):
                print("*", end="")
            print()


obj = Pattern()
obj.pattern1(4)
obj.pattern2(5)
obj.pattern3(4)
obj.pattern4(5)
obj.pattern5(5)
obj.pattern6(5)
obj.pattern7(5)
obj.pattern8(5)
obj.pattern9(5)
obj.pattern10(5)