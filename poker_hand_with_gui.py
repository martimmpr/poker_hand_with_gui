import customtkinter

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")  

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.resizable(0, 0)
        self.geometry("900x175")
        self.iconbitmap("poker.ico")
        self.title("Poker")
        
        self.title = customtkinter.CTkLabel(self, text = "INSIRA AS CARTAS (Ex: 10c | Jc | Qc | Ac | Kc)", justify = "center", width = 250, height = 50, font = customtkinter.CTkFont(size = 25, weight="bold"))
        self.title.place(x = 175, y = 15)
        
        self.card1 = customtkinter.CTkEntry(self, placeholder_text = "1º", justify = "center", width = 50, height = 25, border_width = 1, corner_radius = 10)
        self.card1.place(x = 75, y = 75)
        self.card2 = customtkinter.CTkEntry(self, placeholder_text = "2º", justify = "center", width = 50, height = 25, border_width = 1, corner_radius = 10)
        self.card2.place(x = 250, y = 75)
        self.card3 = customtkinter.CTkEntry(self, placeholder_text = "3º", justify = "center", width = 50, height = 25, border_width = 1, corner_radius = 10)
        self.card3.place(x = 425, y = 75)
        self.card4 = customtkinter.CTkEntry(self, placeholder_text = "4º", justify = "center", width = 50, height = 25, border_width = 1, corner_radius = 10)
        self.card4.place(x = 600, y = 75)
        self.card5 = customtkinter.CTkEntry(self, placeholder_text = "5º", justify = "center", width = 50, height = 25, border_width = 1, corner_radius = 10)
        self.card5.place(x = 775, y = 75)
        
        def poker_hand():
            if (self.card1.get() != "") and (self.card2.get() != "") and (self.card3.get() != "") and (self.card4.get() != "") and (self.card5.get() != ""):
                cards = [self.card1.get(), self.card2.get(), self.card3.get(), self.card4.get(), self.card5.get()]
                
                if check_royal(cards) and check_flush(cards): #Royal Flush -> A, K, Q, J e 10, todos do mesmo naipe
                    return self.hand_result.configure(text = "Royal Flush")
                
                if check_straight(cards) and check_flush(cards): #Straight Flush -> Cinco cartas seguidas, todas do mesmo naipe
                    return self.hand_result.configure(text = "Straight Flush")
                
                if check_poker(cards): #Poker -> Quatro cartas com o mesmo valor
                    return self.hand_result.configure(text = "Poker")
                
                if check_trio(cards) and check_pair(cards): #Full House -> Um trio e um par
                    return self.hand_result.configure(text = "Full House")
                
                if check_flush(cards): #Flush -> Quaisquer 5 cartas do mesmo naipe, sem ser em sequência
                    return self.hand_result.configure(text = "Flush")

                if check_straight(cards): #Sequência -> Sequência de 5 cartas que não sejam todas do mesmo naipe
                    return self.hand_result.configure(text = "Sequência")
                
                if check_trio(cards): #Trio -> 3 cartas com o mesmo valor
                    return self.hand_result.configure(text = "Trio")
                
                if check_two_pairs(cards): #Dois Pares ->  Dois pares diferentes na mesma jogada
                    return self.hand_result.configure(text = "Dois Pares")
                
                if check_pair(cards): #Par -> Dois cartas do mesmo valor
                    return self.hand_result.configure(text = "Par")
                
                return self.hand_result.configure(text = "Carta Alta") #Carta Alta -> Nenhuma das combinações anteriores
            else:
                self.hand_result.configure(text = "Insira as 5 cartas!")
         
        def check_royal(cards):
            royal_values = ["A", "K", "Q", "J", "10"]
            royal = False
            
            for card in cards:
                if card[:-1] in royal_values:
                    royal = True
                else:
                    royal = False
            
            return royal

        def check_flush(cards):
            suits = []
            flush = False
            
            for card in cards:
                suits.append(card[-1])

            if len(set(suits)) == 1:
                flush = True
            
            return flush

        def check_straight(cards):
            values = []
            cards_values = {"J":11, "Q":12, "K":13, "A":14}
            sequence = False
            
            for i in range(0, len(cards)):
                if cards[i][0] in cards_values:
                    cards[i] = f"{cards_values[cards[i][0]]}{cards[i][-1]}"
            
            for card in cards:
                values.append(int(card[:-1]))
            
            if sorted(values) == list(range(min(values), max(values) + 1)):
                sequence = True
            
            return sequence

        def check_poker(cards): 
            counter = {}
            poker = False 
            
            for card in cards:
                card_number = card[:-1]
                try:
                    if counter[card_number]:
                        counter[card_number] += 1
                    else:
                        counter[card_number] = 1
                except KeyError:
                    counter[card_number] = 1
                    
            for number in counter:
                if counter[number] == 4:
                    poker = True
                    break
            
            return poker

        def check_trio(cards):
            counter = {}
            trio = False 
            
            for card in cards:
                card_number = card[:-1]
                try:
                    if counter[card_number]:
                        counter[card_number] += 1
                    else:
                        counter[card_number] = 1
                except KeyError:
                    counter[card_number] = 1
                    
            for number in counter:
                if counter[number] == 3:
                    trio = True
                    break
            
            return trio

        def check_two_pairs(cards): 
            counter = {}
            amount = 0
            two_pairs = False 
            
            for card in cards:
                card_number = card[:-1]
                try:
                    if counter[card_number]:
                        counter[card_number] += 1
                    else:
                        counter[card_number] = 1
                except KeyError:
                    counter[card_number] = 1
                    
            for number in counter:
                if counter[number] == 2:
                    amount += 1
                    
            if amount == 2:
                two_pairs = True
            
            return two_pairs

        def check_pair(cards): 
            counter = {}
            amount = 0
            pair = False 
            
            for card in cards:
                card_number = card[:-1]
                try:
                    if counter[card_number]:
                        counter[card_number] += 1
                    else:
                        counter[card_number] = 1
                except KeyError:
                    counter[card_number] = 1
                    
            for number in counter:
                if counter[number] == 2:
                    amount += 1
                
            if amount == 1:
                pair = True
            
            return pair
        
        self.check_cards = customtkinter.CTkButton(self, text = "Verificar mão", command = poker_hand)
        self.check_cards.place(x = 380, y = 125)
        
        self.hand_result = customtkinter.CTkLabel(self, text = "", justify = "center", width = 250, height = 50, font = customtkinter.CTkFont(size = 20, weight="bold"))
        self.hand_result.place(x = 585, y = 112.5)
        
if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", quit())
    app.mainloop()

# "10c", "Jc", "Qc", "Ac", "Kc" -> Royal Flush
# "3c", "5c", "Qe", "9c", "Ao" -> Carta Alta
# "10e", "10p", "8o", "10o", "10c" -> Poker
# "4c", "9e", "2e", "2o", "Ao" -> Par
# "10e", "9e", "8e", "6e", "7e" -> Straight Flush
# "10p", "9p", "9e", "10e", "9c" -> Full House 
# "8c", "2c", "8e", "3e", "3p" -> Dois Pares
# "Jc", "9c", "7c", "5c", "2c" -> Flush
# "Ap", "Qp", "Ae", "Ac", "2o" -> Trio
# "Ao", "Ko", "Qo", "Jo", "9o" -> Flush
# "10c", "Jc", "Qe", "Ke", "Ap" -> Sequência
# "3c", "8c", "2e", "3e", "3o" -> Trio
# "4c", "Ap", "4e", "4o", "4p" -> Poker
# "3c", "8c", "2e", "3e", "2o" -> Dois Pares
# "8c", "8e", "Ae", "Qc", "Kc" -> Par
# "8c", "8e", "Ae", "Qc", "Kc" -> Par