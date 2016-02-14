# A simple python program to spread love
import pylab as pl
import scipy as sp

x = sp.linspace(-2,2,1000)
y1 = sp.sqrt(1-(abs(x)-1)**2)
y2 = -3.5*sp.sqrt(1-(abs(x)/2)**0.5)
pl.fill_between(x, y1, color='red')
pl.fill_between(x, y2, color='red')
pl.xlim([-2.5, 2.5])
pl.text(0, -1.0, 'Happy Valentines Day\n #pyLove', fontsize=20, fontweight='bold',
           color='white', ha='center')
pl.savefig('pylove.png')
pl.show()

