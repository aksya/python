import sys
import csv

def day_up_value(list, max_value):
    day = 0
    for closing_price in list:
        if closing_price > max_value: 
            day = day + 1
    return day
    

def main(file_name,max_value, file_name_print):
    with open(file_name) as f:
        f.readline()
        csv_file = csv.reader(f, delimiter=',')
        list = []
        for row in csv_file:
            #print(float((row[4])))
            x=float((row[4]))
            list.append(x)
    day = day_up_value(list, max_value)        
    #day = 0
    #for closing_price in list:
    #    if closing_price > max_value: 
    #        day = day + 1
    if file_name_print=="":
        print(day)
    else:
        f_out = open(file_name_print, 'w')
        f_out.write(str(day))
        print("В файл")
        
              
            


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        if len(sys.argv) > 2:
            max_value = sys.argv[2]
            if len(sys.argv) > 3:
                main(file_name,float(max_value),sys.argv[3])
            else:    
                main(file_name,float(max_value),"")
        else:
            print("Укажите уровень закрытия цены")
    else:    
        print("Укажите имя файла")