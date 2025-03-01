package lab0.com.timetravel.main;

import lab0.com.timetravel.booking.Booking;
import lab0.com.timetravel.timemachine.ITimeMachine;
import lab0.com.timetravel.timemachine.TechnicalTimeMachine;
import lab0.com.timetravel.timeperiod.AncientRome;
import lab0.com.timetravel.timeperiod.ITimePeriod;
import lab0.com.timetravel.traveler.ChronoExplorerTraveler;
import lab0.com.timetravel.traveler.ITraveler;

import java.time.LocalDateTime;

public class App {
    public static void main(String[] args) {
        LocalDateTime bookingDateTime = LocalDateTime.now(); // Current date and time

        ITimePeriod timePeriod = new AncientRome();

        ITimeMachine tardis = new TechnicalTimeMachine("TARDIS", "40 TARDIS", "Eye of Harmony", "Verity Lambert", 42);

        ITraveler doctor = new ChronoExplorerTraveler("Doctor Who", "Moder Era", tardis);

        Booking booking  = new Booking("69", doctor, timePeriod, bookingDateTime, 11 );

        System.out.println(booking.displayBookingDetails());
    }
}
