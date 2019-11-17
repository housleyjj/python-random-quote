import random

def primary():
#   print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = random.randint(0, last)
  print(quotes[rnd].rstrip('\n'))
  if rnd == 0:
    print(quotes[rnd+1].rstrip('\n'))
  else:
    print(quotes[rnd-1].rstrip('\n'))

if __name__== "__main__":
  primary()
