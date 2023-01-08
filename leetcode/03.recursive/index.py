class Solution:
    def recursive_func(self, i):
        if i <= 0:
            print(i)
            return
        else:
            Solution().recursive_func(i - 1)


Solution().recursive_func(23)


# def recursive_func(i):
#     if i <= 0:
#         print(i)
#         return
#     else:
#         recursive_func(i - 1)
