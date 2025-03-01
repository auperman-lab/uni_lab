package lab3.com.restaurant.utils.bill;

import lab3.com.restaurant.service.order.OrderResult;

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
