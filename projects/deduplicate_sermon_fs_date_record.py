import os

if __name__ == "__main__":
    with open("sermon_fs_date_record.txt", "r") as fp:
        lines = fp.readlines()
        lines = [ _.strip() for _ in lines ]

    print(lines)
    c2t_dict = {}
    for line in lines:
        res = line.split(' ')
        dt_curr = res[0]
        ytc_curr = res[1]
        if ytc_curr not in c2t_dict:
            c2t_dict[ytc_curr] = dt_curr
        else:
            print(ytc_curr, dt_curr)

    with open("sermon_fs_date_record_deduplicated.txt", "w") as fp:
        for k_ in c2t_dict.keys():
            fp.write(f"{c2t_dict.get(k_)} {k_}\n")

