class user:
    def __init__(self,name,address,Adhar_no,contact_no,email,password,b):
        self.name=name
        self.address=address
        self.Adhar_no=Adhar_no
        self.contact_no=contact_no
        self.email=email
        self.password=password
        self.b=b

        
    def __str__(self):
        return str(self.name)+"\t"+(self.address)+"\t"+str(self.Adhar_no)+"\t"+str(self.contact_no)+"\t"+(self.email)+"\t"+str(self.password)+"\t"+str(self.b)

class user1:
    def __init__(self,name,address,Adhar_number,contact,email,password,c):
        self.name=name
        self.address=address
        self.Adhar_number=Adhar_number
        self.contact=contact
        self.email=email
        self.password=password
        self.c=c
        
    def __str__(self):
        return str(self.name)+"\t"+(self.address)+"\t"+str(self.Adhar_number)+"\t"+str(self.contact)+"\t"+(self.email)+"\t"+str(self.password)+"\t"+str(self.c)



class IDBI:
    print("\t\t\t\t-----------------  Welcome To SafeBank ----------------------");
    print("                     ")
    print("===================================================================")

    user=[]
    user1=[]
    def call(self):
        cho=1
        while cho>0:
            print("Enter The 1     =============> For Create Open Saving Account  <====================")
            print("Enter The 2     =============> For Open Current Account  <==========================")
            
            ch=int(input("Enter The Num : "))
            
            if ch==1:
                self.name=input("Enter The Name : ")
                self.address=(input("Enter The address : "))
                self.Adhar_no=(input("Enter The Adhar_no : "))
                self.contact_no=int(input("Enter The Contact_no : "))
                self.email=(input("Enter The email : "))
                self.password=(input("Enter The password : "))
                print("\t\t\t  --------------------------------")
                print("\t\t\t  =====>  User Information <=====:")
                print("                           ")
                print("\t\t\t  --------------------------------")


                self.b=(self.Adhar_no[::-1])
                print("\t\t ==> Your Account No Is Generated : ",self.b)
                print("\t\t ==> your User Name is :",self.email)
                print("\t\t ==> Your Password is : ",self.password)

                print("---------------------------")
                print("---------------------------")
                a=user(self.name,self.address,self.Adhar_no,self.contact_no,self.email,self.password,self.b)
                self.user.append(a)

                
                 
            elif ch==2:
                self.name=input("Enter The Full Name : ")
                self.address=input("Enter The Address : ")
                self.Adhar_number=input("Enter The Adhar Number : ")
                self.contact=int(input("Enter The Contact Number : "))
                self.email=input("Enter The Email Address : ")
                self.password=input("Enter The Password : ")
                print("\t\t\t-----------------------")
                print("\t\t\t==>  User Information :")
                print("                             ")
                print("\t\t\t-----------------------")

                self.c=(self.Adhar_number[::-1])
                print("\t\t ==> Your Account No Is Generated : ",self.c)
                print("\t\t ==> your User Name is : ",self.email)
                print("\t\t ==> Your Password is : ",self.password)

                print("                           ")
                print("---------------------------")
                B=user1(self.name,self.address,self.Adhar_number,self.contact,self.email,self.password,self.c)
                self.user1.append(B)

            print("1 for saving account")
            print("2 for current account")
            print("---------------------------")

            choice=int(input("Enter The Number : "))
            print("---------------------------")
            if choice==1:

                while choice>0:
                    print("Enter The 1 ==> For Login Account  ")
                    print("Enter The 2 ==> check The Total Accounts  ")
                    print("Enter The 3 ==> For Exite  ")
                    choi=int(input("select The Number : "))
            
                    if choi==1:
                        
                
                            print("\t                ----------------------------------------")
                            print("                                                          ")
                            print("\t                ---------------Login Page---------------")
                            print("                                                          ")
                            print("\t                ----------------------------------------")
                            nam=input("Enter Your email/User Name : ")
                            password=input("Enter Your Password : ")
                            for i in self.user:
                                amt=0
                                while choice==1:
                        
                    
                                    if i.email==nam and i.password ==password:
                                
                                        print("1 For check The User Details")
                                        print("2 For Deposite")
                                        print("3 For Withdraw")
                                        print("4 For check Balance")
                                        print("5 For Logout Account")

                                        check=int(input("Enter The Num : "))
                            
                                        if check==1:
                                            print("---------------------------")
                                

                                            for j in self.user:
                                                if j.email==nam:
                                                    print(j)
                                            print("---------------------------")
                                            print("                           ")
   
                                  
                                        elif check==2:
                                            
                                            deposite=int(input("Enter The Deposite Ammount : "))
                                            print("---------------------------")
                                            amt = amt + deposite
                                            print("Deposite Succesfully",amt)
                                            print("                           ")
                                            print("---------------------------")

                                        elif check==3:
                                            w=int(input("Enter The Withdraw Ammount : "))
                                            print("---------------------------")
                                            if amt>=w:
                                                print("Withdraw Successfully",w)
                                                amt = amt - w
                                                print("Total Amount Is Your Account",amt)
                                            
                                            else:
                                                print("Insefficiant Balance",amt)
                                            print("                           ")
                                            print("---------------------------")

                                        elif check==4:
                                            a=input("Enter The Account No : ")
                                            print("---------------------------")
                                            if self.b==a:
                                            
                                                print("Total  Amount Is:",amt)
                                            print("                           ")
                                            print("---------------------------")

                                        elif check==5:
                                            break
                        
    
                                        else:
                                            print("please Enter correct Password ")

                            

                    elif choi==2:
                        print("-------------------------------------")
                        print(' Total Accounts Are :' ,len(self.user))
                        print("                                     ")
                        print("-------------------------------------")
                    elif choi==3:
                        exit()
                    else:
                        print("Enter Your Correct Number : ")

            
            elif choice==2:

                while choice>0:
                    print("Enter The 1 --> For Login Account : ")
                    print("Enter The 2 --> check The Total Accounts : ")
                    print("Enter The 3 --> For Exite : ")
                    print("                              ")
                    choi=int(input("select The Number : "))
            
                    if choi==1:
                        
                
                            print("\t\t----------------------------------------")
                            print("                                            ")
                            print("\t\t---------------Login Page---------------")
                            print("                                            ")
                            print("\t\t----------------------------------------")
                            nam=input("Enter Your email/User Name : ")
                            password=input("Enter Your Password :   ")
                            for i in self.user1:
                                amount=0
                                while choi==1:
                        
                    
                                    if i.email==nam and i.password ==password:
                                
                                        print("1 For check The User Details")
                                        print("2 For Deposite")
                                        print("3 For Withdraw")
                                        print("4 For check Balance")
                                        print("5 For Logout Account")

                                        check=int(input("Enter The Number : "))
                            
                                        if check==1:
                                            print("---------------------------")
                                

                                            for j in self.user1:
                                                if j.email==nam:
                                                    print(j)
                                            print("                           ")
                                            print("---------------------------")

                                  
                                        elif check==2:
                                            deposite=int(input("Enter The Deposite Amount : "))
                                            amount = amount + deposite
                                            print("---------------------------")
                                            print("Deposite Succesfully  ",amount)
                                            print("                           ")
                                            print("---------------------------")

                                        elif check==3:
                                            w=int(input("Enter The Withdraw Ammount : "))
                                            print("---------------------------")
                                            if amount>=w:
                                                print("Withdraw Successfully  ",w)
                                                amount = amount - w
                                                print("Total Amount Is Your Account  ",amount)
                                            else:
                                                print("Insefficiant Balance  ",amount)
                                            print("                           ")
                                            print("---------------------------")
                                        elif check==4:
                                            print("---------------------------")
                                            a=input("Enter The Account No :  ")
                                    
                                            if self.c==a:
                                                print("---------------------------")
                                            
                                                print("Total  Amount Is : ",amount)
                                                print("                           ")
                                                print("---------------------------")

                                        elif check==5:
                                            break
                        
    
                                        else:
                                            print("please Enter correct Password ")

                            

                    elif choi==2:
                        print(' Total Accounts Are : ' ,len(self.user1))
                    elif choi==3:
                        exit()
                    else:
                        print("Enter Your Correct Number : ")

                


        


    

a=IDBI()
a.call()
a.dis()

