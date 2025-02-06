class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        all_pairs = combinations(nums, 2)
        pair_prods = starmap(mul, all_pairs) # get product of each pair
        prod_freqs = Counter(pair_prods).values() # frequencies of each product
        unique_tuples = sum(comb(freq, 2) for freq in prod_freqs) # sum of unique tuples for each product
        
        return 8 * unique_tuples # each unique tuple makes 8 tuples
