# Writing your own functions

def header(text, surround):
    length = len(text)+4
    print(surround * length)
    print(surround, text, surround)
    print(surround * length)

def main():
    header("Hello, World!", "*")
    header("Python Rocks!", "!")
    header("Coders 4 EVER", "+")

main()