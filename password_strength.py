import string


def dupli_count(array, string):
    count = 0
    for i in array:
        count += string.count(i)

    return count


def max_li(li):
    maxn = li[0]
    for i in range(1, len(li)):
        if li[i] > maxn:
            maxn = li[i]

    return maxn


def psc(password):
    score = 0
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    symbols = string.punctuation
    nums = "0123456789"

    lc = set(lower).intersection(set(password))
    lc_pc = dupli_count(lc, password)/len(password)*100
    uc = set(upper).intersection(set(password))
    uc_pc = dupli_count(uc, password)/len(password)*100
    sc = set(symbols).intersection(set(password))
    sc_pc = dupli_count(sc, password)/len(password)*100
    nc = set(nums).intersection(set(password))
    nc_pc = dupli_count(nc, password)/len(password)*100

    pass_chars_pc = [lc_pc, uc_pc, sc_pc, nc_pc]



    for i in password:
        if i in lower:
            score += 1
        elif i in upper:
            score += 1
        elif i in symbols:
            score += 1
        elif i in nums:
            score += 1


    if len(password) < 4:
        score -= 2
    elif 4 <= len(password) < 8:
        score -= 1


    if len(lc) == 0:
        score -= 1
    if len(uc) == 0: 
        score -= 1
    if len(sc) == 0:
        score -= 1
    if len(nc) == 0:
        score -= 1


    if max_li(pass_chars_pc) < 40:
        score += 2
    elif 40 <= max_li(pass_chars_pc) <= 50:
        score += 1
    elif 60 < max_li(pass_chars_pc) < 80:
        score -= 1
    elif max_li(pass_chars_pc) >= 80:
        score += -2


    if score <= 1:
        print("Very weak password")
    elif 1 < score < 5:
        print("Weak password")
    elif 5 <= score < 8:
        print("Medium password")
    elif 8 <= score <+ 12:
        print("Strong password")
    elif score > 12:
        print("Very strong password")
    
    return score

if __name__ == "__main__":
    print(psc(input("Password: ")))