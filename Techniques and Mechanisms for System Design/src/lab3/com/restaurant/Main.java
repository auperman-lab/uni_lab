package lab3.com.restaurant;

import lab3.com.restaurant.controller.FoodComboDelivery;

public class Main {
    public static void main(String[] args) {
        FoodComboDelivery foodComboDelivery = FoodComboDelivery.getInstance();

        foodComboDelivery.start();
    }
}