import os;
import Slicer
from tkinter import Tk, filedialog, StringVar, IntVar, BooleanVar
from tkinter.ttk import Button, LabelFrame, Label, Entry, Frame, Checkbutton
from tkinter.messagebox import showerror

class ImageEditorGUI:
  def __select_files(self):
    self.filenames = filedialog.askopenfilenames(title="Select Images", filetypes=[("Image Files", "*.jpg;*.png")])
    self.file_list.set("\n".join(self.filenames))

  def __submit(self):
    # Add your logic here to process the selected files, width, height, padding and offset values
    print(f"Selected Files: {self.file_list.get()}")
    print(f"Width: {self.width_entry.get()}")
    print(f"Height: {self.height_entry.get()}")
    print(f"Padding: {self.padding_entry.get()}")
    print(f"Offset: {self.offset_entry.get()}")
    print(f"Open: {self.open_folder_var.get()}")

    if not self.filenames:
      showerror("Error", "Please select some files first!")
      return
    
    for filename in self.filenames:
      # Get filename without extension
      file_name, file_type = os.path.splitext(os.path.basename(filename))
      file_path = os.path.dirname(filename)
      print(filename, file_path)
      # Create folder for each file
      folder_path = os.path.join(file_path, file_name)
      try:
        os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist

        patches = Slicer.slice(filename,self.width_entry.get(),self.height_entry.get(),self.padding_entry.get(),self.offset_entry.get())
        for tuple in enumerate(patches):
          print(tuple)
          patch,x,y = tuple[1]
          patch.save(f"{folder_path}\\{file_name}_{x}_{y}.png")

        if(self.open_folder_var.get()):
          os.startfile(folder_path)
        print(f"Created folder: {folder_path}")
      except OSError as e:
        showerror("Error", f"Failed to create folder: {folder_path}\n{e}")


  def __init__(self):
    self.root = Tk()
    self.root.title("Spritesheet Slicer")

    # Frame for file selection
    self.file_frame = LabelFrame(self.root, text="Select Images")
    self.file_frame.pack(padx=10, pady=10)
    self.select_button = Button(self.file_frame, text="Browse", command=self.__select_files)
    self.select_button.pack(side="left")

    self.file_list = StringVar()
    self.file_label = Label(self.file_frame, textvariable=self.file_list)
    self.file_label.pack(side="left", fill="y")

    # Frame for dimensions and padding/offset
    self.settings_frame = LabelFrame(self.root, text="Settings")
    self.settings_frame.pack(padx=10, pady=10)

    self.width_frame = Frame(self.settings_frame)
    self.width_frame.grid(row=0, column=0)
    self.width_label = Label(self.width_frame, text="W:")
    self.width_label.grid(row=0, column=0)
    self.width_entry = IntVar(value=16)
    self.width_entry_field = Entry(self.width_frame, textvariable=self.width_entry, width=8)
    self.width_entry_field.grid(row=0, column=1)
    
    self.height_frame = Frame(self.settings_frame)
    self.height_frame.grid(row=0, column=1)
    self.height_label = Label(self.height_frame, text="H:")
    self.height_label.grid(row=0, column=2)
    self.height_entry = IntVar(value=16)
    self.height_entry_field = Entry(self.height_frame, textvariable=self.height_entry, width=8)
    self.height_entry_field.grid(row=0, column=3)
    
    self.padding_label = Label(self.settings_frame, text="Padding:")
    self.padding_label.grid(row=2, column=0)
    self.padding_entry = IntVar(value=0)
    self.padding_entry_field = Entry(self.settings_frame, textvariable=self.padding_entry, width=8)
    self.padding_entry_field.grid(row=2, column=1)

    self.offset_label = Label(self.settings_frame, text="Offset:")
    self.offset_label.grid(row=3, column=0)
    self.offset_entry = IntVar(value=0)
    self.offset_entry_field = Entry(self.settings_frame, textvariable=self.offset_entry, width=8)
    self.offset_entry_field.grid(row=3, column=1)
    
    self.open_folder_var = BooleanVar(value=True)  # Set default to unchecked
    self.open_folder_checkbox = Checkbutton(self.settings_frame, text="Open Folder", variable=self.open_folder_var)
    self.open_folder_checkbox.grid(row=4, columnspan=2)  # Add checkbox to settings frame

    # Submit button
    self.submit_button = Button(self.root, text="Slice", command=self.__submit)
    self.submit_button.pack(padx=10, pady=10)


    self.root.mainloop()

# Run the GUI
gui = ImageEditorGUI()





# size = input("size")
# path = input("filename")
# padding = 0
# offset = 0

# slice_image(path, size,padding,offset)