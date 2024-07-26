number = int(input("Number: "))

mono_digit = {
    1 : "One",
    2 : "Two",
    3 : "Three",
    4 : "Four",
    5 : "Five",
    6 : "Six",
    7 : "Seven",
    8 : "Eight",
    9 : "Nine"
}

di_digit1 = {
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen', 
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen', 
    17: 'Seventeen', 
    18: 'Eighteen',
    19: 'Nineteen'
}

di_digit2= {
    2: "Twenty", 
    3: "Thirty", 
    4: "Forty", 
    5: "Fifty", 
    6: "Sixty", 
    7: "Seventy", 
    8: "Eighty", 
    9: "Ninety"
}


def convert(num):
    word = ""
    if num//100 >= 1:
        word += mono_digit.get(num//100) + " Hundred"

    rem = num%100
    try:
        word += " " + di_digit1.get(rem)
    except:
        a = rem//10
        if a >= 1:
            word += " " + di_digit2.get(a)
        if rem%10 >= 1:
            word += " " + mono_digit.get(rem%10)
    return word.strip()


def final_convert(num):
    output = ""
    if num == 0:
        return "Zero"
    if 10**9-1 < num < 10**12:
        n = num//10**9
        output += convert(n) + " Billion "
        num -= n*10**9
    if 10**6-1 < num < 10**9:
        n = num//10**6
        output += convert(n) + " Million "
        num -= n*10**6
    if 10**3-1 < num < 10**6:
        n = num//10**3
        output += convert(n) + " Thousand "
        num -= n*10**3
    if 1 <= num < 10**3:
        output += convert(num)

    return output.strip()


print(final_convert(number))