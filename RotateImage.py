class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        res = []
        for i in zip(*matrix):
            res.append(list(i[::-1]))
        matrix[:]=res[:]
