package lab2.com.restaurant.models;

import lab2.com.restaurant.models.interfaces.Nourriture;

public class CremeDeLaCremeNourriture implements Nourriture {

    private final int prix;
    private final String nom;
    private final String ingredient1;
    private final String ingredient2;
    private final String ingredient3;

    public CremeDeLaCremeNourriture(int prix, String nom, String ingredient1, String ingredient2, String ingredient3) {
        this.prix = prix;
        this.nom = nom;
        this.ingredient1 = ingredient1;
        this.ingredient2 = ingredient2;
        this.ingredient3 = ingredient3;
    }

    public CremeDeLaCremeNourriture(CremeDeLaCremeNourriture autreNourriture) {
        this.prix = autreNourriture.prix;
        this.nom = autreNourriture.nom;
        this.ingredient1 = autreNourriture.ingredient1;
        this.ingredient2 = autreNourriture.ingredient2;
        this.ingredient3 = autreNourriture.ingredient3;
    }

    @Override
    public String getNom() {
        return nom;
    }

    @Override
    public double getPrix() {
        return prix;
    }

    @Override
    public void preparer() {
        System.out.println("Préparation de la crème de la crème nourriture");
        System.out.println("...");
        System.out.println("Ajout de " + ingredient1);
        System.out.println("Ajout de " + ingredient2);
        System.out.println("Ajout de " + ingredient3);
        System.out.println("Cuisson en cours");
        System.out.println("...");
        System.out.println("Prêt");
    }

    @Override
    public Nourriture clone() {
        return new CremeDeLaCremeNourriture(this);
    }
}
