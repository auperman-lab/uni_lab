package lab1.com.restaurant;

public class Main {
    public static void main(String[] args) {
        FoodComboDelivery foodComboDelivery = FoodComboDelivery.getInstance();

        foodComboDelivery.start();
    }
}