def make_bold(f):
    def bold_wrapper():
        return "<b>" + f() +"</b>"
    return bold_wrapper
 
def make_italic(f):
    def italic_wrapper():
        return "<i>" + f() + "</i>" 
    return italic_wrapper
 
@make_bold
@make_italic
def hello():
    return "Hello, Python!"
 
def main():
    print(hello())
main()
