package lab2.com.restaurant.models.builders;

import lab2.com.restaurant.models.AndyCocktail;
import lab2.com.restaurant.models.interfaces.CocktailBuilder;

public class AndyCocktailBuilder implements CocktailBuilder {
    private  int price;
    private  String name;
    private  float quantity;

    public AndyCocktailBuilder setPrice(int price) {
        this.price = price;
        return this;
    }
    public AndyCocktailBuilder setName(String name) {
        this.name = name;
        return this;
    }
    public AndyCocktailBuilder setQuantity(float quantity) {
        this.quantity = quantity;
        return this;
    }

    public AndyCocktail build() {
        return new AndyCocktail(price, name, quantity);
    }
}
