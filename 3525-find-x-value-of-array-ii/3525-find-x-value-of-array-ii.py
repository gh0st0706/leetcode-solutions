class Solution(object):
    def resultArray(self, nums, k, queries):
        n = len(nums)

        treeProd = [1] * (4 * n)
        treeCnt = [[0] * k for _ in range(4 * n)]

        def pull(node):
            left = node * 2
            right = node * 2 + 1

            leftProd = treeProd[left]
            rightProd = treeProd[right]

            treeProd[node] = (leftProd * rightProd) % k

            newCnt = treeCnt[left][:]

            for r in range(k):
                newRemainder = (leftProd * r) % k
                newCnt[newRemainder] += treeCnt[right][r]

            treeCnt[node] = newCnt

        def build(node, l, r):
            if l == r:
                remainder = nums[l] % k
                treeProd[node] = remainder
                treeCnt[node][remainder] = 1
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            pull(node)

        def update(node, l, r, index, value):
            if l == r:
                remainder = value % k

                treeProd[node] = remainder
                treeCnt[node] = [0] * k
                treeCnt[node][remainder] = 1
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            pull(node)

        def merge(a, b):
            if a is None:
                return b

            if b is None:
                return a

            prodA, cntA = a
            prodB, cntB = b

            newProd = (prodA * prodB) % k
            newCnt = cntA[:]

            for r in range(k):
                newRemainder = (prodA * r) % k
                newCnt[newRemainder] += cntB[r]

            return newProd, newCnt

        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return None

            if ql <= l and r <= qr:
                return treeProd[node], treeCnt[node][:]

            mid = (l + r) // 2

            leftResult = query(
                node * 2,
                l,
                mid,
                ql,
                qr
            )

            rightResult = query(
                node * 2 + 1,
                mid + 1,
                r,
                ql,
                qr
            )

            return merge(leftResult, rightResult)

        build(1, 0, n - 1)

        result = []

        for index, value, start, x in queries:
            nums[index] = value

            update(
                1,
                0,
                n - 1,
                index,
                value
            )

            prod, counts = query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            result.append(counts[x])

        return result