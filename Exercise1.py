"""
R-1. Write a short Python script, that takes two numbers values, where one of them is the hours worked by 
employee and the other is the rate, the equation to calculate the payment is (hours * rate), but if the 
hours is more than 40 the equation is (hours * rate + (hours - 40) * rate * 0.5). So we need a script to 
do this automatically.
"""

def payment(hours, rate):
    """_summary_

    Args:
        hours (int): _description_
        rate (float): _description_
    """
    if hours > 40:
        amount = hours * rate + (hours - 40) * rate * 0.5
    else:
        amount = hours * rate
        
    return amount

if __name__ == "__main__":
    hours = int(input('Number of hours worked: '))
    rate = float(input('Employee rate: '))
    
    print(payment(hours, rate))
    