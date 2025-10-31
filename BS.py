def fib(n):
  a,b=0,1
  if n<=1:
    return n
  else:
    for i in range(n):
      a,b=b,a+b
    yield b
print(fib(45))
