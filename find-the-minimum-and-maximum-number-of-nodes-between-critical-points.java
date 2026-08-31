/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        if(head.next==null || head.next.next==null) return new int[]{-1,-1};
        ListNode first=head;
        ListNode mid=first.next;
        ListNode last=mid.next;
        // mid=mid.next;
        // last=last.next.next;
        List<Integer>list = new ArrayList<>();
        int i=1;
        while(last!=null){
            if(first.val<mid.val && mid.val>last.val){
                list.add(i);
            }
            if(first.val>mid.val && mid.val<last.val){
                list.add(i);
            }
            i++;
            first=mid;
            mid=last;
            last=last.next;
        }
        if(list.size()<2) return new int[]{-1,-1};;
        int[] ans = new int[2];
        ans[0]=Integer.MAX_VALUE;
        for(int j=0;j<list.size()-1;j++){
            ans[0]=Math.min(ans[0],list.get(j+1)-list.get(j));
        }
        ans[1]=list.get(list.size()-1)-list.get(0);
        return ans;

    }
}
