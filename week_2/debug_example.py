current_time_str = input("what is the current time (in hours 0-23)?")
wait_time_str = input("how many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_str + wait_time_str

final_answer = final_time_int % 24

print("The time after waiting is:", final_answer)
