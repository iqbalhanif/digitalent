'''
namafile: latihanSBA.py
Lembar kerja/script Latihan SBA
'''
# >>>>>>LEMBAR KERJA>>>>>>>>>
# lembar ini hanya berisi pendefinisian fungsi dan class saja

#email netacad, JANGAN SAMPAI LUPA >>>>>>><<<<<<<
email = 'iqbal.hanif.ipb@gmail.com'

#soal 1
class titik2d:  
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def ambiltitik(self):
    z = (self.x, self.y)
    return z

  def tambahkan(self,x,y):
    titik = titik2d(x,y)
    self.x += titik.x
    self.y += titik.y
  pass
    
# soal 2
def run():
  a, b = [int(x) for x in input("Enter two values\n").split(' ')] 
  c = titik2d(a,b)
  return c

# >>>>>>AKHIR LEMBAR KERJA>>>>>>>>>



if __name__ == '__main__':
  # >>>>>TEST DI SINI>>>>>>
  # gunakan BLOCK MAIN ini untuk mengetes

  # untuk pengetesan kode hanya boleh di bagian sini
  # silakan test sesuka hati di sini
  t1 = run()
  print('titik1:',t1.ambiltitik())

  # >>>>>AKHIR TEST DI SINI>>>>>>
