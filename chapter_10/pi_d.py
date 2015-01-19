new_filename = 'pi_thousand_digits.txt'

with open('pi_million_digits.txt') as f:
    lines = f.readlines()


pi = lines[0].rstrip()

decimals = pi[2:]
print(decimals[:10])
print(len(decimals))

with open(new_filename, 'w') as f:
    index = 0
    digits = 0
    f.write('3.')
    while digits < 1000:
        new_digits = decimals[index:index+100]
        if index > 0:
            prefix = '  '
        else:
            prefix = ''
        f.write(prefix + new_digits + '\n')
        index += 100
        digits += 100
