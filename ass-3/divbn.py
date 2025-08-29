print("numbers divisible by the sum of their digits (1 to 10000):")
for num in range(1,10000):
    dsum = sum(int(d) for d in str(num))
    if dsum != 0 and num % dsum ==0 :
        print(num , end=' ')