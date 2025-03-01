package lab1.com.restaurant;

import lab1.com.restaurant.order.AndyOrder;
import lab1.com.restaurant.order.OrderResult;
import lab1.com.restaurant.order.PlacinteOrder;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class FoodComboDelivery {
    private static volatile FoodComboDelivery instance;
    private AndyOrder andyOrder;
    private PlacinteOrder placinteOrder;
    private Bill bill;

    private FoodComboDelivery() {
        this.andyOrder = new AndyOrder();
        this.placinteOrder = new PlacinteOrder();
        this.bill = Bill.getInstance();

    }

    public static FoodComboDelivery getInstance() {
        FoodComboDelivery foodComboDelivery = instance;
        if (foodComboDelivery == null) {
            synchronized (FoodComboDelivery.class) {
                foodComboDelivery = instance;
                if (foodComboDelivery == null) {
                    instance = new FoodComboDelivery();
                }
            }
        }
        return instance;
    }

    public void start() {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;
        List<OrderResult> orderResults = new ArrayList<>();

        while (running) {
            System.out.println("1. Order Andy's Combo");
            System.out.println("2. Order La Placinte Combo");
            System.out.println("3. Print Bill");
            System.out.println("4. Exit");
            System.out.print("=> ");

            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    orderResults.add(andyOrder.order());
                    break;
                case 2:
                    orderResults.add(placinteOrder.order());
                    break;
                case 3:
                    bill.printBill(orderResults);
                    break;
                case 4:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid option, please try again.");

            }
        }
        scanner.close();
    }
}
