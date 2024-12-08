def find_difference_hcf(values: tuple[int, int]):
   x, y = values
   while(y):
       x, y = y, x % y
   return x

print(find_difference_hcf((0, 0)))