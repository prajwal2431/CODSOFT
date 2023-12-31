class Calculator:
    def add(self,x,y):
        return x + y
    def sub(self,x,y):
        return x - y
    def mul(self,x,y):
        return x * y
    def div(self,x, y):
        try:
            return x / y
        except ZeroDivisionError as e:
            return e
    def expo(self,x,y):
        if x == y == 0:
            raise ValueError("Can't perform this operation")
        return x ** y

def main():
    Calculator_obj = Calculator()

    while True:
        print("\nOptions:")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponential")
        print("6. Quit")
        try:
            choice = int(input("Emter your choice : "))
            if choice in (1, 2, 3, 4, 5):
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == 1:
                    print(f"Result: {Calculator_obj.add(num1, num2)}")
                elif choice == 2:
                    print(f"Result: {Calculator_obj.sub(num1, num2)}")
                elif choice == 3:
                    print(f"Result: {Calculator_obj.mul(num1, num2)}")
                elif choice == 4:
                    print(f"Result: {Calculator_obj.div(num1, num2)}")
                elif choice == 5:
                    print(f"Result: {Calculator_obj.expo(num1, num2)}")

            elif choice == 6:
                print("Exiting the calculator. Goodbye!")
                break
            else:
                raise ValueError("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()