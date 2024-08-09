In this repository, several problems have been solved using Python, utilizing OOPs, classes, math operations, conditions, functions, loops, lists and dictionaries methods.
The questions are listed below.

Bank Accounts: 
“Bank Account Class”
There is a class named Account that is used as an abstract class for three other classes. This class has two attributes, balance and number, which represent the account balance and account number, respectively. Additionally, this class has another attribute called transactions, which is a list that shows the transactions made. This class defines three methods for depositing into the account, withdrawing from the account, and displaying the balance. After each withdrawal or deposit, the transaction amount is stored in the transactions list (a positive amount for deposits and a negative amount for withdrawals). The __str__ method of this class is defined in such a way that it displays as number:balance, and the balance is rounded to two decimal places.

“Current Account Class”
A class named CheckingAccount is created that inherits from the Account class. A class attribute called min_amount is defined for this class, which represents the minimum balance required to open an account (for example, 100,000), and based on this amount, new account creation is allowed. Additionally, the __str__ method is written in such a way that its output is as follows:
“Checking Account, Number: number, Balance: balance”

“Saving Account Class”
A class named SavingAccount is created that inherits from the Account class. A method is implemented for this class to calculate the income-to-expense ratio for the account holder (the ratio of the total deposits to the total withdrawals). The __str__ method is written in such a way that its output is as follows:
“Saving Account, Number: number, Balance: balance”

“Currency Account Class”
A class named CurrencyAccount is created that inherits from the Account class. A static method is designed for this class to convert the amount from rials to dollars so that the account holder can view their balance in terms of the current dollar price. A method is also designed for this class that allows the account holder to view their transaction list based on dollars. The __str__ method is written in such a way that its output is as follows:
“Business Account, Number: number, Balance: balance”

“Customer class”
A class named Customer has been created with three attributes: name, ssn, and acc_type, where acc_type has valid values of B, S, C. The name and ssn attributes represent the customer’s name and national ID number, respectively. Three methods for account creation have been implemented, each corresponding to the types of accounts defined above. The inputs for these methods are the balance and account number.For the Customer class, the following methods are defined:
•	show_balance: This method displays the customer's account balance in a suitable format.
•	make_deposit: This method takes an amount as input and performs a deposit operation into the customer's account.
•	make_withdraw: This method takes an amount as input and performs a withdrawal operation from the customer's account.
•	make_transfer: This method takes three inputs: the source account, the destination account, and the transfer amount. It performs the transfer operation using withdrawal and deposit and finally displays the balance amounts of both the source and destination accounts.

GPA :  A program that takes 5 grades from the user and displays the GPA based on the given format. If any of the input grades are greater than 20, it should display the message "Invalid Grade" and not execute the rest of the program.

Happy number: A program that checks whether the given integer is a happy number or not. A happy number is a number that, if you repeatedly sum the squares of its digits, evevtually leads to 1.

Noemalizer: A program that scales a set of numbers to the range of 0 to 1. 

Polindrome: A program that checks whether the given input string is a palindrome or not. A palindrome is a string that reads the same forwards and backwards.

Reduction to zero: A program that counts the steps required to reduce an integer to zero. In each step, if the current number is even, divide it by 2, and if it is odd, subtract one from it.

Search in position: A program that takes a sorted list in ascending order and an integer (target) and searches for the given number in the list, returning its index. If the number is not present in the list, it returns the expected index.

Word count: A program that takes a long text and a word from the user and displays the number of times the word is repeated in the text.
