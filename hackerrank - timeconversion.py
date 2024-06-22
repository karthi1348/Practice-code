normal="07:05:45PM"
hours=normal[0:2]
minutes=normal[3:5]
seconds=normal[6:8]
mode=normal[8:10]

if mode=="PM":
   if int(hours)<12:
      railwaytime=str(int(hours)+12)
      normal=normal.replace(hours,railwaytime)
if mode=="AM":
   if int(hours)==12:
      railwaytime="00"
      normal=normal.replace(hours,railwaytime)
newnormal=normal[:8]
print(newnormal)



