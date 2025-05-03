def call_center(clients, recipients):
    # Найдем клиентов, которые не видели промо-емейл
    clients_set = set(clients)
    recipients_set = set(recipients)
    return list(clients_set - recipients_set)

def potential_clients(participants, clients):
    # Найдем участников, которые не являются клиентами
    participants_set = set(participants)
    clients_set = set(clients)
    return list(participants_set - clients_set)

def loyalty_program(clients, participants):
    # Найдем клиентов, которые не участвовали в мероприятии
    clients_set = set(clients)
    participants_set = set(participants)
    return list(clients_set - participants_set)

def main():
    # Данные
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    
    # Прочитаем аргумент командной строки
    import sys
    if len(sys.argv) != 2:
        raise Exception("Please provide exactly one task: call_center, potential_clients, or loyalty_program.")
    
    task = sys.argv[1]
    
    # Выполним соответствующую задачу
    if task == "call_center":
        result = call_center(clients, recipients)
        print("Clients who did not see the promotional email:")
    elif task == "potential_clients":
        result = potential_clients(participants, clients)
        print("Participants who are not clients:")
    elif task == "loyalty_program":
        result = loyalty_program(clients, participants)
        print("Clients who did not participate in the event:")
    else:
        raise Exception("Invalid task. Choose from: call_center, potential_clients, or loyalty_program.")
    
    # Выведем результат
    for email in result:
        print(email)

if __name__ == '__main__':
    main()
