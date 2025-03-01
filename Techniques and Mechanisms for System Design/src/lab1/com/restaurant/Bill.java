package lab1.com.restaurant;

import lab1.com.restaurant.order.OrderResult;

import java.util.List;

public class Bill {
    public static volatile Bill instance;

    public static Bill getInstance() {
        Bill bill = instance;
        if (bill == null) {
            synchronized (FoodComboDelivery.class) {
                bill = instance;
                if (bill == null) {
                    instance = new Bill();
                }
            }
        }
        return instance;
    }

    public void printBill(List<OrderResult> orderResults) {
        if (orderResults.isEmpty()) {
            System.out.println("No orders placed yet.");
            return;
        }

        double totalBill = 0.0; // Initialize total bill

        System.out.println("Bill Details:");
        for (OrderResult orderResult : orderResults) {
            System.out.println(orderResult.orderInfo()); // Print order info
            totalBill += orderResult.orderPrice(); // Sum up the total price
        }

        System.out.printf("Total Amount Due: %.2f\n", totalBill); // Print total amount
    }
}
