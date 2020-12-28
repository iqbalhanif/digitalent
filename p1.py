# nama file p1.py 
# Isikan nama anda dan copy semua cell code yang dengan komentar #Graded
 
#netacad email cth: 'abcd@gmail.com'
email='iqbal.hanif.ipb@gmail.com'
priority=1
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

#Graded

# MULAI KODEMU DI SINI
def letter_catalog(items,letter='A'):
  x = []
  for i in range(0,len(items)):
    if letter == items[i][0]:
      x.append(items[i])     
  return x
  pass 

#Graded

# MULAI KODEMU DI SINI
def counter_item(items):
  x = list(set(items))
  y = []
  z = {}
  for i in range(0, len(x)):
    y.append(items.count(x[i]))
  for i in range(0, len(x)):
    z.update({x[i]:y[i]}) 
  return z
  pass 

#Graded

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# MULAI KODEMU DI SINI
fruit_price = dict(zip(fruits, prices))

def total_price(dcounter,fprice):
  x = 0
  for key in dcounter:
    x += dcounter[key] * fprice[key]
  return x
  pass

#Graded

# MULAI KODEMU DI SINI
def discounted_price(total,discount,minprice=100):
  if total >= minprice:
    x = total - total * discount / 100
  else:
    x = total
  return x 
  pass

#Graded

# MULAI KODEMU DI SINI
def print_summary(items,fprice):
  a =[]
  b =[]
  z = counter_item(items)
  x = sorted(list(z.keys())) 
  y = [z[key] for key in sorted(z)]
  w = [fprice[key] for key in sorted(z)]
  for i in range(0,len(z)):
    d = int(y[i]) * int(w[i])
    b.append(d)
  for i in range(0, len(z)):
    c =  str(y[i]) + ' ' + str(x[i])+ ' ' + ':' + ' ' + str(b[i]) 
    a.append(c)
  p = 'total : ' + str(total_price(counter_item(items),fprice)) 
  q = 'discount price : ' + str(discounted_price(total_price(counter_item(items),fprice),10,minprice=100)) 
  a.append(p)
  a.append(q)
  for i in a:
    print(i)
  pass