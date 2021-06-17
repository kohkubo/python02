import beverage as bv
import product as pd
import vendingmachine as vm


def main():
    coffee = bv.Beverage('coffee', 100, 'It is a must for brainwork!!', 80)
    coca = bv.Beverage('coca-cola', 100, 'the most popular drink!', 3)
    vm = vm.Vendingmachine("Henry", "Hi, I am Henry", [[coca, 1],[coffee, 5]])


if __name__ == '__main__':
    main()
