class Solution {
    public List<String> removeSubfolders(String[] folder) {
        List<String> ans = new ArrayList<>();
        Arrays.sort(folder);
        ans.add(folder[0]);
        int j = 0;
        for(int i = 1; i < folder.length ; i++) {
            String lastFolder = ans.get(j) + "/";
            if(!folder[i].startsWith(lastFolder)) {
                ans.add(folder[i]);
                j++;
            }
        }
        return ans;
    }
}
