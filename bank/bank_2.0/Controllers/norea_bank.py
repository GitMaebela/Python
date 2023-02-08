import datetime

# BankStatement
# import datetime
from fpdf import FPDF
import smtplib, ssl


# bank, offers various types of savings account transactions, including:

# Deposits: You can deposit money into your savings account using various methods, such as cash deposits at an ATM, online banking, or mobile banking.

# Withdrawals: You can withdraw money from your savings account using an ATM, online banking, or mobile banking.

# Transfers: You can transfer money between your Absa accounts or to other Absa clients.

# Bill payments: You can use your savings account to pay bills, such as utility bills, insurance premiums, and other recurring payments.

# Debit orders: You can set up automatic debit orders to pay your bills or make regular payments from your savings account.

# Card purchases: You can use your Absa debit card to make purchases, including online purchases.

# Interest payments: Your savings account will earn interest, and the interest will be paid into your account on a regular basis.

class BankAccount:
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance
		self.transaction_history = []

	def deposit(self, amount):
		self.balance += amount
		self.transaction_history.append({'transaction_type': 'deposit', 'amount': amount, 'date': datetime.datetime.now()})
		print(f"Deposited {amount} to {self.name}'s account. New balance: {self.balance}")

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
			self.transaction_history.append({'transaction_type': 'withdraw', 'amount': amount, 'date': datetime.datetime.now()})
			print(f"Withdrew {amount} from {self.name}'s account. New balance: {self.balance}")
		else:
			print(f"Insufficient balance in {self.name}'s account. Current balance: {self.balance}")

	def check_balance(self):
		print(f"{self.name}'s current balance: {self.balance}")

	def view_transaction_history(self, period_in_months):
		period_in_seconds = period_in_months * 30 * 24 * 60 * 60
		current_time = datetime.datetime.now().timestamp()
		transaction_history_in_period = [
			transaction for transaction in self.transaction_history
			if current_time - transaction['date'].timestamp() < period_in_seconds
		]
		print(transaction_history_in_period)



# creating a sample account
sample_account = BankAccount("John Doe", 5000)

# making some transactions
sample_account.deposit(1000)
sample_account.withdraw(500)
sample_account.deposit(2000)

# viewing transaction history for the past 3 months
sample_account.view_transaction_history(3)






class PDFStatement:
	def __init__(self, transaction_history):
		self.transaction_history = transaction_history

	def generate(self):
		pdf = FPDF()
		template = Template(pdf)
		template.parse_html(open("template.html", "r").read(), x_pos=XPos.ABSOLUTE, y_pos=YPos.ABSOLUTE)
		template.render()
		pdf.output("transaction_history.pdf")




import os
from fpdf import FPDF
from fpdf.enums import XPos, YPos
from fpdf.template import Template


class BankStatement:
	def __init__(self, account, period_in_months):
		self.account = account
		self.period_in_months = period_in_months
		self.transaction_history = self.get_transaction_history()

	def generate_pdf_statement(self):
		pdf_statement = PDFStatement(self.transaction_history)
		pdf_statement.generate()



import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

class BankHistoryPDF:
	def __init__(self, bank_history, recipient_email):
		self.bank_history = bank_history
		self.recipient_email = recipient_email

	def generate_pdf(self, filename):
		# generate the PDF of the bank history using a library such as pdfkit or fpdf
		# code to generate the PDF goes here

		# send the PDF as an attachment in an email
		from_email = "sender_email@example.com"
		to_email = self.recipient_email
		password = "sender_email_password"

		msg = MIMEMultipart()
		msg['From'] = from_email
		msg['To'] = to_email
		msg['Subject'] = "Traditional Bank History"

		part = MIMEBase('application', "octet-stream")
		part.set_payload(open(filename, "rb").read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment', filename=filename)
		msg.attach(part)

		try:
			server = smtplib.SMTP('smtp.gmail.com', 587)
			server.ehlo()
			server.starttls()
			server.login(from_email, password)
			server.sendmail(from_email, to_email, msg.as_string())
			server.close()
			print("Email sent successfully")
		except:
			print("Failed to send email")








import os
from bank import Bank
from generate_pdf import PDF
from send_email import Email

# Initialize the bank object
bank = Bank()

# Get the 3-month traditional history
history = bank.get_tradition_history(3)

# Generate a PDF file
pdf = PDF()
pdf.generate_pdf(history)

# Send the PDF file via email
email = Email()
email.send_email(pdf.pdf_file)

print("The traditional history PDF has been generated and sent via email successfully!")
