f = open('foo.txt', 'rt')     # Open for reading (text)
g = open('bar.txt', 'wt')     # Open for writing (text)

data = f.read()               # Read all of the data
data = f.read([maxbytes])     # Read only up to 'maxbytes' bytes

f.close()                     # Close file


# Reading a file
with open(filename, 'rt') as file:
    # Read entire file into string
    data = file.read()
    
    # Process each line
    for line in file:
        
    # No need to close explicitly

# Writing to a file
with open('outfile', 'wt') as out:
    out.write('Hello World\n')      # Write string data
    print('Hello World', file=out)  # Redirect the print function

    
import csv
f = open('Data/prices.csv', 'r')
rows = csv.reader(f)

for row in rows:
  print(row)
