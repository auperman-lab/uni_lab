package lab0.com.timetravel.timemachine;

public class TechnicalTimeMachine implements ITechnicalTimeMachine, ITimeMachine {

    private String vehicleName;
    private String model;
    private String motorModel;
    private String manufacturer;
    private int yearOfManufacture;

    // Constructor to initialize the properties
    public TechnicalTimeMachine(String vehicleName, String model, String motorModel, String manufacturer, int yearOfManufacture) {
        this.vehicleName = vehicleName;
        this.model = model;
        this.motorModel = motorModel;
        this.manufacturer = manufacturer;
        this.yearOfManufacture = yearOfManufacture;
    }

    @Override
    public String getVehicleName() {
        return vehicleName;
    }

    @Override
    public String getModel() {
        return model;
    }

    @Override
    public String getMotorModel() {
        return motorModel;
    }

    @Override
    public String getManufacturer() {
        return manufacturer;
    }

    @Override
    public int getYearOfManufacture() {
        return yearOfManufacture;
    }
}
