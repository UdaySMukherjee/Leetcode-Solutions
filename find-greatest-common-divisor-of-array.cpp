class Solution {
public:
    int findGCD(vector<int>& nums) {
        auto [m, x]=ranges::minmax(nums);
        return gcd(m, x); 
    }
};
