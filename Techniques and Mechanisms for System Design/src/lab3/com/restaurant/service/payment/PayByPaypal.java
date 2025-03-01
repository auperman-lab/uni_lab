package lab3.com.restaurant.service.payment;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class PayByPaypal implements PayStrategy {
    private final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private boolean signedIn;

    @Override
    public void collectPaymentDetails() {
        try {
            while (!signedIn) {
                System.out.print("Enter the user's email: ");
                String email = READER.readLine();
                System.out.print("Enter the password: ");
                String password = READER.readLine();
                if (verify(email, password)) {
                    System.out.println("Data verification has been successful.");
                } else {
                    System.out.println("Wrong email or password!");
                }
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    private boolean verify(String email, String password) {
        System.out.println("checking"+ email);
        System.out.println("checking"+ password);
        System.out.println("valid");
        setSignedIn(true);
        return signedIn;
    }

    @Override
    public boolean pay(float paymentAmount) {
        if (signedIn) {
            System.out.println("Paying " + paymentAmount + " using PayPal.");
            return true;
        } else {
            return false;
        }
    }

    private void setSignedIn(boolean signedIn) {
        this.signedIn = signedIn;
    }
}