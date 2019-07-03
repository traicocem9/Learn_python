num_0 = [" _ _  ", 
         "|   | ",
         "|_ _| "]   
num_1 = ["   ",
         "/| ",
         " | "]
num_2 = [" _ _  ",
         " _ _| ",
         "|_ _  "]
num_3 = ["_ _  ",
         "_ _| ",
         "_ _| "]
num_4 = ["      ",
         "|_ _| ",
         "    | "]
num_5 = [" _ _  ",
        "|_ _  ",
        " _ _| "]
num_6 = [" _ _  ",
        "|_ _  ",
        "|_ _| "]
num_7 = ["_ _ ",
         "  / ",
         " /  "]
num_8 = [" _ _  ",
         "|_ _| ",
         "|_ _| "]
num_9 = [" _ _  ",
         "|_ _| ",
         " _ _| "]
symbol= ["    ",
         "  o ",
         "  o "]
   
font = [num_0, num_1, num_2, num_3, num_4, num_5, num_6, num_7, num_8, num_9, symbol]

# in: datetime of os
# out: string: "11:33:20"
def sys_time()
    time_now = Time.now.to_s
    time = time_now[11..18]   #get h,m,s 
    return time
end

# in: time string and font
# out: [[],[],[],[],...]
def time_to_font(time,font)
    output = []
    for i in 0...time.length()
        converted_font = convert_1_number_to_1_font(time[i],font)
        output.append(converted_font)
    end
    return output
end

# in: number from os time, font
# out: font for each number
def convert_1_number_to_1_font(number,font)
    if number == "0"
        return font[0]
    end
    if number == "1"
        return font[1]
    end
    if number == "2"
        return font[2]
    end
    if number == "3"
        return font[3]
    end
    if number == "4"
        return font[4]
    end
    if number == "5"
        return font[5]
    end
    if number == "6"
        return font[6]
    end
    if number == "7"
        return font[7]
    end
    if number == "8"
        return font[8]
    end
    if number == "9"
        return font[9]
    end
    if number == ":"
        return font[-1]
    end
end

# in: 1 arr with separated items 
# out: 1 arr with united items
def merge_arr(arr)
    merged_arr = ["","","","","",""]
    for i in 0...arr[0].length() 
        for j in 0...arr.length() 
            font_character = arr [j]
            merged_arr[i] += font_character[i]
        end
    end   
    return merged_arr
end
            
#print that marged_arr
def print_merged_arr(merged_arr)
    puts merged_arr
end

pre_sec=0
while true
    time_str = sys_time()
    if time_str[7..8].to_i != pre_sec
        system("clear")
        puts Time.now
        converted_time = time_to_font(time_str,font)
        merged_array = merge_arr(converted_time)
        print_merged_arr(merged_array)
        pre_sec = time_str[7..8].to_i
    end 
    sleep(0.01)
end
