
chik_leg = 2
pig_leg = 4
cow_leg = 4


chik = int(input("Сколько кур? "))


all_chik_leg = chik_leg*chik
print("Всего ног куриных ног ", all_chik_leg)



pig = int(input("Сколько  свиней? "))

all_pig_leg = pig_leg*pig
print("Всего ног свинных ног ", all_pig_leg)



cow = int(input("Сколько  коров? "))

all_cow_leg = cow_leg*cow
print("Всего ног коровьих ног ", all_cow_leg)


all_leg = all_chik_leg + all_pig_leg + all_cow_leg

print("Всего ног ", all_leg)