import product as pd
import salesperson as sp


def main():
    p = pd.Product()
    print(p)

    s = sp.Salesperson(name="salesman")
    print(s)

    print(s.promote())


if __name__ == "__main__":
    main()
