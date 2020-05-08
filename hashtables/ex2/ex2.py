#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    tickets_cache = {}
    for i in range(0, length):
        tickets_cache[tickets[i].source] = tickets[i].destination
    route = []
    ticket_destination = tickets_cache["NONE"]
    while ticket_destination != "NONE":
        route.append(ticket_destination)
        ticket_destination = tickets_cache[ticket_destination]
    route.append("NONE")
    return route
