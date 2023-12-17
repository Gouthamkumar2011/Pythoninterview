# def square(x):
#     return x*x

# d = square

# #Assigned a function to a variable

# # print(square)
# # print(d(6))


# #MAP Function

# def map_function(func,arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result



# def cube(x):
#     return x*x*x

# squares = map_function(square, [1,2,3,4,5])
# squares_1 = map_function(cube, [1,2,3,4,5])
# print(squares)
# print(squares_1)

# def logger(msg):
#     def log():
#         print("log:",msg)
    
#     return log


# log_hi = logger("hi")
# log_hi()


# def html_tag(tag):
#     def wrap_text(msg):
#         print('<{0}>{1}<{0}>'.format(tag,msg))
#     return wrap_text

# print_h1 = html_tag("h1")
# print_h1("test Headline")
# print_h1("Another Headline")

# print_p = html_tag('p')
# print_p("Test_Paragraph")



# def outer_func(msg):
#     message = msg

#     def inner_func():
#         print(message)

#     return inner_func()


# outer_func("Goutham is gonna get a BMW M5CS")


# def decorator_function(og_function):
#     def wrapper_func():
#         return og_function()
#     return wrapper_func

# def display():
#     print("Goutham is gonna get a BMW M5CS")

# decorated_display = decorator_function(display)
# decorated_display()

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()