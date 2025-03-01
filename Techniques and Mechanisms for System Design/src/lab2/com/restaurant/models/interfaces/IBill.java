package lab2.com.restaurant.models.interfaces;

import lab2.com.restaurant.order.OrderResult;

import java.util.List;

public interface IBill {
    String printBill(List<OrderResult> orders);
}
