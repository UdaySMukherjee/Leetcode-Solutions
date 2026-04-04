import numpy as np

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if not encodedText: return ""
        
        n = len(encodedText)
        cols = n // rows
        
        # 1. Generate the coordinate grid for all potential diagonal elements
        # r_idx: [0, 1, ..., rows-1]
        # k_idx: [0, 1, ..., cols-1]
        r_idx = np.arange(rows).reshape(-1, 1)
        k_idx = np.arange(cols).reshape(1, -1)
        
        # 2. Vectorized Index Calculation: r(C+1) + k
        # This creates a grid where each column represents one 'slanted' diagonal
        indices = r_idx * (cols + 1) + k_idx
        
        # 3. The Structural Mask
        # A diagonal starting at k only exists while col (k+r) < cols
        mask = (k_idx + r_idx < cols)
        
        # 4. Extract valid indices in diagonal-first order
        # We transpose so that we read all of diagonal 0, then diagonal 1, etc.
        flat_indices = indices.T[mask.T]
        
        # 5. Vectorized character extraction
        # We convert to a NumPy byte array for O(1) character access
        arr = np.frombuffer(encodedText.encode(), dtype='S1')
        
        # Join, decode, and trim the trailing spaces
        return arr[flat_indices].tobytes().decode().rstrip()     
