win_num = [3,7,6]
new_num = ""
def win_check(win_num):

    for i in range(len(win_num)):
        for j in range(len(win_num)):
            for k in range(len(win_num)):
                if i + 2 < len(win_num):
                    if win_num[i] + win_num[j] + win_num[k] == 15 and i != j != k != i:
                        return True
                    
print(win_check(win_num))
