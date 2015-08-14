import time
import eu.mihosoft.vrl.v3d.Cube as Cube

for i in range(10):
  print time.time()*1000.0
  
result = Cube(20).toCSG()

print "Result = ",result

