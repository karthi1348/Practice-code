arr=[1,1,0,-1,-1]
positive=sum(1 for element in arr if element >0)/len(arr)
negative= sum(1 for element in arr if element<0)/len(arr)
zero= sum(1 for element in arr if element == 0)/len(arr)
print("%.6f" %positive)
print("%.6f" %negative)
print("%.6f" %zero)