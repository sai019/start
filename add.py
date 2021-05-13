def calculate_sum(h):
     total = 0
     for i in h:
          total = total + i
     return total
lis = [745,34,64,343,2,545,56,63,10]
ep = [50,60,70,80]
total_lis = calculate_sum(lis)
total_ep = calculate_sum(ep)
print(total_lis)
print(total_ep)

#### program with forloop and functions