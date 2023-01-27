import random
import string

def generate_id(lenght=8):
    return ''.join(random.choices(string.ascii_uppercase, k=lenght))

class SupportTicket:
    def __init__(self, customer, issue) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class Strategy:
    def execute(list_items):
        pass
        
    
class ConcreteStrategyQueu(Strategy):
    def execute(list_items):
        return list_items

class ConcreteStrategyStack(Strategy):
    def execute(list_items):
        return reversed(item_list)

class ConcreteStrategyRand_item(Strategy):
    def execute(list_items):
        list_copy = list_items.copy()
        random.shuffle(list_copy)
        return list_copy

class CustomerSupport:
    def __init__(self, processing_strategy=queu) -> None:
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!!")
            return
        
        for ticket in self.processing_strategy(self.tickets):
            self.process_ticket(ticket)

    def process_ticket(self, ticket):
        print("============================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("============================")

app = CustomerSupport("random")

app.create_ticket("John Snow", "My computer make strange sounds!!!")
app.create_ticket("Sebastian Santos", "I can't upload any videos, help me!!!")
app.create_ticket("John Sena", "VScode doesn't work.")

app.process_tickets()