class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        maximum = 0

        for row_shift in range(-(n-1), n):
            for col_shift in range(-(n-1), n):

                overlap = 0

                for row in range(n):
                    for col in range(n):

                        new_row = row + row_shift
                        new_col = col + col_shift

                        if 0 <= new_row < n and 0 <= new_col < n:
                            if img1[row][col] == 1 and img2[new_row][new_col] == 1:
                                overlap += 1

                maximum = max(maximum, overlap)
        return maximum 