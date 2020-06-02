def dec_to_base(num,base):  #Maximum base - 36
    base_num = 0
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += dig
        num //= base
    return base_num


print(dec_to_base(47,5))