import beverage as bv
import product as pd
import vendingmachine as vm


def main():

    p = pd.Product(name="coffee", price=100, description="beverage")
    print(p.print_attr())
    print("++++++++++++++++++++++++++++")
    b = bv.Beverage(name="coffee", price=100, description="beverage", temperature=5)
    print(b.print_attr())
    print("++++++++++++++++++++++++++++")
    v = vm.Vendingmachine(name="coffee", stock=10)
    v.ask()

if __name__ == '__main__':
    main()
