class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st_cou = Counter(students)
        sw_cou = Counter(sandwiches)
        size = len(students)
        if st_cou[0] == sw_cou[0] and st_cou[1] == sw_cou[1]:
            return 0
        for step in range(size):
            cur = sandwiches[step]
            if st_cou[cur] == 0:
                ind = step
                break
            sw_cou[cur] -= 1
            st_cou[cur] -= 1
        return size - ind
