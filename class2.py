## strings
name = "Diego M"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "Diego"
last_name = "Moreno"

full_name = first_name+" "+last_name
age = 32
print("This is the full name",full_name)
print("{} {} {}".format(first_name,last_name,age))
print(f"{last_name} {first_name}")
print("%s %s" % (last_name,first_name)) # old mode

## Tab and new line
print('Lenguajes \n\tPython \n\tJavascript \n\tc++')

long_string = """ sfg gadfgaf asdgsdg asdgsag "asdgasdgasdg"
asdgasdgasdgas asdsdsvadf df df afasd  agsgwesbvcvd'ffffff' """
print(long_string)

favorite_language = "    Python "
print(favorite_language.lstrip()) 
print(favorite_language.rstrip())
print(favorite_language.strip()) 

name = input('Enter you name : ')
print("hello ",name)

## Conditionals if ... else
number = -1
if number>2:
    print("Number bigger than 2")
elif number<2 and number>0:
    print("Number smaller than 0")
else:
    print("Number negative")

msg = "Greather than 2" if number > 2 else "smaller than 2"
print(msg)