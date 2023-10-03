class parkingGarage():
    def __init__ ( self, tick_list, parking_spaces, current_tickets,):
        self.tick_list = tick_list
        self.parking_spaces = parking_spaces
        self.current_tickets=current_tickets
        


    def taketicket(self):
        self.tick_list -= 1
        self.parking_spaces -=1
       
        

    def payHere(self):
        transaction=input("Please swipe your card. (type '50 cent payment')")
        if transaction != "50 cent payment":
            print("Please complete your payment or try again.")
        elif transaction == "50 cent payment":
            first_name=input("what is your first name?")
            self.current_tickets[first_name + " paid"]=True
            print("thank you for your payment, you can remain parked for 15 minutes.")
        
   
    def leave(self):
        self.tick_list += 1
        self.parking_spaces += 1
        checkout=input("what is the name you used to sign in?")
        if checkout in self.current_tickets:
            del self.current_tickets[checkout]
        print("Thank you for coming, have a nice day.")

    def showList(self):
        if len(self.current_tickets) == 0:
            print("No entries yet.")
        elif len(self.current_tickets) != 0:
            for k, v in self.current_tickets.items(parkingGarage):
                print(k,v)


UseGarage=parkingGarage(200,200,{})
def useGarage():
    while True:
        comeOrgo=input("Would you like to 'park', 'leave', 'check roster' or 'quit'?")
        if comeOrgo.lower() == 'park':
            UseGarage.taketicket()
            UseGarage.payHere()
        elif comeOrgo.lower()== 'leave':
            UseGarage.leave()
        elif comeOrgo.lower()== 'quit':
            print("Thank you have a good day.")
        elif comeOrgo.lower() == 'check roster':
            UseGarage.showList()
        else:
            print("Please resubmit an answer.")

useGarage()
