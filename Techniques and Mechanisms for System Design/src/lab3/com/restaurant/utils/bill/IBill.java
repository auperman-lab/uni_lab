package lab3.com.restaurant.utils.bill;

import lab3.com.restaurant.service.order.OrderResult;

import java.util.List;

public interface IBill {
    String printBill(List<OrderResult> orders);
}
