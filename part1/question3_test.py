from question3 import alchemy_combine, make_oven


def test_alchemy_combine():

    #Mocks
    list_ingredients_1 = ["lead", "mercury"]
    temperature1 = 5000
    value_expect_1 = "gold"

    list_ingredients_2 = ["water", "air"]
    temperature2 = -100
    value_expect_2 = "snow"

    list_ingredients_3 = ["cheese", "dough", "tomato"]
    temperature3 = 150
    value_expect_3 = "pizza"


    assert alchemy_combine(make_oven(), list_ingredients_1,
                           temperature1) == value_expect_1

    assert alchemy_combine(make_oven(), list_ingredients_2,
                           temperature2) == value_expect_2

    assert alchemy_combine(make_oven(), list_ingredients_3,
                           temperature3) == value_expect_3
