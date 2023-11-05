package org.velezreyes.quiz.question6;

import java.util.HashMap;
import java.util.Map;

public class VendingMachineImpl implements VendingMachine {

  private float currentMoney;
  private static Map<String, Drink> listOfAvailableDrinks;

  public VendingMachineImpl() {
    this.currentMoney = 0;
    this.loadDrinks();
  }

  public static void loadDrinks() {
    listOfAvailableDrinks = new HashMap<String, Drink>() {{
      put("CocaCola", new DrinkImpl("CocaCola", true, 0.50f));
      put("KarenTea", new DrinkImpl("KarenTea", false, 1.0f));
      put("Sprite", new DrinkImpl("Sprite", true, 0.55f));
      put("Fanta", new DrinkImpl("Fanta", true, 0.60f));
      put("Water", new DrinkImpl("Water", false, 0.30f));
      put("Orange Juice", new DrinkImpl("Orange Juice", false, 0.70f));
      put("Apple Juice", new DrinkImpl("Apple Juice", false, 0.65f));
      put("Iced Tea", new DrinkImpl("Iced Tea", true, 0.40f));
      put("Lemonade", new DrinkImpl("Lemonade", true, 0.55f));
      put("ScottCola", new DrinkImpl("ScottCola", true, 0.75f));
    }};
  }

  public static VendingMachine getInstance() {
    return new VendingMachineImpl();
  }

  @Override
  public void insertQuarter() {
    this.currentMoney += 0.25f;
  }

  @Override
  public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
    Drink drink = listOfAvailableDrinks.get(name);

    if (drink == null) {
      throw new UnknownDrinkException();
    }

    if (currentMoney < drink.getPrice()) {
      throw new NotEnoughMoneyException();
    }

    currentMoney -= drink.getPrice();
    return drink;
  }

  @Override
  public void addDrink(String name, Drink drink) {
    listOfAvailableDrinks.put(name, drink);
  }

  @Override
  public float getCurrentMoney() {
    return currentMoney;
  }

  @Override
  public void resetMoney() {
    currentMoney = 0;
  }
}
