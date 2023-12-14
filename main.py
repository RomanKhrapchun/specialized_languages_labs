from lab_runner import LabRunnerFacade

def main():
    runner = LabRunnerFacade()
    lab_options = {
        '1': runner.run_lab1,
        '2': runner.run_lab2,
        '3': runner.run_lab3,
        '4': runner.run_lab4,
        '5': runner.run_lab5,
        '7': runner.run_lab7,
        '8': runner.run_lab8
    }

    while True:
        print("\n==== ЛАБОРАТОРНІ РОБОТИ ====")
        for num in sorted(lab_options.keys()):
            print(f"{num}. Виконати лабораторну роботу {num}")
        print("0. Вихід")

        choice = input("Введіть номер лабораторної роботи або 0 для виходу: ")

        if choice in lab_options:
            lab_options[choice]()
        elif choice == '0':
            print("Дякую за використання програми. До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
