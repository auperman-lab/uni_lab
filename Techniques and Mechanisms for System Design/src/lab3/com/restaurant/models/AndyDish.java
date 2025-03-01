package lab3.com.restaurant.models;

import lab3.com.restaurant.models.interfaces.Dish;

public class AndyDish implements Dish {

    private final int price;
    private final String name;
    private final String ingredient1;
    private final String ingredient2;
    private final String ingredient3;

    public AndyDish(int price, String name, String ingredient1, String ingredient2, String ingredient3) {
        this.price = price;
        this.name = name;
        this.ingredient1 = ingredient1;
        this.ingredient2 = ingredient2;
        this.ingredient3 = ingredient3;
    }
    public AndyDish(AndyDish andyDish) {
        this.price = andyDish.price;
        this.name = andyDish.name;
        this.ingredient1 = andyDish.ingredient1;
        this.ingredient2 = andyDish.ingredient2;
        this.ingredient3 = andyDish.ingredient3;
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
    public void prepare() {
        System.out.println("Preparing andy dish");
        System.out.println("...");
        System.out.println("Adding" + ingredient1);
        System.out.println("Adding" + ingredient2);
        System.out.println("Adding" + ingredient3);
        System.out.println("Cooking");
        System.out.println("...");
        System.out.println("Done");

    }

    @Override
    public Dish clone() {
        return new AndyDish(this);
    }
}
