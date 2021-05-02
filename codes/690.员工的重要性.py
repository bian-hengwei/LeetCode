#
# @lc app=leetcode.cn id=690 lang=python3
#
# [690] 员工的重要性

# @lc code=start
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from typing import List
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # store for better access using dictionary and then do depth first search
        namesList = {employee.id: employee for employee in employees}
        recGetImportance = lambda rId : namesList[rId].importance + sum(recGetImportance(subId) for subId in namesList[rId].subordinates)
        return recGetImportance(id)
# @lc code=end

