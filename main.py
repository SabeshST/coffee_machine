from data import MENU, resources, coins

coffee_machine_on = True
resources_available = True

while coffee_machine_on:

    user_order = input("What would you like? (espresso/latte/cappuccino): ")


    def resources_checker(user_order):
        """Checks if there's enough ingredients in the resources dictionary and returns True or False. It also prints the missing ingredient."""
        ingredients = MENU[user_order]['ingredients']
        for i in ingredients:
            if resources[i] - ingredients[i] < 0:
                print(f"Sorry there is not enough {i}.")
                return False

        return True

    def resources_updater(user_order):
        """Should be called after resources_checker(), this deducts the ingredients from the resources dicitonary"""
        ingredients = MENU[user_order]['ingredients']
        for i in ingredients:
            resources[i] -= ingredients[i]

    if user_order == "report":
        print(resources)
    elif user_order == "off":
        coffee_machine_on = False
        print("See ya")
        break
    else:
        resources_available = resources_checker(user_order)

        if resources_available:

            user_payment = input(f"Your {user_order} costs: ${MENU[user_order]['cost']}. Insert coins, q=0.25, d=0.1, n=0.05, p=0.01: ")

            insert_coins = True
            coins_inserted = user_payment.split(" ")
            total_inserted = 0

            #calculates the total inserted using the values in the coins dictionary
            for i in range(0, len(coins_inserted) - 1, 2):
                total_inserted += int(coins_inserted[i]) * coins[coins_inserted[i + 1]]

            """
            This conditional structure is to process the coins, return change and complete the order, 
            this is where the resources are also updated
            """
            if total_inserted < MENU[user_order]['cost']:
                print("Sorry that's not enough money. Money refunded.")

            elif total_inserted > MENU[user_order]['cost']:
                resources_updater(user_order)
                print(f"here is your change {round(total_inserted- MENU[user_order]['cost'], 2)}. Enjoy your {user_order}.")
                total_inserted -= total_inserted - MENU[user_order]['cost']
                resources["money"] += total_inserted


            elif resources_available:
                resources_updater(user_order)
                print(f"Enjoy your {user_order}.")
                resources["money"] += total_inserted




