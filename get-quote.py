import random

def primary():
#   print("Keep it logically awesome.")

  quotes = ["Hello World!", "I walk the line.", "Nawdang", "Do the next thing"]

  f = open("quotes.txt", 'r+')
  for quote in quotes:
    f.write(quote + "\n")
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
