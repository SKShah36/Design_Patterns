class WelcomeToBank:
    def __init__(self):
        print("Welcome to CBA Bank")
        print("We will serve you the best")


class AccountNumberCheck:
    def __init__(self):
        self._account_number = '12345678'

    def get_account_number(self) -> str:
        return self._account_number

    def account_active(self, acct_num: str) -> bool:
        return str(acct_num) == self.get_account_number()


class SecurityCodeCheck:
    def __init__(self):
        self._security_code = '1234'

    def get_security_code(self) -> str:
        return self._security_code

    def is_code_correct(self, sec_code: str) -> bool:
        return str(sec_code) == self.get_security_code()


class FundsCheck:
    def __init__(self):
        self._account_cash = 1000.00

    def get_account_cash(self) -> float:
        return self._account_cash

    def decrease_account_cash(self, withdraw_amount: float):
        self._account_cash -= withdraw_amount

    def increase_account_cash(self, cash_deposit: float):
        self._account_cash += cash_deposit

    def sufficient_balance(self, withdraw_amount: float) -> bool:
        if withdraw_amount > self.get_account_cash():
            print("You don't have enough balance")
            print("Current balance: {}".format(self.get_account_cash()))
            return False
        else:
            self.decrease_account_cash(withdraw_amount)
            print("Withdrawal complete!")
            print("Current balance: {}".format(self.get_account_cash()))
            self._account_cash -= withdraw_amount
            return True

    def make_deposit(self, cash_deposit: float):
        self.increase_account_cash(cash_deposit)
        print("Deposit Complete!")
        print("Current balance is: {}".format(self.get_account_cash()))


class BankAccountFacade:
    def __init__(self, new_acct_num: str, new_sec_code: str):
        self._bank_welcome = WelcomeToBank()
        self._acct_checker = AccountNumberCheck()
        self._code_checker = SecurityCodeCheck()
        self._fund_checker = FundsCheck()
        self._account_number = new_acct_num
        self._security_code = new_sec_code

    def get_account_number(self):
        return self._account_number

    def get_security_code(self):
        return self._security_code

    def withdraw_cash(self, cash_to_get: float):
        if self._acct_checker.account_active(self.get_account_number()) and self._code_checker.is_code_correct(
                self.get_security_code()) and self._fund_checker.sufficient_balance(cash_to_get):
            print("Transaction complete")
        else:
            print("Transaction failed")

    def deposit_cash(self, deposit_amt: float):
        if self._acct_checker.account_active(self.get_account_number()) and self._code_checker.is_code_correct(
                self.get_security_code()) and self._fund_checker.sufficient_balance(deposit_amt):
            print("Transaction complete")
        else:
            print("Transaction failed")


def driver():
    accessing_bank = BankAccountFacade('12345678', '1234')
    accessing_bank.withdraw_cash(50.00)
    accessing_bank.withdraw_cash(100.05)


if __name__ == "__main__":
    driver()
