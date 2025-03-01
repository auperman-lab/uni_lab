package lab3.com.restaurant.service.order;


import lab3.com.restaurant.models.builders.PlacinteCocktailBuilder;
import lab3.com.restaurant.models.builders.PlacinteDishBuilder;
import lab3.com.restaurant.models.interfaces.Cocktail;
import lab3.com.restaurant.models.interfaces.Dish;

//TODO
public class PlacinteOrder extends Order {
    @Override
    public Dish createDish(){
        return new PlacinteDishBuilder()
                .setIngredient1("qwe")
                .setIngredient2("qwe")
                .setIngredient3("qwe")
                .setName("lab2")
                .setPrice(69)
                .build()
                ;
    }
    @Override
    public Cocktail createCocktail(){
        return new PlacinteCocktailBuilder()
                .setName("lab2")
                .setPrice(69)
                .build();

    }

}
