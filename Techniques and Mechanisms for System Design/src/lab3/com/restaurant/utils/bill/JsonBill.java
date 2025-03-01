package lab3.com.restaurant.utils.bill;

import lab3.com.restaurant.service.order.OrderResult;

import java.util.List;


public class JsonBill extends BaseBillDecorator {

    public JsonBill(IBill bill) {
        super(bill);
    }

    @Override
    public String printBill(List<OrderResult> orderResults) {


        double totalBill = 0.0;
        StringBuilder jsonBuilder = new StringBuilder();

        jsonBuilder.append("{\n");
        jsonBuilder.append("\"BillDetails\": [\n");

        for (int i = 0; i < orderResults.size(); i++) {
            OrderResult orderResult = orderResults.get(i);
            jsonBuilder.append("  {\n");
            jsonBuilder.append("    \"orderInfo\": \"").append(orderResult.orderInfo()).append("\",\n");
            jsonBuilder.append("    \"orderPrice\": ").append(orderResult.orderPrice()).append("\n");
            jsonBuilder.append("  }");

            // Append a comma after each item except the last one
            if (i < orderResults.size() - 1) {
                jsonBuilder.append(",");
            }
            jsonBuilder.append("\n");

            totalBill += orderResult.orderPrice();
        }

        jsonBuilder.append("],\n");
        jsonBuilder.append(String.format("\"TotalAmountDue\": %.2f\n", totalBill));
        jsonBuilder.append("}");

        return jsonBuilder.toString() + super.printBill(orderResults);
    }

}
