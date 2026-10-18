class ATM:
    def __init__(self):
        self.balance=0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Deposite amount must be positive.')
        self.balance += amount

    def Withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Deposite Amount must be positive')

        if amount > self.balance:
            raise ValueError('Insufficiant Fund')

        self.balance -= amount

class ATMController:
    def __init__(self):
        self.atm = ATM()
# Number Input Vanguradhu
    def get_number(self, promt):
        while True:
            try:
                number = float(input(promt))
                return number
            except ValueError:
                print("Please  enter valid number")
#  ATN Menu
    def display_menu(self):
        print('\nWelcome To The ATM!')
        print('1.Check Balance')
        print('2.Deposite')
        print('3.Withdrawl')
        print('4.Exit')
# Controller Methods
    def check_balance(self):
        balance = self.atm.check_balance()
        print(f'Your Current Balance Is: {balance}')

    def deposit(self):
        while True:
            try:
                amount = self.get_number(
                    'Enter The Amount To Deposite: '
                )
                self.atm.deposit(amount)
                print(f'Succesfully Deposited:{amount}.')
                break
            except ValueError as error:
                print(error)

    def withdraw(self):
        while True:
            try:
                amount=self.get_number('Enter the amount to deposit: ')
                self.atm.Withdraw(amount)
                print(f'Succesfully deposited {amount}.')
                break
            except ValueError as errer:
                print(error)

    def run(self):
            while True:
                self.display_menu()

                choice = input('Please Choose An Option: ')
                if choice == '1':
                    self.check_balance()

                elif choice == '2':
                    self.deposit()
                elif choice == '3':
                    self.withdraw()
                elif choice == '4':
                    print('Thank You Using ATM.')
                    break
                else:
                    print('Invalid Choice.Plaese Try Again.')
def main():
        atm = ATMController()
        atm.run()
if __name__== '__main__':
        main()
    