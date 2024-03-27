m = float(input('Digite um valor em metros: '))

dm = m * 10
cm = m * 100
mm = m * 1000
dam = m / 10
hm = m /100
km = m / 1000


print(f'Lendo {m:.2f}m temos:'
      f' {mm:.2f}mm;'
      f' {cm:.2f}cm.'
      f' {dm:.2f}dm;'
      f' {dam:.2f}dam;'
      f' {hm:.2f}hm;'
      f' {km:.2f}km.')