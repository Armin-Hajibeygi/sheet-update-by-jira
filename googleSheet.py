import gspread, time

class Sheet:
    def __init__(self, sheet_name, sheet_id) :
        self.client = gspread.service_account(filename='client_secret.json')
        self.sheet = self.client.open(sheet_name).get_worksheet_by_id(sheet_id)

    
    def get_values(self):
        list_of_records = self.sheet.get_all_values()
        return(list_of_records)

    
    def insert_ticket(self, row, index):
        for i in range(len(row)):
            self.sheet.update_cell(index, i+1, row[i])
        
        time.sleep(5)

    
    def get_sheet_tickets(self):
        self.sheet_tickets = list()
        
        number_of_tickets = len(self.sheet.col_values(1))

        print(f"Total Number of Tickets: {number_of_tickets - 1}")

        for i in range(number_of_tickets - 1):
            self.sheet_tickets.append(self.sheet.cell(i+2, 1).value)
        
        return self.sheet_tickets, number_of_tickets