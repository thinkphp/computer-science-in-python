# func = decorator
def make_bold( func ):
     def deco():
         return "<b>" + func() + "</b>"
     return deco

# func = main
def make_italic( func ):
     def decorator_italic():
         return "<i>" + func() + "</i>"
         #              "hello, universe!"
     return decorator_italic
     # "<i>hello, universe!</i>"

# func = deco
def make_blue(func):
     def decorator_blue():
         return "<blue>" + func() + "</blue>"
     return decorator_blue

# func = decorator_blue
def transform(func):
     def decorator():
         return "<transform>" + func() + "</transform>"
     return decorator

def make_HTML( fn ):
    def decorator_html():
        return "<html>" + fn() + "</html>"
    return decorator_html

@make_HTML   #5 <html><transform><blue><b><i>Hello, Universe!</i></b></blue></transform></html>
@transform   #4 <transform><blue><b><i>Hello, Universe!</i></b></blue></transform>
@make_blue   #3 <blue><b><i>Hello, Universe!</i></b></blue>
@make_bold   #2 /\<b><i>Hello, Universe!</i></b>
@make_italic #1 ||<i>Hello, Universe!</i>
def main():
    return"Hello, Universe!"
# main = "<html><transform><blue><b><i>Hello, Universe!</i></b></blue></transform></html>

f = open("website.html","w")
print( main() ) # <function make_HTML.<locals>.decorator_html at 0x7f4023d6a9e0>
f.write(main())
#functia main este transmisa la linia 6 si func = main
