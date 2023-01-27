import random
import string
from abc import ABC, abstractmethod

def generate_id(lenght=8):
    return ''.join(random.choices(string.ascii_uppercase, k=lenght))

class SupportTicket:
    def __init__(self, customer, issue) -> None:
        self.id = generate_id()
        self.customer = customer
        self.issue = issue

class Strategy(ABC):
    @abstractmethod
    def execute(self, ticket_list):
        pass
        
    
class ConcreteStrategyQueu(Strategy):
    def execute(self, ticket_list):
        return ticket_list.copy()

class ConcreteStrategyStack(Strategy):
    def execute(self, ticket_list):
        return reversed(ticket_list.copy())

class ConcreteStrategyRand_item(Strategy):
    def execute(self, ticket_list):
        list_copy = ticket_list.copy()
        random.shuffle(list_copy)
        return list_copy

class CustomerSupport:
    def __init__(self, processing_strategy) -> None:
        self.tickets = []
        self.processing_strategy = processing_strategy

    def create_ticket(self, customer, issue):
        self.tickets.append(SupportTicket(customer, issue))

    def process_tickets(self):
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!!")
            return
        
        ticket_list = self.processing_strategy.execute(self.tickets)

        for ticket in ticket_list:
            self.process_ticket(ticket)


    def process_ticket(self, ticket):
        print("============================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("============================")

app = CustomerSupport(ConcreteStrategyQueu())

app.create_ticket("John Snow", "My computer make strange sounds!!!")
app.create_ticket("Sebastian Santos", "I can't upload any videos, help me!!!")
app.create_ticket("John Sena", "VScode doesn't work.")

app.process_tickets()