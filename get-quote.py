import random
def primary():
  # print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  for i in range(2):
   rnd = random.randint(0,last)
   print(quotes[rnd],end="")

if __name__== "__main__":
  primary()
