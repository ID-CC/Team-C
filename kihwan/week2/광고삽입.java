public class 광고삽입 {

    private long subtotal[];

    private int timeStrToSec(String timeStr) {
        String times[] = timeStr.split(":");
        int hour = Integer.parseInt(times[0]);
        int min = Integer.parseInt(times[1]);
        int sec = Integer.parseInt(times[2]);
        return hour * 3600 + min * 60 + sec;
    }

    private String secToTimeStr(int sec) {
        int hour = sec / 3600;
        int min = (sec % 3600) / 60;
        int s = (sec % 60);
        return (hour < 10 ? "0" : "") + hour + ":" +
                (min < 10 ? "0" : "") + min + ":" +
                (s < 10 ? "0" : "") + s;
    }

    public String solution(String play_time, String adv_time, String[] logs) {
        int playTime = timeStrToSec(play_time);
        int advTime = timeStrToSec(adv_time);
        // int 하니까 통과안됨
        subtotal = new long[playTime + 1];
        for (String log : logs) {
            String times[] = log.split("-");
            subtotal[timeStrToSec(times[0])]++;
            subtotal[timeStrToSec(times[1])]--;
        }
        // 시청자 카운팅
        for (int i = 1; i <= playTime; i++) {
            subtotal[i] += subtotal[i - 1];
        }
        // 시청시간 카운팅
        for (int i = 1; i <= playTime; i++) {
            subtotal[i] += subtotal[i - 1];
        }
        long maxWatchTime = subtotal[advTime];
        int maxStartTime = 0;
        for (int i = 0; i + advTime <= playTime; i++) {
            long watchTime = subtotal[i + advTime] - subtotal[i];
            if (watchTime > maxWatchTime) {
                maxStartTime = i + 1;
                maxWatchTime = watchTime;
            }
        }
        return secToTimeStr(maxStartTime);
    }

}
