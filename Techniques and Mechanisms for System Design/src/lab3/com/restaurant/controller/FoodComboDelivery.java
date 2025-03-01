package lab3.com.restaurant.controller;

import lab3.com.restaurant.service.payment.PayByCreditCard;
import lab3.com.restaurant.service.payment.PayByPaypal;
import lab3.com.restaurant.service.payment.PayStrategy;
import lab3.com.restaurant.utils.bill.Bill;
import lab3.com.restaurant.utils.bill.BillProxy;
import lab3.com.restaurant.utils.bill.JsonBill;
import lab3.com.restaurant.utils.bill.XmlBill;
import lab3.com.restaurant.utils.bill.IBill;
import lab3.com.restaurant.service.order.AndyOrder;
import lab3.com.restaurant.service.order.CremeOrder;
import lab3.com.restaurant.service.order.OrderResult;
import lab3.com.restaurant.service.order.PlacinteOrder;

import java.util.*;

public class FoodComboDelivery {
    private static volatile FoodComboDelivery instance;
    private final AndyOrder andyOrder;
    private final PlacinteOrder placinteOrder;
    private final CremeOrder cremeOrder;
    private final IBill bill;
    private static PayStrategy strategy;
    private List<OrderResult> orderResults;
    private Deque<FCDMemento> stateHistory;


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

        this.stateHistory = new ArrayDeque<>(3);


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
        orderResults = new ArrayList<>();

        while (running) {
            System.out.println("1. Order Andy's Combo");
            System.out.println("2. Order La Placinte Combo");
            System.out.println("3. Order La Creme de la Creme Combo");
            System.out.println("4. Print Bill");
            System.out.println("5. Pay Order");
            System.out.println("6. CTRL Z");
            System.out.println("7. Exit");
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
                    if (strategy == null) {
                        System.out.println("Please, select a payment method: \n" +
                                "1 - PalPay" + "\n" +
                                "2 - Credit Card");
                        int paymentMethod = scanner.nextInt();


                        if (paymentMethod == 1 ) {
                            strategy = new PayByPaypal();
                        } else {
                            strategy = new PayByCreditCard();
                        }
                    }
                    System.out.println(bill.printBill(orderResults));

                    float totalBill = 0;
                    for (OrderResult orderResult : orderResults) {
                        totalBill += orderResult.orderPrice();
                    }

                    strategy.collectPaymentDetails();
                    if (strategy.pay(totalBill)) {
                        System.out.println("Payment has been successful.");
                        orderResults.clear();
                    } else {
                        System.out.println("FAIL! Please, check your data.");
                    }


                    break;
                case 6:
                    restoreSnapshot(stateHistory.removeFirst());
                    break;
                case 7:
                    running = false;
                    break;
                default:
                    System.out.println("Invalid option, please try again.");

            }
            stateHistory.add(takeSnapshot());

        }
        scanner.close();
    }

    public FCDMemento takeSnapshot() {
        return new FCDMemento(orderResults);
    }

    public void restoreSnapshot(FCDMemento snapshot) {
        this.orderResults = new ArrayList<>(snapshot.getSavedOrder());
    }

    private class FCDMemento{
        private final  List<OrderResult> orderR;

        private FCDMemento(List<OrderResult> orderResults) {
            this.orderR = new ArrayList<>();
            for (OrderResult orderResult : orderResults) {
                this.orderR.add(orderResult.clone());
            }        }

        private  List<OrderResult> getSavedOrder() {
            return this.orderR;
        }


    }

}
