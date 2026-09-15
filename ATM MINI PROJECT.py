import datetime

def write_logs(message):
    with open(r"C:/atm/history/app.log",'a') as file:
        file.write(message+'\n')

def atm_system():

        print('==================welcome to mini atm bank====================')
        print("""
        ENTER THE OPTION YOU WANT
        1)DEPOSIT
        2)WITHDRAWL
        3)CHECK BALANCE
        4) EXIT""")
        write_logs('APP STARTED')
        write_logs(str(datetime.datetime.now()))
        while True:
            try:
                choice=int(input("enter the option you want.."))
                money=5000
                def deposit_money():
                    user=int(input("enter the money you want to deposit"))
                    if user<0:
                        print('deposit cant be negative')
                        quit()
                    else:
                        deposit=money + user
                        print('YOUR TOTAL AMOUNT IS:-',deposit)
                        write_logs(str(datetime.datetime.now()))
                        write_logs('DEPOSIT PROCESS COMPLETED')

                def withdrawl_money():
                    print('please enter how much money you want to withdrawl')
                    user1=int(input('enter the money'))
                    if money<user1:
                        print('insufficient balance')
                        write_logs(str(datetime.datetime.now()))
                        write_logs('INSUFFICIENT BALANCE')
                    else:
                        withdrawl= money- user1
                        print('YOUR TOTAL BALANCE IS:-',withdrawl)
                        write_logs(str(datetime.datetime.now()))
                        write_logs('WITHDRAWL PROCESS COMPLETED')
                 
                def check_balance():
                    print('loading...')
                    print('YOUR BALANCE IS:-',money)
                    write_logs(str(datetime.datetime.now()))
                    write_logs('BALANCE HAS BEEN CHECKED BY THE USER')

                def exit_program():
                    print('thanks for choosing this bank')
                    write_logs(str(datetime.datetime.now()))
                    write_logs('LOGGED OUT')
                    quit()                  
            except ValueError:
                print('invalid value try again')
            if choice==1:
                deposit_money()
            elif choice==2:
                withdrawl_money()
            elif choice==3:
                check_balance()
            elif choice==4:
                exit_program()
            else:
                print("invalid choice try again..")

atm_system()
