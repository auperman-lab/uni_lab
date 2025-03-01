package lab2.com.restaurant.order;

import lab2.com.restaurant.models.interfaces.Cocktail;
import lab2.com.restaurant.models.interfaces.Dish;

public abstract class Order {

    public Order() {
    }

    public OrderResult order() {
        Dish dish = createDish();
        Cocktail cocktail = createCocktail();
        dish.prepare();
        return new OrderResult(dish, cocktail);
    }


    public abstract Dish createDish();
    public abstract Cocktail createCocktail();
}

