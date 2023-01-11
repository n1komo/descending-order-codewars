
def descending_order(num):
    num_in_string_format = str(num)
    temp_list = []
    rdy_num = 0
    for i in num_in_string_format:
        temp_list.append(i)
    temp_list = sorted(temp_list, reverse=True)
    rdy_num = int(''.join(temp_list))
    return rdy_num


# sample tests
descending_order(4446712)
descending_order(4442134562345612)
descending_order(446749678467712)
descending_order(44093456092346509234780512)