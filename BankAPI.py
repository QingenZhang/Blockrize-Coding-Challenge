class BankAPI(object):
    accounts = dict()

    def post(self, account_name, password, init_deposit, first_name="N/A", last_name="N/A"):
        """
        POST
        """
        # Case 1: exist same account name
        if account_name in self.accounts:
            print "Account name already exists, try a different one."
            return -1

        # Case 2: illegal amount of deposit
        elif init_deposit < 0:
            print "Illegal initial deposit amount: " + str(init_deposit)
            return -1

        # Case 3: legal name and deposit amount
        else:
            self.accounts[account_name] = BankAccount(account_name, password, init_deposit, first_name, last_name)
            print "Account " + account_name + " successfully created."
            print "Current balance: " + str(init_deposit)
            return 0

    def get(self, account_name, password):
        """
        GET
        """
        # Case 1 & 2: Account does not exist or Incorrect password
        if not self._validate_account(account_name, password):
            print "Incorrect account name or password. Please try again."
            return -1

        # Get credential
        credential = self.accounts[account_name].get_credentials()

        # Case 3: Correct password
        if credential == password:
            acc = self.accounts[account_name]
            cur_bal = acc.get_balance()
            print "Account name: " + account_name
            print "Current balance: " + str(cur_bal)
            print "First Name: " + acc.first_name
            print "Last Name: " + acc.last_name
            return cur_bal

    def deposit(self, account_name, password, amount):
        """
        Deposit method
        """
        # Case 1: illegal amount to deposit (less than or equal to 0)
        if amount <= 0:
            print "The amount you are depositing must be larger than 0!"
            return -1

        # Case 2: incorrect credentials
        if not self._validate_account(account_name, password):
            print "Incorrect account name or password. Please try again."
            return -1

        # Case 3: Everything good
        balance = self.accounts[account_name].get_balance()
        self.accounts[account_name].deposit(amount)
        balance_new = self.accounts[account_name].get_balance()

        print "Deposit successfully!"
        print "The original balance was " + str(balance)
        print "Current balance is " + str(balance_new)

        return balance_new

    def withdraw(self, account_name, password, amount):
        """
        Withdraw method
        """
        # Case 1: illegal amount to deposit (less than or equal to 0)
        if amount <= 0:
            print "The amount you are withdrawing must be larger than 0!"
            return -1

        # Case 2: incorrect credentials
        if not self._validate_account(account_name, password):
            print "Incorrect account name or password. Please try again."
            return -1

        # Case 3: Everything good
        # Case 4: one additional situation considered in withdraw (withdrawal larger than current balance will be rejected)
        balance = self.accounts[account_name].get_balance()
        if not self.accounts[account_name].withdraw(amount):
            print "You cannot withdraw more money than your current balance!"
            return -1

        balance_new = self.accounts[account_name].get_balance()

        print "Withdraw successfully!"
        print "The original balance was " + str(balance)
        print "Current balance is " + str(balance_new)

        return balance_new

        
    def _validate_account(self, account_name, password):
        """
        instance method to verify credentials before any activity
        """
        if account_name not in self.accounts or self.accounts[account_name].get_credentials() != password:
            return False
        return True


class BankAccount(object):

    def __init__(self, account_name, password, init_deposit, first_name, last_name):
        self.account_name = account_name
        self.password = password
        self.balance = init_deposit
        self.first_name = first_name
        self.last_name = last_name

    def get_balance(self):
        return self.balance

    def get_credentials(self):
        return self.password

    def deposit(self, amount):
        self.balance += amount
        return True

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True