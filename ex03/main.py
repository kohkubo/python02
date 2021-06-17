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
        bv.Beverage(name="apple0", price=100, description="apple0 fruits", temperature=0),
        bv.Beverage(name="apple1", price=110, description="apple1 fruits", temperature=1),
        bv.Beverage(name="apple2", price=120, description="apple2 fruits", temperature=2),
        bv.Beverage(name="apple3", price=130, description="apple3 fruits", temperature=3),
    }

    vg_test = vg.Vendingmachine(name="mmm", stock=ds, greeting="hello world")
    print(vg_test.__str__())
    vg_test.sell(beverage_name="apple0")
    vg_test.sell(beverage_name="test")
    vg_test.display()
    vg_test.greet()
    vg_test.recommend()
    vg_test.ask()

if __name__ == "__main__":
    main()
