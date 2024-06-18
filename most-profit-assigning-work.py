class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Create a list of jobs with their difficulty and profit
        jobs = list(zip(difficulty, profit))
    
        # Sort jobs by difficulty
        jobs.sort()
    
        # Sort workers by their abilities
        worker.sort()
    
        max_profit = 0
        total_profit = 0
        job_index = 0
        n = len(jobs)
    
        for ability in worker:
            # While the worker can do the current job (based on difficulty)
            while job_index < n and ability >= jobs[job_index][0]:
                max_profit = max(max_profit, jobs[job_index][1])
                job_index += 1
            # Add the highest profit job that this worker can complete
            total_profit += max_profit
    
        return total_profit
