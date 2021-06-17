import product as pd
import beverage as bv
import vendingmachine as vg


def main():
    p = pd.Product(name="apple", price=100, description="apple fruits")
    print(p.print_attr())

    print("+++++++++++++++++++")

    b = bv.Beverage(
        name="apple", price=100, description="apple fruits", temperature=100
    )
    print(b.print_attr())

    print("+++++++++++++++++++")

    ds = {
        bv.Beverage(name="coffee", price=100, description="this is coffee", temperature=0),
        bv.Beverage(name="cola", price=110, description="this is cola", temperature=1),
        bv.Beverage(name="Monster", price=120, description="this is Monster", temperature=2),
    }

    vg_test = vg.Vendingmachine(name="mmm", stock=ds)
    print(vg_test.__str__())
    vg_test.sell(beverage_name="cola")
    vg_test.sell(beverage_name="test")
    vg_test.ask()

if __name__ == "__main__":
    main()
