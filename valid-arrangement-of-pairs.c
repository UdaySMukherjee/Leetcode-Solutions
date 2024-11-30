class Solution {
public:
    std::unordered_map<int, std::deque<int>> g;
    std::unordered_map<int, int> h;
    std::deque<std::vector<int>> ans;
public:
    void rx(int source) {
        while(not g[source].empty()) {
            int const dest = g[source].front(); g[source].pop_front();
            rx(dest);
            ans.push_front({source, dest});
        }
    }
    
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        int const n = pairs.size();
        for(std::vector<int> const &pair: pairs) { 
            g[pair[0]].push_back(pair[1]); 
            h[pair[0]] = h[pair[0]] - 1;
            h[pair[1]] = h[pair[1]] + 1;
        }
        int sv = INT_MAX, source = -1;
        for(std::pair<int const, int> const &node: h) {
            if(node.second < sv) {
                sv = node.second;
                source = node.first;
            }
        }
        rx(source);
        return std::vector<std::vector<int>>(ans.begin(), ans.end());
    }
};
