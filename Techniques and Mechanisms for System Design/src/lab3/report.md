# Behavioral Design Patterns

## Author: Danu Macrii

----

## Objectives:
- Study and understand the Behavioral Design Patterns.
- As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system.
- Implement some additional functionalities using behavioral design patterns.

## Used Design Patterns:
- Memento
- Strategy


## Memento
- Here is a memento that stores the state of food combo delivery system ,  specifically list of orders
```java
private class FCDMemento{
        private final  List<OrderResult> orderR;

        private FCDMemento(List<OrderResult> orderResults) {
            this.orderR = new ArrayList<>();
            for (OrderResult orderResult : orderResults) {
                this.orderR.add(orderResult.clone()); 
            }        }

        private  List<OrderResult> getSavedOrder() {
            return this.orderR;
        }
        
    }
```

- FoodComboDelivery has the methods and a history of changes , it saves the state at each iteration

```java
public class FoodComboDelivery {
    private Deque<FCDMemento> stateHistory;


    ...

    public FCDMemento takeSnapshot() {
        return new FCDMemento(orderResults);
    }

    public void restoreSnapshot(FCDMemento snapshot) {
        this.orderResults = new ArrayList<>(snapshot.getSavedOrder());
    }
}
```

- Now customer can get to the previous state of the order

```java
 case 6:
                    restoreSnapshot(stateHistory.removeFirst());
                    break;
```


### Strategy

- This is a payStrategy interface , and an example of its implimentation
```java
public interface PayStrategy {
    boolean pay(float paymentAmount);
    void collectPaymentDetails();
}


```

```java
public class PayByCreditCard implements PayStrategy {
    private final BufferedReader READER = new BufferedReader(new InputStreamReader(System.in));
    private CreditCard card;

    @Override
    public void collectPaymentDetails() {
        try {
            System.out.print("Enter the card number: ");
            String number = READER.readLine();
            System.out.print("Enter the card expiration date 'mm/yy': ");
            String date = READER.readLine();
            System.out.print("Enter the CVV code: ");
            String cvv = READER.readLine();
            card = new CreditCard(number, date, cvv);


        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    @Override
    public boolean pay(float paymentAmount) {
        if (cardIsPresent()) {
            System.out.println("Paying " + paymentAmount + " using Credit Card.");
            card.setAmount(card.getAmount() - paymentAmount);
            return true;
        } else {
            return false;
        }
    }

    private boolean cardIsPresent() {
        return card != null;
    }
}
```

- Now FoodComboDelivery isn't responsive for the payment details, and only is an entrypoint for the payment system

```java
if (strategy == null) {
                        System.out.println("Please, select a payment method: \n" +
                                "1 - PalPay" + "\n" +
                                "2 - Credit Card");
                        int paymentMethod = scanner.nextInt();


                        if (paymentMethod == 1 ) {
                            strategy = new PayByPaypal();
                        } else {
                            strategy = new PayByCreditCard();
                        }
                    }
                    System.out.println(bill.printBill(orderResults));

                    float totalBill = 0;
                    for (OrderResult orderResult : orderResults) {
                        totalBill += orderResult.orderPrice();
                    }

                    strategy.collectPaymentDetails();
                    if (strategy.pay(totalBill)) {
                        System.out.println("Payment has been successful.");
                        orderResults.clear();
                    } else {
                        System.out.println("FAIL! Please, check your data.");
                    }


```


## Conclusions / Screenshots / Results

This laboratory work provided practical insights into behavioral design patterns, specifically Memento and Strategy. By integrating these patterns, the system gained improved modularity and flexibility. Memento allowed state management and restoration, enhancing order handling, while Strategy streamlined payment processing by decoupling payment methods from the core functionality. This exercise demonstrated how behavioral patterns facilitate efficient interaction and dynamic adaptability between software components.