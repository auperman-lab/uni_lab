package lab1.com.restaurant.models;

import lab1.com.restaurant.models.interfaces.Cocktail;

public class PlacinteCocktail implements Cocktail {

    private final int price;
    private final String name;
    private final float quantity;


    public PlacinteCocktail(int price, String name, float quantity) {
        this.price = price;
        this.name = name;
        this.quantity = quantity;
    }
    public PlacinteCocktail(PlacinteCocktail placinteCocktail){
        this.price = placinteCocktail.price;
        this.name = placinteCocktail.name;
        this.quantity = placinteCocktail.quantity;
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
        return new PlacinteCocktail(this);
    }

}
