def jewels_count(jewels, stones):
  jewels_sum = 0
  
  for stone in stones:
    if (stone in jewels):
      jewels_sum += 1
      
  return jewels_sum
      
