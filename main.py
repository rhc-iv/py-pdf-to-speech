# Import statements:
import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import filedialog

# Create a GUI for the application:
root = tk.Tk()
root.configure(
    bg='#3E4451',
)
root.geometry('800x600')
root.title('PDF-To-Speech')

# Construct a grid for the Tkinter GUI:
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


# Create a function to open a PDF file and convert it into speech:
def open_pdf():

    # Open a file dialog to select a PDF file:
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    # Create a PDF reader object:
    pdf_reader = PyPDF2.PdfReader(file_path)

    # Create a text variable to store the text from the PDF:
    text = ""

    # Loop through each page of the PDF:
    for page in range(len(pdf_reader.pages)):

        # Extract the text from the page and add it to the text variable:
        text += pdf_reader.pages[0].extract_text()

    # Create a text-to-speech engine object:
    engine = pyttsx3.init()

    # Set the rate of speech:
    engine.setProperty("rate", 150)

    # Deliver the text as speech:
    engine.say(text)
    engine.runAndWait()


# Create a label for the application:
app_label = tk.Label(
    root,
    bg='#3E4451',
    fg='#D19A66',
    font=(
        'SF Pro Display',
        32,
        'bold',
    ),
    padx=10,
    pady=10,
    text='PDF-To-Speech Application',
)
app_label.grid(
    column=0,
    columnspan=2,
    row=0,
    pady=15,
)

# Create a button to open a PDF file:
open_button = tk.Button(
    root,
    bg='#98C379',
    borderwidth=1.0,
    command=open_pdf,
    fg='#565C64',
    font=(
        'SF Pro Display',
        18,
        'normal',
    ),
    justify='center',
    padx=10,
    pady=10,
    relief='groove',
    text="Open PDF",
)
open_button.grid(
    column=0,
    row=3,
    pady=15,
)

# Run the Tkinter event loop:
root.mainloop()