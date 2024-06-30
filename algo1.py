# Sonu 0 ilə bitən bütün 3 rəqəmli ədədləri ekrana çıxaran proqram yazın. 
# Display all 3-digit numbers ending with 0 write a program that outputs.
import math
for i in range(100,1000):
    num=str(i)
    if num[-1:]=='0' :
        print(num)