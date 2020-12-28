# nama file p3.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 2

#netacad email cth: 'abcd@gmail.com'
email='iqbal.hanif.ipb@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini
def caesar_encript(txt,shift):
  b = ''
  c = shift % 26
  for i in range (0, len(txt)):
    if txt[i].isalpha() == True: 
      if txt[i].islower() == False:
        x = ord(txt[i].lower())
        if x + c > 122:
          y = 96 + (x + c - 122)
        elif x + c < 97:
          y = 123 + (c + (x - 97))   
        else:
          y = x + c
        z = chr(y).upper()
      else:
        x = ord(txt[i])
        if x + c > 122:
          y = 96 + (x + c - 122) 
        elif x + c < 97:
          y = 123 + (c + (x - 97))   
        else:
          y = x + c
        z = chr(y)
    else:
      z = txt[i]
    b = b + z 
  
  return(b)
  pass

# Fungsi Decript caesar
def caesar_decript(chiper,shift):
  b = ''
  c = shift % 26
  for i in range (0, len(chiper)):
    if chiper[i].isalpha() == True: 
      if chiper[i].islower() == False:
        x = ord(chiper[i].lower())
        if x - c < 97:
          y = 122 - (c - (x - 96)) 
        elif x - c > 122:
          y = 96 - (c + (122 - x)) 
        else:
          y = x - c
        z = chr(y).upper()
      else:
        x = ord(chiper[i])
        if x - c < 97:
          y = 122 - (c - (x - 96))
        elif x - c > 122:
          y = 96 - (c + (122 - x))  
        else:
          y = x - c
        z = chr(y)
    else:
      z = chiper[i]
    b = b + z 
  
  return(b)
  pass
    
  #return caesar_encript(chiper,-shift)



# Fungsi mengacak urutan
def shuffle_order(txt,order):
  return ''.join([txt[i] for i in order])
 
# Fungsi untuk mengurutkan kembali sesuai order
def deshuffle_order(sftxt,order):
  a = [0] * len(sftxt)
  for i in range(0,len(sftxt)):
    x = order[i]
    a[x] = sftxt[i]
  a = ''.join(a)
  return a 
  pass
  
 
import math
# convert txt ke dalam bentuk list teks yang lebih pendek
# dan terenkrispi dengan urutan acak setiap batchnya
def send_batch(txt,batch_order,shift=3):
  # Mulai Kode anda di sini
  enc = caesar_encript(txt, shift)
  if (((math.ceil(len(enc) / len(batch_order))) * len(batch_order)) - (len(enc))) !=0:
    a = "_" * (((math.ceil(len(enc) / len(batch_order))) * len(batch_order)) - (len(enc)))
    b = enc + a 
  else:
    b = enc
  x = [b[i:i+len(batch_order)] for i in range(0, len(enc), len(batch_order))]
  y = [0] * math.ceil((len(b) / len(batch_order))) 
  for i in range(0,len(x)):
    y[i] = shuffle_order(x[i],batch_order)  
  return y 
  pass
# batch_cpr: list keluaran send_batch
# fungsi ini akan mengembalikan lagi ke txt semula
def receive_batch(batch_cpr,batch_order,shift=3):
  batch_txt = [caesar_decript(deshuffle_order(i,batch_order),shift) for i in batch_cpr]
  return ''.join(batch_txt).strip('_')