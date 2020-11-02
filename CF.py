from scipy import spatial
import statistics
import math

"""
u-u
data format:
user: [item1, item2, .., itemn]

i-i
data format:
item: [u1,u2,...un]
"""

# Row for others to compare against
da = [1, 0, 3, 0, 0, 5, 0, 0, 5, 0 ,4 ,0]
d1 = [1,0,5,0,4,0]
d2 = [0,0,0,5,4,0]
d6 = [0,0,2,0,2,4]
d7 = [0,0,1,2,0,0]

# Change here
# Other data row
db = [0, 0, 5, 4, 0, 0, 4, 0, 0, 2, 1, 3]
dc = [2,4,0,1,2,0,3,0,4,3,5,0]

# Page 33
u1 = [4,0,0,5,1,0,0]
u2 = [5,5,4,0,0,0,0]

# Page 32
t1 =[4,0,0,5,1,0,0]
t2=[5,5,4,0,0,0,0]

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

# Normal Cosine similarity
# cos = 1- spatial.distance.cosine(t1,t2)
# print(cos)

# Update variables here
da_mean,new_da = pearson_data_pre(d1)
db_mean,new_db = pearson_data_pre(d7)


# Pearson similarity
# sim(da,db)
p_cos = 1- spatial.distance.cosine(new_da,new_db)

print ("New units")
print(new_da)
print(new_db)
print("sim")
print(p_cos)






