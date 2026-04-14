from scipy.optimize import linprog
import numpy as np

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n = len(robot)
        m = len(factory)
    
        # 1. Costs: flattened array of all |robot_i - factory_j|
        costs = []
        for r in robot:
            for f_pos, limit in factory:
                costs.append(abs(r - f_pos))
            
        # 2. Equality Constraints: Each robot assigned to 1 factory
        # A_eq * x = b_eq
        A_eq = np.zeros((n, n * m))
        for i in range(n):
            A_eq[i, i*m : (i+1)*m] = 1
        b_eq = np.ones(n)
    
        # 3. Inequality Constraints: Factory capacity limits
        # A_ub * x <= b_ub
        A_ub = np.zeros((m, n * m))
        for j in range(m):
            for i in range(n):
                A_ub[j, i*m + j] = 1
        b_ub = [f[1] for f in factory]
    
        # 4. Solve using the Simplex or Interior-Point method
        res = linprog(costs, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method='highs')
    
        return int(round(res.fun))        
