package lab3.com.restaurant.utils.bill;

import lab3.com.restaurant.service.order.OrderResult;

import java.util.List;

public class XmlBill extends BaseBillDecorator {
    public XmlBill(IBill bill) {
        super(bill);
    }

    @Override
    public String printBill(List<OrderResult> orderResults) {

        double totalBill = 0.0;
        StringBuilder xmlBuilder = new StringBuilder();

        xmlBuilder.append("<Bill>\n");

        xmlBuilder.append("  <BillDetails>\n");
        for (OrderResult orderResult : orderResults) {
            xmlBuilder.append("    <Order>\n");
            xmlBuilder.append("      <OrderInfo>").append(orderResult.orderInfo()).append("</OrderInfo>\n");
            xmlBuilder.append("      <OrderPrice>").append(orderResult.orderPrice()).append("</OrderPrice>\n");
            xmlBuilder.append("    </Order>\n");

            totalBill += orderResult.orderPrice();
        }
        xmlBuilder.append("  </BillDetails>\n");

        xmlBuilder.append(String.format("  <TotalAmountDue>%.2f</TotalAmountDue>\n", totalBill));
        xmlBuilder.append("</Bill>");

        return xmlBuilder.toString() +  super.printBill(orderResults);
    }


}
