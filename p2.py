# nama file p2.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0

#netacad email cth: 'abcd@gmail.com'
email='iqbal.hanif.ipb@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini



#Graded
# MULAI KODEMU DI SINI
def isPointInCircle(x,y,r,center=(0,0)):
  if (x - center[0])**2 + (y - center[1])**2 <= r**2:
    return True
  else:
    return False
  pass
  

  
#Graded
import random

def generateRandomSquarePoints(n,length,center=(0,0)):
  # MULAI KODEMU DI SINI
  minx = center[0]-length/2
  miny = center[1]-length/2
  maxx = center[0]+length/2
  maxy = center[1]+length/2
  
  # Gunakan list comprehension dengan variable minx, miny, length, dan n
  points = []
  for i in range(0, n):
    x = random.uniform(minx, maxx)
    y = random.uniform(miny, maxy)
    z = [x,y]
    points.append(z)
  return points

  

#Graded

def MCCircleArea(r,n=100,center=(0,0)):
  # MULAI KODEMU DI SINI
  x = generateRandomSquarePoints(n,r*2,center)
  y = 0
  for i in x:
    if isPointInCircle(i[0],i[1],r,center) == True:
      y = y +1
    else:
      continue
  z = y/n * (r*2)**2
  return z

  pass
  
  
  
#Graded

def LLNPiMC(nsim,nsample):
  # MULAI KODEMU DI SINI
  x = 0
  for i in range (0, nsim):
    x = x + MCCircleArea(1,nsample)
  p = x / nsim 
  return p
  pass
  
  
  
# Graded
def relativeError(act,est):
  
  # MULAI KODEMU DI SINI
  e = abs((est-act)/act) * 100
  return e
  pass