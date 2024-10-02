class Solution {
    public int solution(int[] arr) {
      int answer = arr[0];
      for (int i : arr) {
        if (i != arr[0]) {
          answer = lcm(answer, i);
        }
      }
        
        return answer;
    }

    public static int gcd(int n1, int n2) {
      while (n2 > 0) {
        int r = n1 % n2;
        n1 = n2;
        n2 = r;
      }
      return n1;
    }

    public static int lcm(int n1, int n2) {
      return n1*n2/gcd(n1,n2);
    }
}