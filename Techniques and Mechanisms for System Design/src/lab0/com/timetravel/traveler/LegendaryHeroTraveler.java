package lab0.com.timetravel.traveler;

import lab0.com.timetravel.timemachine.ITimeMachine;

public class LegendaryHeroTraveler implements ITraveler {
    private String name;
    private String currentTimePeriod;
    private ITimeMachine timeMachine;

    // Constructor
    public LegendaryHeroTraveler(String name, String currentTimePeriod, ITimeMachine timeMachine) {
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
        return "Traveler: " + name + "\nCurrent Time Period: " + currentTimePeriod + "\n with " + timeMachine.getVehicleName();
    }

    @Override
    public String displayTravelReason() {
        return "slay the dragon";
    }

}
