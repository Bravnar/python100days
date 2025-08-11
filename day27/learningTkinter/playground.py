import tkinter as tk

# The simplest way to create a tkinter window

def add(*args):
        total_sum = 0
        for n in args:
            total_sum += n
        return total_sum

def main() -> int:

    window = tk.Tk()
    window.title("My First GUI Program")
    window.minsize(width=500, height=300)

    my_label = tk.Label(text="I Am a Label", font=("Arial", 24, "bold"))
    my_label.pack(expand=True) # places an element centerered on the window, doesn't show up otherwise
    # packer takes some arguments to change where the label will be displayed

    # python arguments!! 
    # more importanty ADVANCED PYTHON ARGUMENTS

    # how to allow any number of arguments to be used ? it's essentially va_args & va_list
    
    print(add(1, 2, 3))



    window.mainloop()

    return 0



if __name__ == "__main__":
    main()





