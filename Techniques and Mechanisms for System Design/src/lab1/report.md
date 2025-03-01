# Creational Design Patterns

## Author: Danu Macrii

----

## Objectives:
* Study and understand the Creational Design Patterns.
* Choose a domain, define its main classes/models/entities and choose the appropriate instantiation mechanisms.
* Use some creational design patterns for object instantiation in a sample project.

## Used Design Patterns:
* Singleton - restricts the instantiation of a class to a singular instance
* Builder - separates the construction of a complex object from its representation
* Abstract Factory - create families of related objects without imposing their concrete classes
* Prototype - create prototypical instance, which is cloned to produce new objects


## Implementation

### Singleton
- Only one instance of FoodComboDelivery can exist at a time. The synchronized getInstance method is used to control access to the singleton instance, which is lazily initialized to improve performance.
```java
public static FoodComboDelivery getInstance() {
    FoodComboDelivery foodComboDelivery = instance;
    if (foodComboDelivery == null) {
        synchronized (FoodComboDelivery.class) {
            foodComboDelivery = instance;
            if (foodComboDelivery == null) {
                instance = new FoodComboDelivery();
            }
        }
    }
    return instance;
}
```

###  Builder
- CocktailBuilder defines an interface for building complex Cocktail objects in a step-by-step manner. It allows for the separation of the object’s construction from its representation, enabling easier and more readable object creation.

```java
public interface CocktailBuilder {
    CocktailBuilder setPrice(int price);
    CocktailBuilder setName(String name);
    CocktailBuilder setQuantity(float quantity);
    Cocktail build();
}

```


### Abstract Factory
- The abstract Order class provides a framework for creating families of related products (such as Dish and Cocktail). Each subclass of Order, like PlacinteOrder, defines methods for creating specific types of dishes and cocktails.
- This pattern allows for the creation of related objects without specifying the exact classes, promoting flexibility and scalability.
```java

public abstract class Order {
    ...

    public abstract Dish createDish();
    public abstract Cocktail createCocktail();
}

```

```java
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

```

### Prototype

- The Prototype interface defines a clone method for cloning objects. The PlacinteDish class implements this pattern by providing a clone method, which creates a duplicate of the dish object.
- This approach is effective for copying instances with complex states, avoiding the cost of building new objects from scratch.

```java

public interface Prototype {
    Prototype clone();
}
```

```java

 @Override
    public Dish clone() {
        return new PlacinteDish(this);
    }
```

## Conclusions / Screenshots / Results

The implementation of creational design patterns enhances the restaurant app's flexibility and efficiency. The Singleton pattern controls access to a single FoodComboDelivery instance, while the Builder pattern simplifies complex object creation, as seen in Cocktail. The Abstract Factory pattern enables consistent and modular instantiation of related objects in Order classes, improving extensibility. Lastly, the Prototype pattern supports efficient cloning, reducing instantiation costs. Together, these patterns streamline object creation, improve code readability, and support scalability, making the app more maintainable and adaptable to future requirements.
