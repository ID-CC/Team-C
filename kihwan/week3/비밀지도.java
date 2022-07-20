import java.util.ArrayList;
import java.util.List;

// 풀이시간 : 7분 12초
public class 비밀지도 {

    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(arr1[i] | arr2[i]);
        }
        for (int i = 0; i < list.size(); i++) {
            int val = list.get(i);
            String result = "";
            while (val > 0) {
                if ((val & 1) == 1) {
                    result = "#" + result;
                } else {
                    result = ' ' + result;
                }
                val = val >> 1;
            }
            while (result.length() < n) {
                result = ' ' + result;
            }
            answer[i] = result;
        }
        return answer;
    }

}
