print("input cost and selling price respectively")
c=int(input())
s=int(input())
if s>c:
    profit=s-c
    print("profit is",profit)
elif s<c:
    loss=c-s
    print("loss is",loss)
else:
    print("no profit and no loss")
