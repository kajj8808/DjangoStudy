def plus(a , b):
  return a + b

#종종 파이썬에서 함수에 무제한으로 arguments 를 넣고싶을때.
#첫번째 방법은 *args 를 써놓는것.
# 이렇게하면 tuple 로 return 
def plus_args(a , b , *args):
  print(args)
  return a + b

#무한정으로 keyword argument 를 사용하고싶을때면. ** 은 꼭붙혀야함.
def plus_args_infinity(a , b , *args , **kwargs):
  print(args)
  print(kwargs)
  return a + b
#positional argument => (1 ,2,3,4,5,6,7,8,9)  keyword argument => {'gus'=True}

#숫자를 전부 받아서 더해주는 함수. ex) (1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10)
def infinity_plus_cal(*args):
  result = 0
  for number in args:
    result += number
  print(result) 
