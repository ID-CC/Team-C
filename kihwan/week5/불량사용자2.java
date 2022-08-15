import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.Map;

public class 불량사용자2 {

    class Solution {

        private HashSet<HashSet<String>> answer;

        public int solution(String[] user_id, String[] banned_id) {
            answer = new HashSet<>();
            dfs(new LinkedHashSet<>(), user_id, banned_id);
            return answer.size();
        }


        /*
        유저를 모든 경우의 수로 삽입된 순서를 보장하는 LinkedHashSet 에 담고, ban 여부 확인.
         */
        private void dfs(LinkedHashSet<String> set, String[] userIds, String[] banIds) {
            if (set.size() == banIds.length) {
                if (isBanList(set, banIds)) { // 유효한 리스트라면 불량 사용자 목록 추가
                    answer.add(new HashSet<>(set));
                }
                return;
            }
            for (String userId : userIds) {
                if (set.add(userId)) {
                    dfs(set, userIds, banIds);
                    set.remove(userId);
                }
            }
        }

        private boolean isBanList(LinkedHashSet<String> set, String[] banIds) {
            int idx = 0;
            for (String id : set) {
                String banId = banIds[idx++];
                if (id.length() != banId.length()) {
                    return false;
                }
                for (int i = 0; i < banId.length(); i++) {
                    if (banId.charAt(i) == '*') {
                        continue;
                    }
                    if (id.charAt(i) != banId.charAt(i)) {
                        return false;
                    }
                }
            }
            return true;
        }
    }
}
