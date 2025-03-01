package lab0.com.timetravel.booking;

import lab0.com.timetravel.timeperiod.ITimePeriod;
import lab0.com.timetravel.traveler.ITraveler;

import java.time.LocalDateTime;

public class Booking {
    private String bookingId;
    private ITraveler traveler;
    private ITimePeriod timePeriod;
    private LocalDateTime bookingDateTime;
    private double totalPrice;

    // Constructor
    public Booking(String bookingId, ITraveler traveler, ITimePeriod timePeriod, LocalDateTime bookingDateTime, double totalPrice) {
        this.bookingId = bookingId;
        this.traveler = traveler;
        this.timePeriod = timePeriod; //Dependency Inversion Principle
        this.bookingDateTime = bookingDateTime;
        this.totalPrice = totalPrice;
    }

    public String getBookingId() {
        return bookingId;
    }

    public void setBookingId(String bookingId) {
        this.bookingId = bookingId;
    }

    public void setTraveler(ITraveler traveler) {
        this.traveler = traveler;
    }

    public void setTimePeriod(ITimePeriod timePeriod) {
        this.timePeriod = timePeriod;
    }

    public void setBookingDateTime(LocalDateTime bookingDateTime) {
        this.bookingDateTime = bookingDateTime;
    }

    public void setTotalPrice(double totalPrice) {
        this.totalPrice = totalPrice;
    }

    public String displayBookingDetails() {
        return "Booking ID: " + bookingId +
                "\nTraveler: " + traveler.getName() +
                "\nMachine: "+ traveler.getTimeMachine().getModel()+
                "\nTime Period: " + timePeriod.getName() +
                "\nBooking Date and Time: " + bookingDateTime +
                "\nTotal Price: $" + totalPrice;
    }
}
