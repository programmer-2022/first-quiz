package org.velezreyes.quiz.question6;

public interface VendingMachine {

  void insertQuarter();

  Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException;

  void addDrink(String name, Drink drink);

  float getCurrentMoney();

  void resetMoney();

}