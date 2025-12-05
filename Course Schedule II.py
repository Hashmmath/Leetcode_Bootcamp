from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        in_degree = [0] * numCourses
      
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            in_degree[course] += 1
      
        result = []
        queue = deque([course for course, degree in enumerate(in_degree) if degree == 0])
      
        while queue:
            current_course = queue.popleft()
            result.append(current_course)
          
            for dependent_course in graph[current_course]:
                in_degree[dependent_course] -= 1
                if in_degree[dependent_course] == 0:
                    queue.append(dependent_course)
      
        return result if len(result) == numCourses else []