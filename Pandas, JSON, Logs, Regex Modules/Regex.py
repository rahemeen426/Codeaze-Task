import re
#Example 1
pattern = r'hello'
string = 'hello world'

match = re.match(pattern, string)
if match:
    print("Match found!")
#Example 2   
pattern = r'apple'
string = 'I have an apple'

new_string = re.sub(pattern, 'banana', string)
print(new_string)
#Example 3
pattern = r'\d+'  # Match one or more digits
string = 'I have 12 apples and 15 oranges.'

matches = re.findall(pattern, string)
print(matches) 
#Example 4
matches = re.finditer(pattern, string)
for match in matches:
    print("Match:", match.group())
    print("Start:", match.start())
    print("End:", match.end())
