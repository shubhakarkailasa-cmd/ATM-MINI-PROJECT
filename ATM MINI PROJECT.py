import datetime
money=5000
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
        while True:
            try:
                choice=int(input("enter the option you want.."))

                if choice==1:
                    def deposit_money():
                        global money
                        user=int(input("enter the money you want to deposit"))
                        if user<0:
                            print('deposit cant be negative')
                            quit()
                        else:
                            money=money + user
                            print('YOUR TOTAL AMOUNT IS:-',money)
                    deposit_money()
                    write_logs(str(datetime.datetime.now()))
                    write_logs('DEPOSIT PROCESS COMPLETED')
    
                elif choice==2:
                    def withdrawl_money():
                        global money
                        print('please enter how much money you want to withdrawl')
                        user1=int(input('enter the money'))
                        if money<user1:
                            print('insufficient balance')
                            write_logs(str(datetime.datetime.now()))
                            write_logs('INSUFFICIENT BALANCE')
                        else:
                            money=money - user1
                            print('YOUR TOTAL BALANCE IS:-',money)
                            write_logs(str(datetime.datetime.now()))
                            write_logs('WITHDRAWL PROCESS COMPLETED')
                    withdrawl_money()
                elif choice==3:    
                    def check_balance():
                        global money
                        print('loading...')
                        print('YOUR BALANCE IS:-',money)
                        write_logs(str(datetime.datetime.now()))
                        write_logs('BALANCE HAS BEEN CHECKED BY THE USER')
                    check_balance()
                elif choice==4:
                    def exit_program():
                        print('thanks for choosing this bank')
                        write_logs(str(datetime.datetime.now()))
                        write_logs('LOGGED OUT')
                        quit()                  
                    exit_program()
                else:
                    print('invalid number')
            except ValueError:
                print('invalid value try again')
atm_system()


