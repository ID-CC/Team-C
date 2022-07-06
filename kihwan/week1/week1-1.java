/*
총 풀이시간 : 22분 36초
 */

public class NewIdRecommend {

    static class Solution {

        private String toLowerCase(String new_id) {
            return new_id.toLowerCase();
        }

        private boolean isLowerAlpha(char chr) {
            return (chr >= 'a' && chr <= 'z');
        }

        private boolean isNumber(char chr) {
            return (chr >= '0' && chr <= '9');
        }

        private boolean isAllowedSpecialChr(char chr) {
            return chr == '-' || chr == '_' || chr == '.';
        }

        private boolean isValidChar(char chr) {
            return isLowerAlpha(chr) || isNumber(chr) || isAllowedSpecialChr(chr);
        }

        private String removeIllegalChar(String new_id) {
            StringBuilder builder = new StringBuilder();
            for (int i = 0; i < new_id.length(); i++) {
                if (isValidChar(new_id.charAt(i))) {
                    builder.append(new_id.charAt(i));
                }
            }
            return builder.toString();
        }

        private String removeContinuousDot(String new_id) {
            int len = 0;
            while (len != new_id.length()) {
                len = new_id.length();
                new_id = new_id.replace("..", ".");
            }
            return new_id;
        }

        private String removeIllegalDots(String new_id) {
            if (new_id.isEmpty()) {
                return new_id;
            }
            if (new_id.charAt(0) == '.') {
                new_id = new_id.substring(1);
            }
            if (!new_id.isEmpty() && new_id.charAt(new_id.length() - 1) == '.') {
                new_id = new_id.substring(0, new_id.length() - 1);
            }
            return new_id;
        }

        private String removeOverLenChr(String new_id) {
            if (new_id.length() >= 16) {
                new_id = new_id.substring(0, 15);
                new_id = removeIllegalDots(new_id);
            }
            return new_id;
        }

        public String solution(String new_id) {
            String answer = new_id;
            answer = toLowerCase(answer);
            answer = removeIllegalChar(answer);
            answer = removeContinuousDot(answer);
            answer = removeIllegalDots(answer);
            if (answer.isEmpty()) {
                answer = "a";
            }
            answer = removeOverLenChr(answer);
            while (answer.length() < 3) {
                answer += answer.charAt(answer.length() - 1);
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        String[] params = {
//            "...!@BaT#*..y.abcdefghijklm",
//            "z-+.^.",
            "=.=",
            "123_.def",
            "abcdefghijklmn.p"
        };
        for (int i = 0; i < params.length; i++) {
            String answer = new Solution().solution(params[i]);
            System.out.println(answer);
        }
    }

}
