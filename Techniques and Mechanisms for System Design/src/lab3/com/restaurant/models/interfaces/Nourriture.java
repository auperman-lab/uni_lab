package lab3.com.restaurant.models.interfaces;

public interface Nourriture extends Prototype {
    String getNom();
    double getPrix();
    void preparer();
    Nourriture clone();

}
