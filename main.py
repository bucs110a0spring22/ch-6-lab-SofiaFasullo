
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        #print(n)
        count += 1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    #print(n)                  # the last print is 1
    #print(count)
    return(count)
    

def main():
  upper_bound = int(input("input an upper range value:"))
  if upper_bound > 0:
    for i in range(1,upper_bound+1):
      print(i)
      count = seq3np1(i)
      print(count)
  else:
    print("You must input a postive number")
    return()


import turtle
grapher = turtle.Turtle()
wn = turtle.Screen()

def main2():
  upper_bound = int(input("input an upper range value:"))
  list = []
  if upper_bound > 0:
    for i in range(1,upper_bound+1):
      #print(i)
      count = seq3np1(i)
      #print(count)
      list.append(count)
  else:
    print("You must input a postive number")
    return()
  max_seq3np1 = max(list)
  print(max_seq3np1)
  wn.setworldcoordinates(-1,-1,upper_bound+2,max_seq3np1+2)
  grapher.down()
  grapher.down()
  grapher.goto(0,max_seq3np1+2)
  grapher.up()
  grapher.goto(0,0)
  grapher.down()
  grapher.goto(upper_bound+2, 0)
  grapher.up()
  grapher.goto(0,0)
  grapher.down()
  grapher.color("green")
  for i in range(1,upper_bound+1):
    grapher.goto(i,seq3np1(i))

main2()
wn.exitonclick()

main2()