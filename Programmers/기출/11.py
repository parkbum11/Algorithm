def solution(program, flag_rules, commands):
    answer = []
    new_flag_rules = {}
    null_flage_name = ''
    check_num = '0123456789'
    check_str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    for i in flag_rules:
        flag_name, flag_argument_type = i.split()
        new_flag_rules[flag_name] = flag_argument_type
        if flag_argument_type == 'NULL': null_flage_name = flag_name

    for c in commands:
        result = True
        new = c.split()
        new_commands = []
        flag_argus = []

        if new[0] != program:
            answer.append(False)
            continue

        for n in new[1:]:
            if n[0] == '-':
                if len(flag_argus) != 0:
                    new_commands.append(flag_argus)
                    flag_argus = []
                flag_argus.append(n)
            else:
                flag_argus.append(n)
        if len(flag_argus) != 0: new_commands.append(flag_argus)
        for n in new_commands:
            if n[0] == null_flage_name:
                if len(n) != 1:
                    result = False
                    break
            else:
                if len(n) <= 1:
                    result = False
                    break
                if new_flag_rules[n[0]] == "NUMBER":
                    if len(n) != 2:
                        result = False
                        break
                    else:
                        for nn in n[1:]:
                            for nnn in nn:
                                if nnn not in check_num:
                                    result = False
                                    break
                elif new_flag_rules[n[0]] == "STRING":
                    if len(n) != 2:
                        result = False
                        break
                    else:
                        for nn in n[1:]:
                            for nnn in nn:
                                if nnn not in check_str:
                                    result = False
                                    break
            if result == False: break
        answer.append(result)
    return answer