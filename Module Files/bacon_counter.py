# Import mrjob library
from mrjob.job import MRJob
# Create a class called Bacon_count, which inherits, or takes properties, from the MRJob class
class Bacon_count(MRJob):
   # Next, create a mapper()function that will take (self, _, line) as parameters
   def mapper(self, _, line):
       # function will loop through each word in the line of text
       for word in line.split():
           if word.lower() == "bacon":
               yield "bacon", 1
   #reducer function
   def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   Bacon_count.run()
# Run the following code in the terminal: $ python bacon_counter.py input.txt