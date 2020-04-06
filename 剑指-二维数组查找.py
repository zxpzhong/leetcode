class Solution:
    def findNumberIn2DArray(self, matrix,target):
        # 排序数组的查找，二分查找
        # # 先对行进行二分查找
        # row = matrix[0]
        # left = 0
        # right = len(row)-1
        # while right-left > 1:
        #     middle = (right-left)//2
        #     if row[middle] == target:
        #         return True
        #     elif row[middle] > target:
        #         right = middle
        #     else:
        #         left = middle
        
        # # 对列进行二分查找
        # column = [matrix[left][i] for i in range(len(matrix[0]))]
        # left = 0
        # right = len(column)-1
        # while right-left > 1:
        #     middle = (right-left)//2
        #     if column[middle] == target:
        #         return True
        #     elif column[middle] > target:
        #         right = middle
        #     else:
        #         left = middle
        # return False

        # 暴力解法
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == target:
        #             return True
        # return False       

        # 利用行列的特点
        pt1 = 0
        
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        pt2 = n-1
        if n == 0:
            return False
        while True:
            if matrix[pt1][pt2] == target:
                return True
            else:
                if pt2>0 and target <= matrix[pt1][pt2]: 
                    # 左移
                    pt2-=1
                elif pt1<m-1 and target >= matrix[pt1][pt2]: 
                    # 下沉
                    pt1+=1
                else:
                    return False


matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

target = 19
solu = Solution()
print(solu.findNumberIn2DArray(matrix,target))