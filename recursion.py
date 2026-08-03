class recursion:
    def name(self, i, n):
        if i > n:
            return
        # print name 5 times: base condition
        print("Manya")
        self.name(i+1, n)
        # Time complexity: O(n), space: O(n)


    def linear(self,i,n):
        if i > n:
            return
        print(i)
        self.linear(i+1,n)
       
    def reverse(self, i, n):
        if i < 1:
            return
        print(i)
        self.reverse(i-1, n)


# using backtracking, that is using the print call after the recursive call
    def linearbacktrack(self,i,n):
        if i < 1:
            return
        self.linearbacktrack(i-1,n)
        print(i)

    def reversebacktrack(self, i, n):
        if i > n:
            return
        self.reversebacktrack(i+1, n)
        print(i)

obj = recursion()
obj.name(1, 5)
obj.linear(1,5)
obj.reverse(5,5)
obj.linearbacktrack(5,5)
obj.reversebacktrack(1,5)