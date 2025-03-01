package lab2.com.restaurant.bill;

import lab2.com.restaurant.models.interfaces.IBill;
import lab2.com.restaurant.order.OrderResult;

import java.util.List;
import java.util.HashMap;

public class BillProxy implements IBill {
    private final IBill realBill;  // Real object
    private HashMap<List<OrderResult>, String> cachedBill;

    public BillProxy(IBill realBill) {
        this.realBill = realBill;
        this.cachedBill = new HashMap<>();
    }

    @Override
    public String printBill(List<OrderResult> orderResults) {
        if (cachedBill.get(orderResults) == null) {
            System.out.println("Generating and caching the bill...");
            cachedBill.put(orderResults, realBill.printBill(orderResults));
        }else{
            System.out.println("Bill already cached!");
        }
        return cachedBill.get(orderResults);
    }

}