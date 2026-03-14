# # Intuition
# - 深拷貝 (Deep Copy) 的概念
# - 考試要看你能不能建立一個「完全獨立」的新圖。
# - 修改新圖不會影響舊圖，這就是深拷貝。

# # Approach
# 建立一個「完全獨立但結構相同」的圖，也就是 深拷貝 (deep copy)。
# 關鍵技術
# - 圖的遍歷：使用 DFS（深度優先）或 BFS（廣度優先）來走訪整個圖。
# - HashMap 映射：記錄「原節點 → 新節點」，避免重複建立，也防止陷入環。

# # Complexity
# - Time complexity:O(V+E)
# - Space complexity:O(V+E)
# Perfect optimal complexity achieved; no further algorithmic changes needed.

# language: Python
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        visited = {}  # HashMap: 原節點 -> 新節點

        def dfs(n):
            if n in visited:          # 如果已經複製過，直接回傳
                return visited[n]

            copy = Node(n.val)        # 建立新節點
            visited[n] = copy         # 記錄映射關係

            for nei in n.neighbors:   # 遞迴複製鄰居
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)

        