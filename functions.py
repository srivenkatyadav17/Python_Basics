def total_exp(exp):
    total = 0
    for i in exp:
        total = total + i
    return total


tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

print('Toms total is ', total_exp(tom_exp_list))
print('Joes total is ', total_exp(joe_exp_list))
