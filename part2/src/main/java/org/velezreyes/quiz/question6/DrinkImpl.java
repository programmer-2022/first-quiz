package org.velezreyes.quiz.question6;

public class DrinkImpl implements Drink {
    private String name;
    private boolean isFizzy;
    private float price;

    public DrinkImpl(String name, boolean isFizzy, float price) {
        this.name = name;
        this.isFizzy = isFizzy;
        this.price = price;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFizzy() {
        return isFizzy;
    }

    @Override
    public float getPrice() {
        return price;
    }
}