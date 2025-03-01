package lab3.com.restaurant.service.order;

import lab3.com.restaurant.models.interfaces.Cocktail;
import lab3.com.restaurant.models.interfaces.Dish;
import lab3.com.restaurant.models.interfaces.Prototype;

import java.io.Serializable;

public class OrderResult implements Prototype {
    private final Dish dish;
    private final Cocktail cocktail;

    public OrderResult(Dish dish, Cocktail cocktail) {
        this.dish = dish;
        this.cocktail = cocktail;
    }

    public OrderResult(OrderResult orderResult) {
        this.dish = orderResult.dish;
        this.cocktail = orderResult.cocktail;
    }

    public Dish getDish() {
        return dish;
    }

    public Cocktail getCocktail() {
        return cocktail;
    }

    public String orderInfo() {
        return "Order Details:\n" +
                "Dish: " + dish.getName() + " | Price: " + dish.getPrice() + "\n" +
                "Cocktail: " + cocktail.getName() + " | Price: " + cocktail.getPrice();
    }

    public double orderPrice() {
        return dish.getPrice() + cocktail.getPrice();
    }


    @Override
    public OrderResult clone() {
        return new OrderResult(this);
    }
}
