import java.util.*;

public class 주차요금계산 {

    private static final int MAX_MINUTE = 1439;

    private Map<String, Car> cars = new HashMap<>();
    private List<String> carIds = new ArrayList<>();

    private int baseTime;
    private int baseFee;
    private int unitMinute;
    private int unitFee;

    public static int toMinute(String time) {
        String[] times = time.split(":");
        return Integer.parseInt(times[0]) * 60 + Integer.parseInt(times[1]);
    }

    private void init(int[] fees) {
        baseTime = fees[0];
        baseFee = fees[1];
        unitMinute = fees[2];
        unitFee = fees[3];
    }

    private void parseRecords(String[] records) {
        for (String record : records) {
            String parsed[] = record.split(" ");
            int time = toMinute(parsed[0]);
            String carId = parsed[1];
            Car car;
            if (!cars.containsKey(carId)) {
                car = new Car(carId);
                carIds.add(carId);
                cars.put(carId, car);
            }
            car = cars.get(carId);
            if (parsed[2].equals("IN")) {
                car.in(time);
            } else {
                car.out(time);
            }
        }
    }

    private int getFee(int totalParkTime) {
        if (totalParkTime <= baseTime) {
            return baseFee;
        }
        return (int) (baseFee + (Math.ceil((totalParkTime - baseTime) / (unitMinute * 1.0)) * unitFee));
    }

    public int[] solution(int[] fees, String[] records) {
        init(fees);
        parseRecords(records);

        Collections.sort(carIds);

        int[] answer = new int[carIds.size()];
        for (int i = 0; i < carIds.size(); i++) {
            answer[i] = getFee(cars.get(carIds.get(i)).getTotalParkTime());
        }
        return answer;
    }

    public class Car {
        private String id;
        private boolean isParking = false;
        private int lastInTime = 0;
        private int totalParkTime = 0;
        public Car(String id) {
            this.id = id;
        }
        public String getId() {
            return id;
        }
        public void in(int inTime) {
            lastInTime = inTime;
            isParking = true;
        }
        public void out(int outTime) {
            totalParkTime += outTime - lastInTime;
            isParking = false;
        }
        public int getTotalParkTime() {
            if (isParking) {
                return totalParkTime + (MAX_MINUTE - lastInTime);
            }
            return totalParkTime;
        }
    }

}
