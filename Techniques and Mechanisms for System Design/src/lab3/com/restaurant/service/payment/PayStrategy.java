package lab3.com.restaurant.service.payment;

public interface PayStrategy {
    boolean pay(float paymentAmount);
    void collectPaymentDetails();
}
