package lab1.com.restaurant.order;

import lab1.com.restaurant.models.builders.PlacinteCocktailBuilder;
import lab1.com.restaurant.models.builders.PlacinteDishBuilder;
import lab1.com.restaurant.models.interfaces.Cocktail;
import lab1.com.restaurant.models.interfaces.Dish;

//TODO
public class PlacinteOrder extends Order {
    @Override
    public Dish createDish() {
        return new PlacinteDishBuilder()
                .setPrice(80)
                .setName("Placinta cu cascaval")
                .setIngredient1("placinta")
                .setIngredient2("cascaval")
                .build();
    }

    @Override
    public Cocktail createCocktail() {
        return new PlacinteCocktailBuilder()
                .setPrice(12)
                .setName("Wine")
                .setQuantity(0.5f)
                .build();
    }
}
