package lab2.com.restaurant.order;

import lab2.com.restaurant.FrenchDishAdapter;
import lab2.com.restaurant.models.CremeDeLaCremeNourriture;
import lab2.com.restaurant.models.builders.AndyCocktailBuilder;
import lab2.com.restaurant.models.interfaces.Cocktail;
import lab2.com.restaurant.models.interfaces.Dish;
import lab2.com.restaurant.models.interfaces.Nourriture;

public class CremeOrder extends Order{
    @Override
    public Dish createDish() {
        Nourriture sandwich =  new CremeDeLaCremeNourriture(119, "Croque Monsieur", "pain", "pomme", "lard");
        return new FrenchDishAdapter(sandwich);
    }

    @Override
    public Cocktail createCocktail() {
        return  new AndyCocktailBuilder()
                .setPrice(115)
                .setName("Limonada")
                .setQuantity(0.25f)
                .build()
                ;
    }
}
