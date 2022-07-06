import java.util.*;

// 총 풀이 시간 1:07:25

public class 순위검색 {
    Map<String, List<Integer>> data = new HashMap<>();
    Map<String, Boolean> sortResult = new HashMap<>();

    // for memoization
    Map<String, Map<Integer, Integer>> cache = new HashMap<>();

    // DFS
    private void addInfo(String[] infos, String cur, int depth) {
        if (depth == infos.length - 1) { // 마지막 value 까지 도달
            if (!data.containsKey(cur)) {
                data.put(cur, new ArrayList<>());
                sortResult.put(cur, false);
                cache.put(cur, new HashMap<>());
            }
            data.get(cur).add(Integer.parseInt(infos[depth]));
            return;
        }
        addInfo(infos, cur + infos[depth], depth + 1); // info 데이터 그대로 가져가는 경우
        addInfo(infos, cur + "-", depth + 1); // info 데이터 없애고 wildcard 넣기
    }

    private int binarySearch(List<Integer> list, int target) {
        int left = 0, right = list.size() - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (list.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }

    private int getQueryResult(String query) {
        query = query.replace(" and ", "");
        String[] queries = query.split(" ");
        String category = queries[0];
        int score = Integer.parseInt(queries[1]);
        // 이미 검색된 적 있다면 그 결과 그대로 반환
        if (cache.containsKey(category) && cache.get(category).containsKey(score)) {
            return cache.get(category).get(score);
        }
        if (data.containsKey(category) == false) { return 0; }
        List<Integer> scores = data.get(category);
        // Sort 되지 않은 경우 Sort 수행
        if (sortResult.get(category) == false) {
            Collections.sort(scores);
            sortResult.replace(category, true);
        }
        int index = binarySearch(scores, score);
        int result = scores.size() - index;
        cache.get(category).put(score, result);
        return result;
    }

    public int[] solution(String[] infos, String[] queries) {
        int[] answer = new int[queries.length];
        // infos 배열 원소에 대해 대응될 수 있는 query의 모든 경우의 수를 찾는다
        for (String info : infos) {
            addInfo(info.split(" "), "",0);
        }
        // 탐색
        for (int i = 0; i < queries.length; i++) {
            answer[i] = getQueryResult(queries[i]);
        }
        return answer;
    }

}
