package lab1.com.restaurant.models;

import lab1.com.restaurant.models.interfaces.Cocktail;

public class AndyCocktail implements Cocktail {
    private final String name;
    private final double price;
    private final float quantity;

    public AndyCocktail(int price, String name, float quantity) {
        this.name   = name;
        this.price  = price;
        this.quantity   = quantity;
    }
    public AndyCocktail(AndyCocktail andyCocktail){
        this.name   = andyCocktail.name;
        this.price  = andyCocktail.price;
        this.quantity   = andyCocktail.quantity;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public double getPrice() {
        return price;
    }

    @Override
    public float getServingSize() {
        return quantity;
    }


    @Override
    public Cocktail clone() {
        return new AndyCocktail(this);
    }

}
