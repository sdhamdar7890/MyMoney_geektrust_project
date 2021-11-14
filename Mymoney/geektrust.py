import sys
import mymoney

"""The main function read input from the file whose path is given in the argument and process the commands from
each line.
It has 5 Commands i.e. Allocate, Sip, Change, Balance, Rebalance.
Allocate and Sip takes 3 integer parameter.
Change takes 3 integer and 1 sting parameter.
Balance takes 1 string parameter.
Rebalance doesn't take any parameters.
"""


def main():
    input_file = sys.argv[1]
    file_name = open(input_file, 'r', encoding='utf-8')
    account = mymoney.Account(1000, 2000, 3000)
    for line in file_name:
        command = list(line.split())
        if command[0].lower() == "allocate":
            account = mymoney.Account(int(command[1]), int(command[2]), int(command[3]))

        elif command[0].lower() == "sip":
            account.sip(int(command[1]), int(command[2]), int(command[3]))
        elif command[0].lower() == "change":
            account.change(float(command[1][:-1]), float(command[2][:-1]), float(command[3][:-1]), command[4].lower())

        elif command[0].lower() == "balance":
            account.balance(command[1].lower())

        elif command[0].lower() == "rebalance":
            account.balance(account.rebalance_month)

        else:
            print("Invalid Command")


if __name__ == "__main__":
    main()
