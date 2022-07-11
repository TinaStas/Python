from replit import clear
from art import logo

num1=int(input("What's the first number?: "))
print("+ \n-\n* \n/")
operation=input("Pick an operation: ")
num2=int(input("What's the next number?: "))
stop_calculation=False 

def calc(first_number,next_number,op):
  while not stop_calculation:
    if op == "+":
      res=first_number+next_number
      print(f"{first_number} {op} {next_number} = {res}")
    elif op == "-":
      res=first_number-next_number
      print(f"{first_number} {op} {next_number} = {res}")
    elif op == "*":
      res=first_number*next_number
      print(f"{first_number} {op} {next_number} = {res}")
    elif op == "/":
      res=first_number/next_number
      print(f"{first_number} {op} {next_number} = {res}")
      
    question=input(f"Type \"y\" to coninue calculating with {res}, or type \"n\" to start a new calculation:\n")
    if question == 'n':
      stop_calculation==True
      first_number=int(input("What's the first number?: "))
      op=input("Pick an operation: ")
      next_number=int(input("What's the next number?: "))
      
    else:
      stop_calculation==False 
      first_number = res
      op=input("Pick an operation: ")
      next_number=int(input("What's the next number?: "))
 
    
result=calc(num1,num2,operation)
print(f"{num1} {operation} {num2} = {result}")
 

