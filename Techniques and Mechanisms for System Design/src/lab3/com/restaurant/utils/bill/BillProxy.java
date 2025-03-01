package lab3.com.restaurant.utils.bill;

import lab3.com.restaurant.service.order.OrderResult;

import java.util.HashMap;
import java.util.List;

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