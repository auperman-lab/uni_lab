package lab2.com.restaurant.order;

import lab2.com.restaurant.models.interfaces.Cocktail;
import lab2.com.restaurant.models.interfaces.Dish;

public class OrderResult {
    private final Dish dish;
    private final Cocktail cocktail;

    public OrderResult(Dish dish, Cocktail cocktail) {
        this.dish = dish;
        this.cocktail = cocktail;
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
}
