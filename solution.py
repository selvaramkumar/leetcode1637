class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[0])
        k=[]
        for i in range (0, len(points)):
            j=i+1
            if j != len(points):
                k.append(points[j][0]-points[i][0])
        k.sort(reverse=True)
        return k[0]

points=[[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(Solution().maxWidthOfVerticalArea(points))
