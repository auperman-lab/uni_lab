package lab1.com.restaurant.models.builders;

import lab1.com.restaurant.models.PlacinteCocktail;
import lab1.com.restaurant.models.interfaces.CocktailBuilder;

public class PlacinteCocktailBuilder implements CocktailBuilder {

    private  int price;
    private  String name;
    private float quantity;


    public PlacinteCocktailBuilder setPrice(int price) {
        this.price = price;
        return this;
    }
    public PlacinteCocktailBuilder setName(String name) {
        this.name = name;
        return this;
    }
    public PlacinteCocktailBuilder setQuantity(float quantity) {
        this.quantity = quantity;
        return this;
    }


    public PlacinteCocktail build() {
        return new PlacinteCocktail(price, name, quantity);
    }
}
