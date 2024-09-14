class Solution:
    def helper(self, arr, n, mid):
        students = 1
        pages = 0
        for i in range(n):
            if pages + arr[i] <= mid:
                pages += arr[i]
            else:
                students += 1
                pages = arr[i]
        return students

    def books(self, A, B):
        n = len(A)
        low = max(A)
        high = sum(A)
        if B > n:
            return -1

        for pages in range(low, high + 1):
            if self.helper(A, n, pages) == B:
                return pages
        return low
