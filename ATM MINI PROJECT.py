import datetime
import random
import time
def write_logs(message):
    with open(r"C:/updated/atm/app.log",'a') as file:
        file.write(message+'\n')
def atm_system():
        money=5000

        Pin_number=random.randint(1000,9999)
        print(Pin_number)
        for i in range(3,0,-1):
            try:
                verify=int(input("enter the pin number.."))
            except ValueError:
                print("please type pin number correctly")
            if verify==Pin_number:
                print("correct")
                write_logs("USERS LOGINED...")
                write_logs(str(datetime.datetime.now()))
                time.sleep(2)
                print('================== WELCOME TO MINI ATM BANK====================')
                print("""
                    ENTER THE OPTION YOU WANT
                    1)DEPOSIT
                    2)WITHDRAWL
                    3)CHECK BALANCE
                    4) EXIT""")
                try:
                    while True:
                        try:
                            choice=int(input("enter the choice"))
                            if choice==1:
                                write_logs('user selected deposit processs')
                                write_logs(str(datetime.datetime.now()))
                                try:
                                    user=int(input("enter the amount you want to deposit"))
                                    print('please enter the deposit number')
                                    if user<=0:
                                        print("negative numbers cant be deposited..")
                                        break
                                    money=user+money
                                    print("deposit process completed")
                                    time.sleep(2)
                                    print("UR CURRENT BALANCE IS",money)
                                    write_logs('deposit process completed')
                                    write_logs(str(datetime.datetime.now()))
                                except ValueError:
                                     print("invalid amount has been typed")
                            elif choice==2:
                                    write_logs('user selected withdrawl process')
                                    write_logs(str(datetime.datetime.now()))
                                    print("opening users bank deatils")
                                    time.sleep(2)
                                    try:
                                        user1=int(input("enter the money you want to withdrawl"))
                                        print("please enter the withdrawl amount")
                                        if user1>money or user1<0:
                                            print("NO SUCH ACTIONS ARE POSSIBLE")
                                            break
                                        money=money - user1
                                        print("withdrawl process completed")
                                        time.sleep(2)
                                        print("ur current balance is ",money)
                                        write_logs("withdrawl process completed")
                                        write_logs(str(datetime.datetime.now()))
                                    except ValueError:
                                        print("invalid withdrawl amount has been typed")
                            elif choice==3:
                                    write_logs('user selected current balance')
                                    write_logs(str(datetime.datetime.now()))
                                    time.sleep(2)
                                    print("loading users bank details")
                                    time.sleep(2)
                                    print("UR CURRENT BALANCE IS",money)
                                    write_logs("user checked his bank balance")
                                    write_logs(str(datetime.datetime.now()))
                            elif choice==4:
                                    print("thank you for choosing our bank")
                                    write_logs("user left the app")
                                    write_logs(str(datetime.datetime.now()))
                                    exit()
                            else:
                                print("invalid pin")
                        except ValueError:
                                print("please enter the correct choice")
                except ValueError:
                    print("invalid choice")
            else:
                print("invalid pin number try again")
                i-=1
                print("u have this many attempts left",i)
                if i==3:
                     print("attempts finished",i)
                     break
                
atm_system()
