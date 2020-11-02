from scipy import spatial
import statistics
import math

# Change here: User Profile
u1 = [3,5,1,2,4,3]
u2 = [1,0,5,0,4,0]
u3 = [3,5,1,2,3,3,5,4]

# Don't touch
# Start
def pearson_data_pre(data):
  total = 0
  for i in range(len(data)):
    if (data[i] != 0 ):
      total += 1

  data_s = sum(data)
  data_mean = data_s/ total


  new_data = []
  for i in range(len(data)):
    if (data[i] != 0 ):
      new_data.append(data[i]-data_mean)
    else:
      new_data.append(0)
  return data_mean,new_data
# End 

# Update variables here
da_mean,new_da = pearson_data_pre(u3)


print("Value to normalize with")
print(da_mean)

print("Data after normalization")
print(new_da)







