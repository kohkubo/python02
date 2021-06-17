import product as pd
import beverage as bv


def main():
    p = pd.Product(name="apple", price=100, description="apple fruits")
    print(p.print_attr())

    print("+++++++++++++++++++")

    b = bv.Beverage(
        name="apple", price=100, description="apple fruits", temperature=100
    )
    print(b.print_attr())


if __name__ == "__main__":
    main()
