package lab2.com.restaurant;

import lab2.com.restaurant.models.interfaces.Dish;
import lab2.com.restaurant.models.interfaces.Nourriture;

public class FrenchDishAdapter implements Dish{
    private Nourriture nourriture;

    public FrenchDishAdapter(Nourriture nourriture) {
        this.nourriture = nourriture;
    }

    @Override
    public String getName() {
        return nourriture.getNom();
    }

    @Override
    public double getPrice() {
        return nourriture.getPrix();
    }

    @Override
    public void prepare() {
        nourriture.preparer();

    }

    @Override
    public Dish clone() {
        return  null;
    }
}
