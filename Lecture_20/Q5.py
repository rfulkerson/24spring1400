def song_length(sec, mins):
    calc = mins * 60 + sec
    return calc
    
m = int(input("Min: "))
s = int(input("Sec: "))

r = song_length(mins=m,sec=s)
print(f"Length: {r}")

# print("minutes is:", m, end= '......')
# print("second is:", s)
