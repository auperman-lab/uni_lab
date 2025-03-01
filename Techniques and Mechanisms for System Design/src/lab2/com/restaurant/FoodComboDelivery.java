package lab2.com.restaurant;

import lab2.com.restaurant.bill.Bill;
import lab2.com.restaurant.bill.BillProxy;
import lab2.com.restaurant.bill.JsonBill;
import lab2.com.restaurant.bill.XmlBill;
import lab2.com.restaurant.models.interfaces.IBill;
import lab2.com.restaurant.order.AndyOrder;
import lab2.com.restaurant.order.CremeOrder;
import lab2.com.restaurant.order.OrderResult;
import lab2.com.restaurant.order.PlacinteOrder;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class FoodComboDelivery {
    private static volatile FoodComboDelivery instance;
    private final AndyOrder andyOrder;
    private final PlacinteOrder placinteOrder;
    private final CremeOrder cremeOrder;
    private final IBill bill;

    private FoodComboDelivery() {
        this.andyOrder = new AndyOrder();
        this.placinteOrder = new PlacinteOrder();
        this.cremeOrder = new CremeOrder();

        IBill realBill = new JsonBill(
                new XmlBill(
                        new Bill()
                )
        );
        this.bill = new BillProxy(realBill);


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
            System.out.println("3. Order La Creme de la Creme Combo");
            System.out.println("4. Print Bill");
            System.out.println("5. Exit");
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
                    orderResults.add(cremeOrder.order());
                    break;
                case 4:
                    System.out.println(bill.printBill(orderResults));
                    break;
                case 5:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid option, please try again.");

            }
        }
        scanner.close();
    }
}
