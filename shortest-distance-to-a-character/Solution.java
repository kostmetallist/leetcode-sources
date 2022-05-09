class Solution {
    public int[] shortestToChar(String S, char C) {
        int N = S.length();
        int[] ans = new int[N];
        int prev = -1;

        for (int i = 0; i < N; ++i) {
            if (S.charAt(i) == C) prev = i;
            ans[i] = (prev != -1)? (i - prev): N;
        }

        prev = -1;
        for (int i = N-1; i >= 0; --i) {
            if (S.charAt(i) == C) prev = i;
            ans[i] = (prev != -1)? Math.min(ans[i], prev - i): ans[i];
        }

        return ans;
    }
}
