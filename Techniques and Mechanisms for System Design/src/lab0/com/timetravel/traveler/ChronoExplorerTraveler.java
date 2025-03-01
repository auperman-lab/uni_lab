package lab0.com.timetravel.traveler;

import lab0.com.timetravel.timemachine.ITimeMachine;

public class ChronoExplorerTraveler implements ITraveler {

    private String name;
    private String currentTimePeriod;
    private ITimeMachine timeMachine;


    // Constructor
    public ChronoExplorerTraveler(String name, String currentTimePeriod, ITimeMachine timeMachine) {
        this.name = name;
        this.currentTimePeriod = currentTimePeriod;
        this.timeMachine = timeMachine;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public String getCurrentTimePeriod() {
        return currentTimePeriod;
    }

    @Override
    public ITimeMachine getTimeMachine() {
        return timeMachine;
    }

    @Override
    public void setCurrentTimePeriod(String timePeriod) {
        this.currentTimePeriod = timePeriod;
    }

    @Override
    public String displayTravelerDetails() {
        return "Traveler: " + name + "\nCurrent Time Period: " + currentTimePeriod ;
    }

    @Override
    public String displayTravelReason() {
        return "for fun i guess";
    }


}
