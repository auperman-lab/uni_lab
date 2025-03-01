package lab3.com.restaurant.models.interfaces;

public interface CocktailBuilder {
    CocktailBuilder setPrice(int price);
    CocktailBuilder setName(String name);
    CocktailBuilder setQuantity(float quantity);
    Cocktail build();
}