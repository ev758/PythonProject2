import csv

def read_csv():
    with open(csvfile, newline="") as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row)
            if row[2] not in rating_list:
                rating_list.append(row[2])

try:
    csvfile = input("Enter csv file: ")
    in_csvfile = open(csvfile)
    num = 0
    title_list = list()
    rating_list = list()
    showtime_dict = {}
    read_csv()
    print('\n')
    
    for line in in_csvfile:
        csvfile_line = line.split(',')
        if csvfile_line[1] not in title_list:
            title_list.append(csvfile_line[1])
        
        if csvfile_line[1] not in showtime_dict.keys():
            showtime_list = []
            showtime_list.append(csvfile_line[0])
            showtime_dict[csvfile_line[1]] = showtime_list
        else:
            showtime_dict[csvfile_line[1]].append(csvfile_line[0])
    
    for title in title_list:
        if (len(title) > 44):
            title_list[num] = title[0:44]
            num += 1
        else:
            num += 1
    
    txt = '{:<44} | {:>5} | '
    for x in range(0, num):
        print(txt.format(title_list[x], rating_list[x]), end="")
        
        for key in showtime_dict.keys():
            if (title_list[x] == key):
                print(showtime_dict[key])
                break
            elif (title_list[x] == key[0:44]):
                if (len(key) > 44):
                    print(showtime_dict[key])
                    break
                
    in_csvfile.close()
    
except FileNotFoundError:
    print('csv file not found')