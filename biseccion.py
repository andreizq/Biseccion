import sys

def f(x,a,b,c):
	ax = a*(x**2)
	bx = b*x
	return ax+bx+c

def sameSign(xl,xu,a,b,c):
	fl = f(xl,a,b,c)
	fu = f(xu,a,b,c)
	res = fl*fu > 0
	return res

tolerancia = 0.01

print("Este programa buscará la raiz de un polinomio en segundo grado, dentro del intervalo de x indicado.")
print("El polinomio tendrá la forma ax²+bx+c")
print("Introduce el valor de a")
a = float(input())
print("Introduce el valor de b")
b = float(input())
print("Introduce el valor de c")
c = float(input())
print("Introduce el limite inferior del intervalo")
xl_i = float(input())
print("Introduce el limite inferior del intervalo")
xu_i = float(input())

xl = xl_i
xu = xu_i

if(f(xl,a,b,c)==0):
	print("La raiz es ",xl)
	sys.exit()

if(f(xu,a,b,c)==0):
	print("La raiz es ",xu)
	sys.exit()

m = (xu+xl)/2

if sameSign(xl,m,a,b,c):
	xl = m
else:
	xu = m

while(abs(xl-xu)>tolerancia):
	m = (xu+xl)/2
	if sameSign(xl,m,a,b,c):
		xl = m
	else:
		xu = m

if(xu==xu_i or xl==xl_i):
	print("No hay raices en el intervalo")
else:
	print("la raiz se encuentra entre ",xl," y ",xu)