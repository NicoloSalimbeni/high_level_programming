"""exercisi 4 week 4"""
# load the binary file named credit_card.dat and convert the data
# into the real credit-card number. Each line correspond to a
# credit card number. Each character is composed by 6 bit (even
# the space) and the last 4 bit are just a padding

with open("credit_card.dat", 'r') as f:
    # loop on lines
    for line in f:
        if len(line) < 6:
            print("\nFile readed completly")
        else:
            num = []
            for i in range(19):
                num.append(chr(int(line[i * 6:(i + 1) * 6], 2)))
            card = "".join(num)
            print(card)
