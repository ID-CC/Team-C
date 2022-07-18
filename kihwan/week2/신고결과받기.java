import java.util.*;

// 풀이 시간 : 42분
public class 신고결과받기 {

    Map<String, Set<String>> reportHistory = new LinkedHashMap<>();
    Map<String, Integer> mailHistory = new LinkedHashMap<>();

    private void init(String[] id_list) {
        reportHistory.clear();
        mailHistory.clear();

        for (String id : id_list) {
            reportHistory.put(id, new HashSet<>());
            mailHistory.put(id, 0);
        }
    }

    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        init(id_list);

        Set<String> filteredReport = new HashSet<>();
        for (String rpt : report) {
            // 한 사람이 여러번 신고한 경우 필터링
            if (!filteredReport.contains(rpt)) {
                filteredReport.add(rpt);
            }
        }

        // 정지 대상
        List<String> blockTargets = new ArrayList<>();
        Iterator<String> rptIter = filteredReport.iterator();
        while (rptIter.hasNext()) {
            String[] parsed = rptIter.next().split(" ");
            String reporter = parsed[0];
            String target = parsed[1];
            Set<String> reporters = reportHistory.get(target);
            // 중복 체크
            if (!reporters.contains(reporter)) {
                reporters.add(reporter);
                // 정지 대상만 필터링
                if (reporters.size() == k) {
                    blockTargets.add(target);
                }
            }
        }
        for (String blockTarget : blockTargets) {
            Set<String> reporters = reportHistory.get(blockTarget);
            Iterator<String> iter = reporters.iterator();
            while (iter.hasNext()) {
                String id = iter.next();
                mailHistory.replace(id, mailHistory.get(id) + 1);
            }
        }
        int i = 0;
        for (int ret : mailHistory.values()) {
            answer[i++] = ret;
        }
        return answer;
    }

}
