def main():
    # Stating amount
    amount = 50

    while amount > 0:
        print(f"Amount Due: {amount}")
        # Inserting coin
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            amount -= coin

    change = abs(amount)
    print(f"Change Owed: {change}")

main()