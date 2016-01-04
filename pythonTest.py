import time
import eu.mihosoft.vrl.v3d.Cube as Cube

for i in range(100):
  print i
  
result = Cube(20).toCSG()

print "Result = ",result

