from datetime import date
class User():
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.is_logged_in = False 
    
    def user_acct(self):
        self.name = input('Please enter name: ')
        self.email = input('Please enter email: ')
        self.phone = input('Please enter phone number: ')
        password = input('Please enter password: ')

        users_file_name = "log.csv"
        users_file = open(users_file_name, "a")

        users_file.write(f"{self.name},{password},{self.email},{self.phone} \n")
        users_file.close()
   
    def login(self):
        input_name = input("please enter your name: ")
        input_password = input("please enter your password: ")

        users_file_name = "log.csv"
        users_file = open(users_file_name, "r")

        for line in users_file.readlines():
            # print(line.split(","))
            name, saved_password, email, phone = line.split(",")
        
            if name == input_name:

                if saved_password == input_password:  #match password value
                    self.is_logged_in = True
                    
                    self.name = name
                    self.email = email
                    self.phone = phone

                    print(f'successfully logged in {self.name}')

                    return

                else: 
                    print('sorry wrong password try logging in again')
                    self.login()
        else:
            print("sorry your username does not exist you woul have to create an account")
            self.user_acct()    
    
class List(User):

    def __init__(self, name = "nill", email =  "nill", phone = "nill"):
        super().__init__(name, email, phone)

        self.date = self.get_datestamp()

    def get_datestamp(self):
        day = date.today()
        return(day)

    def write_note(self):
        
        note = input('This is where you input your entry: ')
        print(f'{self.name} This is the entry for the day {self.date} which you wrote {note}')
    
    def storage(self, date, note):
        new_file = "notepads.csv"
        users_file = open(new_file, "a")

        users_file.write(f"{self.date},{note}\n")
        # users_file.close()
        print(date, note)
    def start(self):
        create = input("If you want to create a new account type 'n' for login type 'y': ")

        if create == 'y':
            self.login()
            proceed = input("type A to begin to write: ")
            A = self.write_note()

        else:
            self.user_acct()
            proceed = input("type A to begin to write: ")
            A = self.write_note()
y = List()
y.start()
# y = List('flora', 'floraoladipupo@gmail.com', 8106107331, 'hduk')
# print(y.date)
# y.write_note()

    # def to_do_list(self):
        