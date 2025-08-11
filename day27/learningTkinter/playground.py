import tkinter as tk

# labels
# button
# entry
# text
# spinbox
# scale
# checkbutton
# radiobutton
# listbox



class Car: #can also pass this to object creation 
    def __init__(self, **kw):
        # obviously, this might cause issues, if I give any **kwargs then it might not work
        # in this case we can use dict.get()
        # this is how we can create a class with many optional key word arguments
        self.make = kw.get("make")
        self.model = kw.get("model")

def add(*args):
    total_sum = 0
    for n in args:
        total_sum += n
    return total_sum

# **kwargs creates unlimited key word arguments
# essentially passes a custom made dictionary to the function, mind = blown

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

def button_clicker(label):
    label.config(text="Button was clicked!")

def main() -> int:

    window = tk.Tk()
    window.title("My First GUI Program")
    window.minsize(width=500, height=300)

    my_label = tk.Label(text="I Am a Label", font=("Arial", 24, "bold"))
    my_label.pack() # places an element centerered on the window, doesn't show up otherwise]
    
    # packer takes some arguments to change where the label will be displayed

    # python arguments!! 
    # more importanty ADVANCED PYTHON ARGUMENTS

    # how to allow any number of arguments to be used ? it's essentially va_args & va_list

    # we can also create buttons

    button = tk.Button(text="Click Me!", command=button_clicker, arg=my_label)
    button.pack()

    entry = tk.Entry(width=10, )
    entry.pack()   
    entry.get() 
    print(add(1, 2, 3))
    calculate(2, add=5, multiply=2)
    my_car = Car(make="Nissan", model="GT-R")


    window.mainloop()

    return 0



if __name__ == "__main__":
    main()





