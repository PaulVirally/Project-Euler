units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def num_to_len_word(n):
    s = str(n)
    l = len(s)
    out = ''

    for i in range(l):
        dig = int(s[i])
        place = l - i

        if place == 4:
            out += 'onethousandand'

        elif place == 3:
            if dig != 0:
                out += units[dig - 1] + 'hundredand'

        elif place == 2:
            if dig == 1:
                out += teens[int(s[i + 1])]
                break
            elif dig != 0:
                out += tens[dig - 1]

        elif place == 1:
            if dig != 0:
                out += units[dig - 1]

    if out.endswith('and'):
        out = out[:-3]

    return len(out)

total = 0
for i in range(1, 1001):
    total += num_to_len_word(i)

print(total)