t = 0

while t==0:
  print("оберіть дію \n1 - перше завдання \n"
        "2 - друге завдання \nбудь-якa "
        "інша цифра - вихід з програми")

  num = input()
  if int(num) == 1:
    print("введіть число")
    a = float(input())
    print(a)
    print("поділ на дійсну і дробову частину")
    print(str(int(a)) + "____________________" + str(round(a - int(a),2)))
    t=0
  elif int(num)==2:
    print("введіть цілу частину числа")
    b = str(input())
    print("введіть дробову частину числа")
    c = str(input())
    print("ви склали число")
    qqq = str(b) + "." + str(c)
    print(float(qqq))
    t=0
  else:
    t=1
    print("програму завершенно")
    break