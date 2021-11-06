from typing import final


current_time_str = input("What is the current time (in hours 0 - 23)? ")
wait_time_str = input("How man hours do you want to wait? ")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

print(current_time_str)
print(wait_time_str)

final_time_int = current_time_int + wait_time_int
final_time = final_time_int % 24

print("The time after waiting is:", final_time)
