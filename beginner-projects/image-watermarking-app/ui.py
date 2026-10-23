from tkinter import *
from tkinter import filedialog
from tkinter import Scale
from tkinter import ttk
from PIL import Image, ImageTk,ImageDraw,ImageFont

BG =  "#0F172A"
PANEL =	"#1E293B"
ACCENT = "#2DD4BF"
BUTTON_HOVER = "#14B8A6"
WHITE_TEXT = "#F8FAFC"
TITLE_FONT = ("Bahnschrift", 28, "bold")
HEADING_FONT = ("Bahnschrift", 16, "bold")
LABEL_FONT = ("Bahnschrift", 11)
BUTTON_FONT = ("Bahnschrift", 11, "bold")

class UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Image Watermark Tool")
        self.window.state('zoomed')
        self.window.config(bg=BG)
        self.image = None
        self.tk_image = None
        self.image_path = None
        self.image_label = None
        self.original_image = None


        self.main_frame = Frame(self.window, bg=BG)
        self.main_frame.pack(fill="both", expand=True)

        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

        self.header = Frame(self.main_frame, bg=BG,height=90)
        self.header.grid(row=0, column=0,padx=(0,20),sticky="ew")
        self.header.grid_propagate(False)

        self.header_label = Label(self.header,text="🖼 Image Watermark Tool",bg=BG,fg=WHITE_TEXT,font=TITLE_FONT)
        self.header_label.pack(expand=True)

        self.content_frame = Frame(self.main_frame, bg=BG)
        self.content_frame.grid(row=1, column=0,padx=30,pady=(0,30),sticky="nsew")
        self.main_frame.rowconfigure(1, weight=1)

        self.preview_panel = Frame(self.content_frame, bg=PANEL,height=650,bd=1,relief="solid")
        self.preview_panel.grid(row=0, column=0,padx=(0,20),sticky="nsew")
        self.preview_panel.grid_propagate(False)


        self.content_frame.columnconfigure(0, weight=3)
        self.content_frame.columnconfigure(1, weight=1)
        self.content_frame.rowconfigure(0, weight=1)
        self.content_frame.columnconfigure(0, weight=4)
        self.content_frame.columnconfigure(1, weight=2)

        self.preview_header = Frame(self.preview_panel,bg="#162032",height=55)
        self.preview_header.pack(fill="x")
        self.preview_header.pack_propagate(False)

        self.preview_header_label = Label(self.preview_header,text="🖼  Preview",bg="#162032",fg=WHITE_TEXT,font=HEADING_FONT)
        self.preview_header_label.pack(side="left",padx=20)

        self.preview_area = Frame(self.preview_panel,bg="#293548")
        self.preview_area.pack(fill="both",expand=True,padx=20,pady=20,)

        self.placeholder = Label(self.preview_area,text="Click 'Upload Image' to begin",bg="#293548",fg="#A1A1AA",font=("Bahnschrift", 14))
        self.placeholder.place(relx=0.5,rely=0.5,anchor="center")

        self.control_panel = Frame(self.content_frame, bg=PANEL,width=450,bd=1,relief="solid")
        self.control_panel.grid(row=0, column=1,sticky="nsew")

        self.control_header = Frame(self.control_panel,bg="#162032",height=55)
        self.control_header.pack(fill="x")
        self.control_header.pack_propagate(False)

        self.control_header_label = Label(self.control_header,text="⚙  Controls",bg="#162032",fg=WHITE_TEXT,font=HEADING_FONT)
        self.control_header_label.pack(side="left",padx=20)

        self.control_body = Frame(self.control_panel, bg=PANEL)
        self.control_body.pack(fill="both", expand=True, padx=20, pady=20)

        # Bottom status frame
        self.bottom_bar = Frame(self.main_frame, bg=BG)
        self.bottom_bar.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="ew")

        self.bottom_bar.columnconfigure(0, weight=1)

        # Status label
        self.status_bar = Label(
            self.bottom_bar,
            text="Ready",
            bg=BG,
            fg=WHITE_TEXT,
            font=LABEL_FONT,
            anchor="w"
        )
        self.status_bar.grid(row=0, column=0, sticky="w")

        # Save button
        self.save_button = Button(
            self.bottom_bar,
            text="💾 Save Image",
            bg=ACCENT,
            fg=WHITE_TEXT,
            font=BUTTON_FONT,
            activebackground=BUTTON_HOVER,
            activeforeground=WHITE_TEXT,
            relief="flat",
            cursor="hand2",
            padx=20,
            command=self.save_image
        )
        self.save_button.grid(row=0, column=1, sticky="e")

        self.upload_button = Button(self.control_body,text="📂 Upload Image",font=BUTTON_FONT,bg=ACCENT,fg=WHITE_TEXT,activebackground=BUTTON_HOVER,activeforeground=WHITE_TEXT,relief="flat",cursor="hand2",command=self.upload_picture)
        self.upload_button.pack(fill="x",pady=(0,20))


        self.watermark_label = Label(self.control_body,text="Watermark Text", bg=PANEL,fg=WHITE_TEXT,font=LABEL_FONT)
        self.watermark_label.pack(anchor="w",pady=(0,5))

        self.watermark_entry = Entry(self.control_body,font=LABEL_FONT,relief="flat",bd=5)
        self.watermark_entry.bind("<KeyRelease>", self.text_changed)
        self.watermark_entry.pack(fill='x',pady=(0,20))

        self.font_size_label = Label(self.control_body,text="Font Size",bg=PANEL,fg=WHITE_TEXT,font=LABEL_FONT)

        self.font_size = IntVar(value=40)
        self.font_size_slider = Scale(
            self.control_body,
            from_=10,
            to=100,
            orient="horizontal",
            variable=self.font_size,
            bg=PANEL,
            fg=WHITE_TEXT,
            highlightthickness=0,
            troughcolor="#293548",
            activebackground=ACCENT,
            font=LABEL_FONT,
            command=self.update_font_size,
            length=350
        )

        self.font_size_value = Label(self.control_body,bg=PANEL,fg=ACCENT,font=LABEL_FONT,text="40")

        self.opacity_label = Label(self.control_body,bg=PANEL,fg=WHITE_TEXT,font=LABEL_FONT,text="Opacity")
        self.opacity = IntVar(value=128)

        self.opacity_slider = Scale(
            self.control_body,
            from_=0,
            to=255,
            orient="horizontal",
            variable=self.opacity,
            bg=PANEL,
            fg=WHITE_TEXT,
            highlightthickness=0,
            troughcolor="#293548",
            activebackground=ACCENT,
            font=LABEL_FONT,
            command=self.update_opacity,
            length=350
        )
        self.opacity_value = Label(self.control_body,bg=PANEL,fg=ACCENT,font=LABEL_FONT,text="128")

        self.position = StringVar(value="bottom_right")


        self.font_size_label.pack(anchor="w",pady=(0,5))
        self.font_size_slider.pack(anchor="w",pady=(0,20))
        self.font_size_value.pack(anchor="e")
        self.opacity_label.pack(anchor="w",pady=(0,5))
        self.opacity_slider.pack(fill="x")
        self.opacity_value.pack(anchor="e",pady=(0,20))

        self.position_label = Label(
            self.control_body,
            text="Watermark Position",
            bg=PANEL,
            fg=WHITE_TEXT,
            font=LABEL_FONT
        )
        self.position_label.pack(anchor="w", pady=(10, 5))

        self.position = StringVar(value="Bottom Right")

        self.position_combo = ttk.Combobox(
            self.control_body,
            textvariable=self.position,
            state="readonly",
            values=[
                "Top Left",
                "Top Right",
                "Center",
                "Bottom Left",
                "Bottom Right"
            ]
        )
        self.position_combo.pack(fill="x", pady=(0, 20))
        self.position_combo.bind("<<ComboboxSelected>>", lambda e: self.refresh_preview())





    def upload_picture(self):
        file_path = filedialog.askopenfilename(
            title="Select an Image",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if not file_path:
            return
        self.image_path = file_path
        self.display_image(file_path)
    def display_image(self,path):
        self.original_image = Image.open(path)
        self.image = self.original_image.copy()

        self.window.update_idletasks()

        width = self.preview_area.winfo_width()
        height = self.preview_area.winfo_height()

        preview = self.image.copy()
        preview.thumbnail((width,height))

        self.tk_image = ImageTk.PhotoImage(preview)
        if self.image_label:
            self.image_label.destroy()

        if self.placeholder is not None:
            self.placeholder.destroy()
            self.placeholder = None

        self.image_label = Label(self.preview_area,image=self.tk_image,bg="#293548")
        self.image_label.pack(expand=True)
        self.status_bar.config(text="Image Uploaded")

    def update_preview(self):
        if not self.original_image:
            self.status_bar.config(text="Please upload an image first.")
            return
        if self.image is None:
            self.status_bar.config(text="Please add an Image first.")
            return
        text = self.watermark_entry.get().strip()
        if not text:
            self.status_bar.config(text="Please add a text first.")
            return
        self.image = self.original_image.copy().convert("RGBA")
        watermark = Image.new("RGBA",self.image.size,(255,255,255,0))
        draw = ImageDraw.Draw(watermark)
        font_size = self.font_size.get()
        try:
            font= ImageFont.truetype("arial.ttf",font_size)
        except:
            font = ImageFont.load_default()
        bbox = draw.textbbox((0,0),text=text,font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        margin = 20
        position = self.position.get()
        if position == "Top Left":
            x = margin
            y = margin

        elif position == "Top Right":
            x = self.image.width - text_width - margin
            y = margin

        elif position == "Bottom Left":
            x = margin
            y = self.image.height - text_height - margin

        elif position == "Center":
            x = (self.image.width - text_width) // 2
            y = (self.image.height - text_height) // 2

        else:  # Bottom Right
            x = self.image.width - text_width - margin
            y = self.image.height - text_height - margin
        alpha= self.opacity.get()
        text_color = (255,255,255,alpha)
        draw.text((x,y),text,font=font,fill=text_color)
        self.image = Image.alpha_composite(self.image,watermark)
        self.image = self.image.convert("RGB")

        preview = self.image.copy()
        preview.thumbnail((self.preview_area.winfo_width(),self.preview_area.winfo_height()))
        self.tk_image = ImageTk.PhotoImage(preview)
        if self.image_label:
            self.image_label.config(image=self.tk_image)
        self.status_bar.config(text=f"Watermark Applied (Font Size: {self.font_size.get()})")

    def update_font_size(self,value):
        self.font_size_value.config(text=value)
        self.refresh_preview()

    def update_opacity(self,value):
        self.opacity_value.config(text=value)
        self.refresh_preview()

    def text_changed(self,event):
        self.refresh_preview()

    def refresh_preview(self):
        if self.original_image:
            self.update_preview()

    def save_image(self):
        if self.image is None:
            self.status_bar.config(text="No image to save.")
            return
        self.update_preview()
        file_path = filedialog.asksaveasfilename(
            title="Save Image",
            defaultextension=".jpg",
            filetypes=[
                ("PNG Image", "*.png"),
                ("JPEG Image", "*.jpg"),
                ("JPEG Image", "*.jpeg"),
                ("BMP Image", "*.bmp")
            ]
        )
        if not file_path:
            return
        save_image = self.image.convert("RGB")
        save_image.save(file_path)
