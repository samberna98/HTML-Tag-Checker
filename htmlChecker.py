#  File: htmlChecker.py
#  Description: program that read html wilfe and extracts and checks to make sure all the tags are matched up
#  Date Created: 10-10-17
#  Date Last Modified:10-13-17

class Stack (object): # Stack class implementation
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def push (self, item):
      self.items.append (item)

   def pop (self):
      return self.items.pop ()

   def peek (self):
      return self.items [len(self.items)-1]

   def size (self):
      return len(self.items)

   def __str__ (self):
      return str(self.items)

def getTag(inp): # method that extraccts tags

   tag = ""
   index = 0
   while index < len(inp):
      if inp[index] == "<":
         inp.remove(inp[index])
         while inp[index] != ">" and  inp[index] != " ":
            tag += inp[index]
            index += 1
         return tag
      else:
         inp.remove(inp[index])
   

      
 

def main():
    
   myfile = open ('htmlfile.txt')
   inp = myfile.read()
   myfile.close()
    
   chars = []
   for i in inp:
      chars.append(i)

   exceptions = ["br", "meta","hr"]
   validtags = [  ]
   x = 0
   tags = Stack()
   taglist = []
   while x < len(chars):
      taglist.append(getTag(chars))
      x+=1

   print(taglist)
   
   for i in taglist:
      if i[0] != "/":
         tags.push(i)
         for y in exceptions:
            if i == y:
               print("Tag", i , "does not need to match: stack is still", tags)
               tags.pop()
               break
         for z in validtags:
            if i != z:
               validtags.append(i)
               break
         
         print("Tag",i,"pushed: stack is now", tags)
      elif i[0] == "/" and i[1:] == tags.peek():
         tags.pop()
         print("Tag", i, "matches top of stack: stack is now", tags)
      elif i[0] == "/" and i[1:] != tags.peek():
         for j in exceptions:
            if i[1:] == j:
               print("Tag", i[1:], "does not need to match: stack is is still", tags)
               tags.pop()
               break
            else:
               print("Error: tag is", i,"but top of stack is", tags.peek())
               break
      else:
         y+=1
   print("Processing complete. No mismatches found.")
   print("Exceptions:",exceptions)
   print("Validtags:", validtags)
    

main()
    
