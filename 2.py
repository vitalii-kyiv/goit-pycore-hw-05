import re

text = "Загальний дохід працівника складається з декількох частин: як основний дохід, доповнений додатковими надходженнями 10.25 і 5555.22 доларів."

def generator_numbers(text:str):
    pattern = r'\b\d+\.\d+|\b\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group()) 


def sum_profit(text: str, func):
    if not text:
        return "Рядок не передано або він пустий"
    
    return sum(func(text)) 
    
print(sum_profit(text, generator_numbers))