import tkinter as tk
from tkinter import ttk
import time
import threading
import random

class NextYearCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Year Prediction System™")
        self.root.geometry("500x400")
        self.root.configure(bg='#2c3e50')
        
        # Main frame
        main_frame = tk.Frame(root, bg='#2c3e50', padx=20, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        # Title
        title_label = tk.Label(
            main_frame, 
            text="🔮 Next Year Prediction System 🔮",
            font=('Arial', 18, 'bold'),
            fg='#ecf0f1',
            bg='#2c3e50'
        )
        title_label.pack(pady=(0, 20))
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Using advanced algorithms to calculate the next year",
            font=('Arial', 10, 'italic'),
            fg='#bdc3c7',
            bg='#2c3e50'
        )
        subtitle_label.pack(pady=(0, 30))
        
        # Input frame
        input_frame = tk.Frame(main_frame, bg='#2c3e50')
        input_frame.pack(pady=20)
        
        tk.Label(
            input_frame,
            text="Enter current year:",
            font=('Arial', 12),
            fg='#ecf0f1',
            bg='#2c3e50'
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.year_entry = tk.Entry(
            input_frame,
            font=('Arial', 12),
            width=10,
            justify='center',
            bg='#34495e',
            fg='#ecf0f1',
            insertbackground='#ecf0f1'
        )
        self.year_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.year_entry.bind('<Return>', self.calculate_next_year)
        
        self.calculate_btn = tk.Button(
            input_frame,
            text="Calculate",
            font=('Arial', 12, 'bold'),
            bg='#3498db',
            fg='white',
            padx=20,
            command=self.calculate_next_year,
            cursor='hand2'
        )
        self.calculate_btn.pack(side=tk.LEFT)
        
        # Progress frame
        self.progress_frame = tk.Frame(main_frame, bg='#2c3e50')
        self.progress_frame.pack(pady=30, fill='x')
        
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            length=400,
            mode='determinate'
        )
        
        self.status_label = tk.Label(
            self.progress_frame,
            text="",
            font=('Arial', 11),
            fg='#f39c12',
            bg='#2c3e50'
        )
        
        # Result frame
        self.result_frame = tk.Frame(main_frame, bg='#2c3e50')
        self.result_frame.pack(pady=20, fill='x')
        
        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=('Arial', 16, 'bold'),
            fg='#27ae60',
            bg='#2c3e50'
        )
        
        # Fun messages for loading
        self.loading_messages = [
            "🤖 Initializing quantum year processors...",
            "🔍 Scanning temporal databases...",
            "📊 Analyzing chronological patterns...",
            "🧮 Performing complex mathematical operations...",
            "🌟 Consulting the year prediction algorithms...",
            "⚡ Calibrating time-space continuum...",
            "🎯 Cross-referencing with calendar systems...",
            "🚀 Launching year calculation sequence...",
            "🎲 Rolling the dice of time...",
            "🔮 Gazing into the crystal ball of years..."
        ]
        
        # Center the window
        self.center_window()
        
        # Focus on entry
        self.year_entry.focus()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def calculate_next_year(self, event=None):
        try:
            current_year = int(self.year_entry.get())
            
            # Clear previous results
            self.result_label.config(text="")
            self.result_label.pack_forget()
            
            # Disable button and entry
            self.calculate_btn.config(state='disabled')
            self.year_entry.config(state='disabled')
            
            # Start the "complex" calculation process
            thread = threading.Thread(target=self.perform_calculation, args=(current_year,))
            thread.daemon = True
            thread.start()
            
        except ValueError:
            self.show_error("Please enter a valid year!")
    
    def perform_calculation(self, current_year):
        # Show progress bar
        self.progress_bar.pack(pady=(0, 10))
        self.status_label.pack()
        
        # Phase 1: Loading sequence
        selected_messages = random.sample(self.loading_messages, 3)
        
        for i, message in enumerate(selected_messages):
            self.update_status(message)
            
            # Simulate progress
            for j in range(33):
                progress = (i * 33) + j + 1
                self.progress_bar['value'] = progress
                self.root.update_idletasks()
                time.sleep(0.05)
        
        # Final calculation message
        self.update_status("🎉 Calculation complete! Revealing results...")
        self.progress_bar['value'] = 100
        self.root.update_idletasks()
        time.sleep(0.5)
        
        # Calculate the "complex" result
        next_year = current_year + 1
        
        # Hide progress elements
        self.progress_bar.pack_forget()
        self.status_label.pack_forget()
        
        # Show result with fanfare
        self.show_result(current_year, next_year)
        
        # Re-enable controls
        self.calculate_btn.config(state='normal')
        self.year_entry.config(state='normal')
    
    def update_status(self, message):
        self.status_label.config(text=message)
        self.root.update_idletasks()
    
    def show_result(self, current_year, next_year):
        result_text = f"🎊 BREAKTHROUGH! 🎊\n\nAfter extensive calculations,\nthe year after {current_year} is:\n\n✨ {next_year} ✨"
        self.result_label.config(text=result_text)
        self.result_label.pack(pady=20)
        
        # Add a fun animation effect
        self.animate_result()
    
    def animate_result(self):
        colors = ['#27ae60', '#e74c3c', '#3498db', '#f39c12', '#9b59b6']
        for i in range(10):
            color = colors[i % len(colors)]
            self.result_label.config(fg=color)
            self.root.update_idletasks()
            time.sleep(0.2)
        
        # Set final color
        self.result_label.config(fg='#27ae60')
    
    def show_error(self, message):
        self.result_label.config(text=f"❌ Error: {message}", fg='#e74c3c')
        self.result_label.pack(pady=20)

def main():
    root = tk.Tk()
    app = NextYearCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()