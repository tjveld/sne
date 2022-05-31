# TUPLES
## A tuple is a collection of values grouped together. A single item consisting of multiple parts. 
s = ('GOOG', 100, 490.1)
t = ()            # An empty tuple
w = ('GOOG', )    # A 1-item tuple

## Tuple contents are ordered (like an array).
name = s[0]                 # 'GOOG'
shares = s[1]               # 100
price = s[2]                # 490.1

## Make a new tuple based on a current tuple.
s = (s[0], 75, s[2])

## You can unpack its parts into variables.
name, shares, price = s

# LIST
## Lists are usually a collection of distinct items, usually all of the same data type
symbols = [ 'GOOG', 'AAPL', 'IBM' ]


#DICTIONARIES
s = {
    'name': 'GOOG',
    'shares': 100,
    'price': 490.1
}

## To get values from a dictionary use the key names.

print(s['name'], s['shares'])
s['price']
