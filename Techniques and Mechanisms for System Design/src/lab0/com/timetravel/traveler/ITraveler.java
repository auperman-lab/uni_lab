package lab0.com.timetravel.traveler;

import lab0.com.timetravel.timemachine.ITimeMachine;

public interface ITraveler {
    String getName();
    String getCurrentTimePeriod();
    ITimeMachine getTimeMachine();
    void setCurrentTimePeriod(String timePeriod);
    String displayTravelerDetails();
    String displayTravelReason();
}
