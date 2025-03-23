"""
Keyboard träningsprogram
"""
import tests

def main():
    """
    main
    """
    
    while True:
        tests.clear_screen()
        print("1) Easy")
        print("2) Medium")
        print("3) Hard")
        print("4) Score")
        print("q) Quit")
        
        choice = input("--> ")

        if choice == "q":
            print("Bye, bye!")
            break

        elif choice == "1":
            tests.easy()

        elif choice == "2":
            tests.medium()

        elif choice == "3":
            tests.hard()

        elif choice == "4":
            tests.read_file_s()

        else:
            print("That is not a valid choice. You can only choose from the menu.")

        input("\nPress enter to go back to the menu.")


if __name__ == "__main__":
    main()
