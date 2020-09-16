"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!\nIt can add and subtract whole numbers from zero to five!')

a, b, c = input('Please choose your first number (zero to five): '),input('What do you want to do? plus or minus: '), input('Please choose your second number (zero to five): ')

def operaciones(a,b,c):
    nums = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5}
    result = ["zero","one", "two", "three", "four", "five","six","seven","eight","nine","ten"]
    if b == "plus":
        print(result[nums[a] + nums[c]])
    elif b == "minus":
        d = nums[a] - nums[c]
        print(a,c, d)
        if d >= 0:
            print(result[d])
        else:
            print(f"minus {result[-d]}")
    else:
        return "I am not able to answer this question. Check your input.\nThanks for using this calculator, goodbye :)"

if __name__ == "__main__": 
    operaciones(a,b,c)
