#
# @lc app=leetcode.cn id=1723 lang=python3
#
# [1723] 完成所有工作的最短时间

# @lc code=start
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # global variables that remains the same during dfs
        # maximum amount of days needed
        self.res = math.inf
        # jobs array
        self.jobs = sorted(jobs, reverse=True)
        # No. of workers
        self.k = k
        # workers' hours
        self.solutions = [0 for _ in range(k)]

        # perform dfs on job0, busy0, time0
        self.dfs(0, 0, 0)
        return self.res
        
    def dfs(self, job, busy, time):
        # cut branches where new time exceeds current result
        if time >= self.res: return
        # update current result only if all jobs are assigned
        if job == len(self.jobs): 
            self.res = time
            return
        # assign to free workers first
        if busy < self.k:
            self.solutions[busy] = self.jobs[job]
            self.dfs(job + 1, busy + 1, max(self.solutions[busy], time))
            self.solutions[busy] = 0
        # assign to all busy workers
        for i in range(busy):
            self.solutions[i] += self.jobs[job]
            self.dfs(job + 1, busy, max(self.solutions[i], time))
            self.solutions[i] -= self.jobs[job]
# @lc code=end

