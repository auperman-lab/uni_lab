package lab1.com.restaurant.models.interfaces;

public interface DishBuilder {
    DishBuilder setPrice(int price);
    DishBuilder setName(String name);
    DishBuilder setIngredient1(String ingredient1);
    DishBuilder setIngredient2(String ingredient2);
    DishBuilder setIngredient3(String ingredient3);
    Dish build(); // Returns a Dish type
}
