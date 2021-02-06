import collections


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        graph = collections.defaultdict(list)
        for u, v in prerequisites: # inverse the graph
            graph[u].append(v)
        # 0 = Unknown, 1 = visiting, 2 = visited
        visited = [0] * numCourses
        path = []
        for i in range(numCourses):
            if self.dfs(graph, visited, i, path):
                return []
        return path

    def dfs(self, graph, visited, i, path):
        if visited[i] == 1: return True     # End if cyclic
        if visited[i] == 2: return False    # Skip if visited
        visited[i] = 1
        for j in graph[i]:
            if self.dfs(graph, visited, j, path): # check if there is a cycle (True)
                return True                       # or if it is the deepest (False)
        visited[i] = 2  # on its way out of backtrack
        path.append(i)  # everything should be "visited"
        return False

ob = Solution()
print(ob.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))


