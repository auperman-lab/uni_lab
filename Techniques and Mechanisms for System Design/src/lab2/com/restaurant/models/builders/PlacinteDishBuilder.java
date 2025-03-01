package lab2.com.restaurant.models.builders;

import lab2.com.restaurant.models.PlacinteDish;
import lab2.com.restaurant.models.interfaces.DishBuilder;

public class PlacinteDishBuilder implements DishBuilder {
    private  int price;
    private  String name;
    private  String ingredient1;
    private  String ingredient2;
    private  String ingredient3;

    public PlacinteDishBuilder setPrice(int price) {
        this.price = price;
        return this;
    }
    public PlacinteDishBuilder setName(String name) {
        this.name = name;
        return this;
    }
    public PlacinteDishBuilder setIngredient1(String ingredient1) {
        this.ingredient1 = ingredient1;
        return this;
    }
    public PlacinteDishBuilder setIngredient2(String ingredient2) {
        this.ingredient2 = ingredient2;
        return this;
    }
    public PlacinteDishBuilder setIngredient3(String ingredient3) {
        this.ingredient3 = ingredient3;
        return this;
    }

    public PlacinteDish build() {
        return new PlacinteDish(price, name, ingredient1, ingredient2, ingredient3);
    }
}
