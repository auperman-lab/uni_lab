package lab1.com.restaurant.order;

import lab1.com.restaurant.models.builders.AndyCocktailBuilder;
import lab1.com.restaurant.models.builders.AndyDishBuilder;
import lab1.com.restaurant.models.interfaces.Cocktail;
import lab1.com.restaurant.models.interfaces.Dish;

public class AndyOrder extends Order {
    @Override
    public Dish createDish() {
        return new AndyDishBuilder()
                .setPrice(115)
                .setName("Capricioasa")
                .setIngredient1("Sunca")
                .setIngredient2("Cascaval")
                .setIngredient3("Ciuperci")
                .build();
    }

    @Override
    public Cocktail createCocktail() {
        return new AndyCocktailBuilder()
                .setPrice(115)
                .setName("Limonada")
                .setQuantity(0.25f)
                .build()
                ;
    }
}
