package lab3.com.restaurant.service.order;

import lab3.com.restaurant.utils.FrenchDishAdapter;
import lab3.com.restaurant.models.CremeDeLaCremeNourriture;
import lab3.com.restaurant.models.builders.AndyCocktailBuilder;
import lab3.com.restaurant.models.interfaces.Cocktail;
import lab3.com.restaurant.models.interfaces.Dish;
import lab3.com.restaurant.models.interfaces.Nourriture;

public class CremeOrder extends Order {
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
