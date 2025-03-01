package lab2.com.restaurant.bill;

import lab2.com.restaurant.models.interfaces.IBill;
import lab2.com.restaurant.order.OrderResult;

import java.util.List;

public class BaseBillDecorator implements IBill {
    public final IBill wrapper;

    public BaseBillDecorator(IBill wrapper) {
        this.wrapper = wrapper;
    }



    @Override
    public String printBill(List<OrderResult> orders) {
        if (orders.isEmpty()) {
            return "No orders placed yet.";
        }
        return wrapper.printBill(orders);
    }
}
