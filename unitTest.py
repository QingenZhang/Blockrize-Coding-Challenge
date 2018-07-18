import BankAPI

def main():
    
    success = 0
    failure = 0

    acc1 = "account1"
    acc2 = "account2"

    pwd1 = "password1"
    pwd2 = "password2"
    wrong_pwd = "wrong password"

    first_name = "Troy"
    last_name  = "Zhang"

    # set up bank api system
    bank_system = BankAPI.BankAPI()
    success += 1

    try:
        # create a dummy account (test simple POST)
        assert bank_system.post(acc1, pwd1, 0) == 0
        success += 1
    except AssertionError:
        failure += 1

    try:
        # get info about the account we just create (test simple GET)
        assert bank_system.get(acc1, pwd1) == 0
        success += 1
    except AssertionError:
        failure += 1

    try:
        # get info with incorrect password
        assert bank_system.get(acc1, wrong_pwd) == -1
        success += 1
    except AssertionError:
        failure += 1

    try:
        # post another account
        assert bank_system.post(acc2, pwd2, 100, first_name, last_name) == 0
        success += 1
    except AssertionError:
        failure += 1

    try:
        # get info
        assert bank_system.get(acc2, pwd2) == 100
        success += 1
    except AssertionError:
        failure += 1

    try:
        # get info (creation of new account does not affect existing ones)
        assert bank_system.get(acc1, pwd1) == 0
        success += 1
    except AssertionError:
        failure += 1

    try:
        # Test deposit and withdraw
        assert bank_system.deposit(acc1, pwd1, 100) == 100
        assert bank_system.get(acc1, pwd1) == 100
        assert bank_system.withdraw(acc1, pwd1, 50) == 50
        assert bank_system.get(acc1, pwd1) == 50
        assert bank_system.withdraw(acc1, pwd1, 100) == -1
        assert bank_system.withdraw(acc1, pwd2, 25) == -1
        success += 1
    except AssertionError:
        failure += 1

    try:
        # test multiple accounts creation for stability
        for i in range(50):
            acc_name = "acc" + str(i)
            pwd = str(i)
            deposit = i
            first_name = "Farst" + str(i)
            last_name = "Lost" + str(i)
            bank_system.post(acc_name, pwd, deposit, first_name, last_name)
        for j in range(50):
            acc_name = "acc" + str(j)
            pwd = str(j)
            deposit = j
            assert bank_system.get(acc_name, pwd) == deposit
        success += 1
    except AssertionError:
        failure += 1

    try:
        # test multiple accounts creation for stability
        for i in range(50):
            acc_name = "acc" + str(i)
            pwd = str(i)
            deposit = i
            bank_system.deposit(acc_name, pwd, deposit)
        for j in range(50):
            acc_name = "acc" + str(j)
            pwd = str(j)
            deposit = j
            assert bank_system.get(acc_name, pwd) == 2 * deposit
        success += 1
    except AssertionError:
        failure += 1

    print "==================================="
    print str(success + failure) + " tests run."
    print str(success) + " tests passed."
    print str(failure) + " tests failed"

if __name__ == '__main__':
    main()