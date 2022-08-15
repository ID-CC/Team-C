import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class 파일명정렬2 {
    class Solution {
        public String[] solution(String[] files) {
            List<KakaoFile> kFiles = new ArrayList<>();
            for (String file : files) {
                final String number = getNumber(file);
                kFiles.add(new KakaoFile(file, file.split(number)[0].toLowerCase(), Integer.parseInt(number)));
            }
            kFiles.sort((a, b) -> {
                if (a.head.equals(b.head)) {
                    return Integer.compare(a.number, b.number);
                }
                return a.head.compareTo(b.head);
            });
            return kFiles.stream().map(e -> e.name).toArray(String[]::new);
        }

        private String getNumber(String file) {
            Pattern pattern = Pattern.compile("[0-9]+");
            Matcher matcher = pattern.matcher(file);
            if (matcher.find()) {
                return matcher.group();
            }
            return "";
        }
    }

    class KakaoFile {
        public String name;
        public String head;
        public int number;

        public KakaoFile(String name, String head, int number) {
            this.name = name;
            this.head = head;
            this.number = number;
        }
    }
}
