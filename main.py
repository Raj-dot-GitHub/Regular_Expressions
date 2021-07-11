
### General Introduction:
import re

test_string = '123 abc456789 abc123'

pattern = re.compile(r"\B123")  # 'r' = raw string

## Finditer Method:
#---------------------
matches = pattern.finditer(test_string)   # finditer method

matches = re.finditer(r"abc", test_string)

for match in matches:
    print(match)

## Uses of raw string
#-----------------------
a = "\tHello World"   # Without raw string
print(a)

b = r"\tHello World"   # With raw string
print(b)

## Findall Method:
#-----------------------
matches = pattern.findall(test_string)

for match in matches:
    print(match)


## Match Method:
#------------------------
match = pattern.match(test_string)
print(match)


## Search Method:
# --------------------------
match = pattern.search(test_string)
print(match)


## Group, Start, End, Span Methods:
# ----------------------------------
matches = pattern.finditer(test_string)
for match in matches:
    print(match.span(), match.start(), match.end())
    print(match)


## Set [ ]
# -----------------------------
test_string = 'Raj_sinha_abc123456'
pattern = re.compile(r'[a-zA-Z0-9_]')
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

# Eg.
test_string = 'hello_1233'
pattern = re.compile(r"_?\d{1,4}")
matches = pattern.finditer(test_string)
for match in matches:
    print(match)

# Eg.
dates = """
2020-08-26
2001-07-21
2001/06/12
2003_03_24"""
pattern = re.compile(r"\d{4}.0[4-7].\d{2}")
matches = pattern.finditer(dates)
for match in matches:
    print(match)

# Eg.
my_string = """
hello world
123245
Mr Raj Sinha
Mrs. Sinha
Ms Sneha Raut
Mr. Smith Ignease
"""
pattern = re.compile(r"(Mr|Ms|Mrs)\.?\s\w+\s\w+")
matches = pattern.finditer(my_string)
for match in matches:
    print(match)


# Eg.
emails = """
raj Sinha
2115219
1234
raj.sinha@somaiya.edu
raj28560964@gmail.com
rajaccess2@gmail.com
raj.sinha@yahoo.in"""

patterns = re.compile(r"([a-zA-Z0-9\.]+)@([a-zA-Z]+)\.([a-zA-Z]+)")
matches = patterns.finditer(emails)
for match in matches:
    print(match.group(1))


## Split & Sub method.
# --------------------------------
test_string = '123abc456789abc123ABC'
patterns = re.compile(r"abc")
matches = patterns.split(test_string)
print(matches)

test_string = "Hello world, you are the best world"
pattern = re.compile(r"world", re.IGNORECASE)    # Compilation flag.
subbed_string = pattern.sub("planet", test_string)
print(subbed_string)
