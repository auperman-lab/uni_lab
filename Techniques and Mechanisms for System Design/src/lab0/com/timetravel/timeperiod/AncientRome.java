package lab0.com.timetravel.timeperiod;

import java.time.LocalDate;

public class AncientRome implements ITimePeriod{

    // Single Responsibility Principle


    @Override
    public LocalDate getStartDate() {
        return LocalDate.of(753, 4, 21); // Founding of Rome
    }

    @Override
    public LocalDate getEndDate() {
        return LocalDate.of(476, 9, 4); // Fall of Western Roman Empire
    }

    @Override
    public String getName() {
        return "Ancient Rome";
    }

    @Override
    public String getDescription() {
        return "A civilization that dominated the Mediterranean region and contributed significantly to law, politics, engineering, and architecture.";
    }


}
