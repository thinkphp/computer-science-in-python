#How to create a simple website from Decorator Python

def make_html( fn ):
    def decorator_html():
        return "<!DOCTYPE html><html>" + fn() + "</html>"
    return decorator_html    

def make_list( fn ):
    def decorator_list():
        return fn() + "<ol><li>C</li><li>C++</li><li>JAVA</li><li>Python</li></ol>"
    return decorator_list

def make_span( fn ):
    def decorator_span():
        return "<span style='color:green;font-size: 30px'>" + fn() + "</span>"
    return decorator_span

def make_center( fn ):
    def decorator_center():
        return "<center>" + fn() + "</center>"
    return decorator_center

def make_bold( fn ):
    def decorator_bold():
        return "<b>" + fn() + "</b>"
    return decorator_bold

@make_html
@make_list
@make_span
@make_bold
@make_center
def main():
    return "Hello, Universe!"

f = open("Andrei.html","w")
# "w" va suprascrie peste orice continut existent
#f = open("Andrei.html","a")
# "a" = append -> va adauga continutul la sfarsitul fisierului
f.write( main() )
