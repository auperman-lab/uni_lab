package lab0.com.timetravel.timeperiod;

import java.time.LocalDate;

public interface ITimePeriod {


    // Get the start date of the time period
    LocalDate getStartDate();

    // Get the end date of the time period
    LocalDate getEndDate();

    // Get the name of the time period
    String getName();

    // Get the description of the time period
    String getDescription();




}
