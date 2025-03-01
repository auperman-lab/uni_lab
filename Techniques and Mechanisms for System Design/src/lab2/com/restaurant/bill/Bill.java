package lab2.com.restaurant.bill;

import lab2.com.restaurant.FoodComboDelivery;
import lab2.com.restaurant.models.interfaces.IBill;
import lab2.com.restaurant.order.OrderResult;

import java.util.List;

public class Bill implements IBill {

    public String printBill(List<OrderResult> orderResults) {

        double totalBill = 0.0;
        StringBuilder detailsBill = new StringBuilder();

        System.out.println("Bill Details:");
        for (OrderResult orderResult : orderResults) {
            detailsBill.append(orderResult.orderInfo());
            totalBill += orderResult.orderPrice();
        }

        return detailsBill + String.format("Total Amount Due: %.2f\n", totalBill);
    }
}
