import gspread
import time


class Sheet:
    def __init__(self, sheet_name):
        self.sheet_tickets = None
        self.sheet_name = sheet_name
        self.client = gspread.service_account(filename="client_secret.json")
        self.sheet_id = self.get_sheet_id()
        self.sheet = self.client.open(self.sheet_name).get_worksheet_by_id(
            self.sheet_id
        )

    def get_sheet_id(self):
        sheets = self.client.open(self.sheet_name).worksheets()
        return sheets[-2].id

    def get_values(self):
        list_of_records = self.sheet.get_all_values()
        return list_of_records

    def insert_ticket(self, row, skip, index):
        for i in range(len(row)):
            self.sheet.update_cell(index, i + 1 + skip, row[i])

        time.sleep(8)

    def get_sheet_tickets(self):
        self.sheet_tickets = list()

        number_of_tickets = len(self.sheet.col_values(1))

        if number_of_tickets >= 60:
            self.sheet_tickets, number_of_tickets = self.get_sheet_tickets_long()

        else:
            print(f"Total Number of Tickets: {number_of_tickets - 1}")
            print("Loading Tickets ...")

            for i in range(number_of_tickets - 1):
                self.sheet_tickets.append(self.sheet.cell(i + 2, 1).value)

        return self.sheet_tickets, number_of_tickets

    def get_sheet_tickets_long(self):
        self.sheet_tickets = list()

        number_of_tickets = len(self.sheet.col_values(1))

        print(f"Total Number of Tickets: {number_of_tickets - 1}")
        print("^^ Packets are flowing through the internet to you ^^")

        for i in range(number_of_tickets - 1):
            self.sheet_tickets.append(self.sheet.cell(i + 2, 1).value)
            if i % 10 == 0:
                time.sleep(7)

        return self.sheet_tickets, number_of_tickets

    def update_field(self, row, column, value):
        self.sheet.update_cell(row, column, value)
        time.sleep(1)

    def get_sheet_name(self):
        return self.sheet.title
