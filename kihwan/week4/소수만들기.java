public class 소수만들기 {

    private int[] nums;

    private int isPrime(int num) {
        if (num <= 2) {
            return num == 2 ? 1: 0;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return 0;
            }
        }
        return 1;
    }

    private int dfs(int start, int sum, int depth) {
        if (depth == 3) {
            return isPrime(sum);
        }
        int cnt = 0;
        for (int i = start; i < nums.length; i++) {
            cnt += dfs(i + 1, sum + nums[i],depth + 1);
        }
        return cnt;
    }

    public int solution(int[] nums) {
        this.nums = nums;
        return dfs(0, 0, 0);
    }

}
