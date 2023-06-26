name = 'Al'
age = 4000
'Hello, my name is ' + name + '. I am ' + str(age) + ' years old.'

# string interpolation 1
name = 'Al'
age = 4000
'My name is %s. I am %s years old.' % (name, age)

# string interpolation 2
name = 'Al'
age = 4000
f'My name is {name}. Next year I will be {age + 1}.'