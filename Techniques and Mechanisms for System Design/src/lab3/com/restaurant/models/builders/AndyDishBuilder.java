package lab3.com.restaurant.models.builders;

import lab3.com.restaurant.models.AndyDish;
import lab3.com.restaurant.models.interfaces.DishBuilder;

public class AndyDishBuilder implements DishBuilder {
    private  int price;
    private  String name;
    private  String ingredient1;
    private  String ingredient2;
    private  String ingredient3;

    public AndyDishBuilder setPrice(int price) {
        this.price = price;
        return this;
    }
    public AndyDishBuilder setName(String name) {
        this.name = name;
        return this;
    }
    public AndyDishBuilder setIngredient1(String ingredient1) {
        this.ingredient1 = ingredient1;
        return this;
    }
    public AndyDishBuilder setIngredient2(String ingredient2) {
        this.ingredient2 = ingredient2;
        return this;
    }
    public AndyDishBuilder setIngredient3(String ingredient3) {
        this.ingredient3 = ingredient3;
        return this;
    }

    public AndyDish build() {
        return new AndyDish(price, name, ingredient1, ingredient2, ingredient3);
    }
}
