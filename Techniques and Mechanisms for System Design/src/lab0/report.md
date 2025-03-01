# SOLID Principles

## Author: Danu Macrii

----

## Objectives:
* To understand and apply the SOLID principles of object-oriented design
* To implement 2 SOLID principles in code

## Used Design Patterns:
* S - Single Responsibility Principle
* I - Interface Segregation Principle
* D - Dependency Inversion Principle


## Implementation

### Single Responsibility Principle
- **AncientRome**: Implements the `ITimePeriod` interface, it is responding for time period related methods and attributes, keeping only one job .

```java
public class AncientRome implements ITimePeriod {
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
```

###  Interface Segregation Principle

- **ITechnicalTimeMachine**  is an interface related to `ITimeMachine` and thus doesn't force the client to implement methods it doesnt use 


```java

public class TechnicalTimeMachine implements ITechnicalTimeMachine, ITimeMachine {}

```
```java
public interface ITimeMachine {
    String getVehicleName();
    String getModel();
    String getManufacturer();
    int getYearOfManufacture();
}


public interface ITechnicalTimeMachine {
    String getMotorModel();
}

```

### Dependency Inversion Principle

- **Booking** class instead of directly addressing `Traveler` class, it depends on abstraction of this class


```java
 public Booking(String bookingId, ITraveler traveler, ITimePeriod timePeriod, LocalDateTime bookingDateTime, double totalPrice) {
        this.bookingId = bookingId;
        this.traveler = traveler;//Dependency Inversion Principle
        this.timePeriod = timePeriod; 
        this.bookingDateTime = bookingDateTime;
        this.totalPrice = totalPrice;
    }

```

## Conclusions / Screenshots / Results



In this lab, I  applied SOLID principles, enhancing code maintainability and flexibility. By enforcing single
responsibility, segregating interfaces, and utilizing dependency inversion, I created a  time-travel booking system what
can grow and adapt to demand. These practices promote cleaner code, easier updates, and a scalable architecture, equipping
us for future software development challenges.