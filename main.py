from service.speed_service import SpeedTestService


def display_menu():
    print("\n===== Internet Speed Tester =====")
    print("1. Run Optimized Speed Test")
    print("2. Run Naive Speed Test")
    print("3. Compare Performance")
    print("4. View Test History")
    print("5. Exit")


def main():
    service = SpeedTestService()

    while True:
        display_menu()
        choice = input("Select an option: ")

        if choice == "1":
            result = service.run_test(optimized=True)
            print(result)

        elif choice == "2":
            result = service.run_test(optimized=False)
            print(result)

        elif choice == "3":
            naive, optimized, improvement = service.compare_performance()

            print("\n--- Naive Test ---")
            print(naive)

            print("\n--- Optimized Test ---")
            print(optimized)

            print(f"\nPerformance Improvement: {improvement:.6f} seconds")

        elif choice == "4":
            history = service.get_test_history()

            if not history:
                print("No records found.")
            else:
                for row in history:
                    print(row)

        elif choice == "5":
            print("Exiting application...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()

