rate = input("оцените работу оператора от 1 до 5: ") # str
rate_us_number = int(rate) # int

if(rate_us_number < 1):
    rate_us_number = 1

if(rate_us_number > 5):
    rate_us_number = 5

print(rate_us_number)


feedback = ''

if rate_us_number == 1:
    feedback = input("расскажите, что нам улучшить: ")
elif rate_us_number == 2:
    feedback = input("расскажите, что вас смутило: ")
elif rate_us_number == 3:
    feedback = input("расскажите, как нам стать лучше: ")
elif rate_us_number == 4:
    feedback = input("расскажите, почему не 5?: ")
else:
    feedback = input("расскажите, за что похвалить оператора: ")
print(feedback)