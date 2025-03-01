# Creational Design Patterns

## Author: Danu Macrii

----

## Objectives:
* Study and understand the Structural Design Patterns.
* As a continuation of the previous laboratory work, think about the functionalities that your system will need to provide to the user.
* Implement some additional functionalities using structural design patterns.
  
## Used Design Patterns:
* Adapter - allows the interface of an existing class to be used as another interface
* Decorator - allows behavior to be added to an individual object, dynamically, without affecting the behavior of other instances of the same class
* Proxy - a class functioning as an interface to something else


## Implementation

### Adapter
- Here this adapter allows classes of type Nourriture to be used as of type Dish

```java
public class FrenchDishAdapter implements Dish{
    private Nourriture nourriture;

    public FrenchDishAdapter(Nourriture nourriture) {
        this.nourriture = nourriture;
    }

    @Override
    public String getName() {
        return nourriture.getNom();
    }

    @Override
    public double getPrice() {
        return nourriture.getPrix();
    }

    @Override
    public void prepare() {
        nourriture.preparer();

    }

    @Override
    public Dish clone() {
        return  null;
    }
}
```
### Decorator

- BaseBillDecorator is used to divide functionality of printing bill in json and xml format without interfering withe the base printing of bill.

```java
  IBill realBill = new JsonBill(
        new XmlBill(
                new Bill()
        )
);

```

```java
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

```


### Proxy
- In this case proxy pattern is used to interfere in bill creating and caching the bills, because they are expensive to create(:^)

```java

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

```


## Conclusions / Screenshots / Results

