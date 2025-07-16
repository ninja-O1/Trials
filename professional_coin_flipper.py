import tkinter as tk
from tkinter import ttk
import time
import threading
import random
import math

class ProfessionalCoinFlipper:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Coin Flip Analytics System™ v2.1")
        self.root.geometry("600x500")
        self.root.configure(bg='#1a1a1a')
        
        # Statistics tracking
        self.flip_count = 0
        self.heads_count = 0
        self.tails_count = 0
        
        # Main frame
        main_frame = tk.Frame(root, bg='#1a1a1a', padx=30, pady=20)
        main_frame.pack(expand=True, fill='both')
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🪙 PROFESSIONAL COIN FLIP SYSTEM 🪙",
            font=('Arial', 16, 'bold'),
            fg='#00ff88',
            bg='#1a1a1a'
        )
        title_label.pack(pady=(0, 10))
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Advanced Probability Analysis & Quantum Randomization Engine",
            font=('Arial', 10, 'italic'),
            fg='#888888',
            bg='#1a1a1a'
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Coin display
        self.coin_frame = tk.Frame(main_frame, bg='#1a1a1a')
        self.coin_frame.pack(pady=20)
        
        self.coin_label = tk.Label(
            self.coin_frame,
            text="🪙",
            font=('Arial', 80),
            bg='#1a1a1a'
        )
        self.coin_label.pack()
        
        # Flip button
        self.flip_btn = tk.Button(
            main_frame,
            text="🚀 INITIATE COIN FLIP SEQUENCE 🚀",
            font=('Arial', 14, 'bold'),
            bg='#ff6b35',
            fg='white',
            padx=30,
            pady=10,
            command=self.flip_coin,
            cursor='hand2'
        )
        self.flip_btn.pack(pady=20)
        
        # Progress frame
        self.progress_frame = tk.Frame(main_frame, bg='#1a1a1a')
        self.progress_frame.pack(pady=20, fill='x')
        
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            length=500,
            mode='determinate',
            style='Custom.Horizontal.TProgressbar'
        )
        
        self.status_label = tk.Label(
            self.progress_frame,
            text="",
            font=('Arial', 11),
            fg='#00aaff',
            bg='#1a1a1a'
        )
        
        # Result frame
        self.result_frame = tk.Frame(main_frame, bg='#1a1a1a')
        self.result_frame.pack(pady=20, fill='x')
        
        self.result_label = tk.Label(
            self.result_frame,
            text="",
            font=('Arial', 18, 'bold'),
            fg='#ffff00',
            bg='#1a1a1a'
        )
        
        # Statistics frame
        self.stats_frame = tk.Frame(main_frame, bg='#2d2d2d', relief='ridge', bd=2)
        self.stats_frame.pack(pady=20, fill='x', padx=20)
        
        stats_title = tk.Label(
            self.stats_frame,
            text="📊 ADVANCED ANALYTICS DASHBOARD 📊",
            font=('Arial', 12, 'bold'),
            fg='#00ff88',
            bg='#2d2d2d'
        )
        stats_title.pack(pady=10)
        
        self.stats_label = tk.Label(
            self.stats_frame,
            text="Total Flips: 0 | Heads: 0 (0.0%) | Tails: 0 (0.0%)",
            font=('Arial', 10),
            fg='#cccccc',
            bg='#2d2d2d'
        )
        self.stats_label.pack(pady=(0, 10))
        
        # Professional analysis messages
        self.analysis_messages = [
            "🔬 Calibrating quantum random number generators...",
            "🌍 Consulting gravitational field data...",
            "🧬 Analyzing molecular coin composition...",
            "📡 Accessing NASA probability databases...",
            "🤖 Initializing AI prediction algorithms...",
            "⚡ Calculating atmospheric pressure effects...",
            "🎯 Determining optimal flip trajectory...",
            "🔮 Consulting ancient probability oracles...",
            "🌟 Synchronizing with cosmic radiation patterns...",
            "💻 Running Monte Carlo simulations...",
            "🎲 Activating chaos theory processors...",
            "🧮 Cross-referencing with mathematical constants..."
        ]
        
        # Center window
        self.center_window()
        
        # Configure progress bar style
        self.setup_progressbar_style()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def setup_progressbar_style(self):
        style = ttk.Style()
        style.configure('Custom.Horizontal.TProgressbar', 
                       background='#00ff88',
                       troughcolor='#333333',
                       bordercolor='#555555',
                       lightcolor='#00ff88',
                       darkcolor='#00aa66')
    
    def flip_coin(self):
        # Disable button
        self.flip_btn.config(state='disabled')
        
        # Clear previous results
        self.result_label.config(text="")
        self.result_label.pack_forget()
        
        # Start the "professional" analysis
        thread = threading.Thread(target=self.perform_analysis)
        thread.daemon = True
        thread.start()
    
    def perform_analysis(self):
        # Show progress elements
        self.progress_bar.pack(pady=(0, 10))
        self.status_label.pack()
        
        # Phase 1: Initial analysis
        selected_messages = random.sample(self.analysis_messages, 4)
        
        for i, message in enumerate(selected_messages):
            self.update_status(message)
            
            # Animate coin during analysis
            self.animate_coin_analysis()
            
            # Progress simulation
            for j in range(20):
                progress = (i * 20) + j + 1
                self.progress_bar['value'] = progress
                self.root.update_idletasks()
                time.sleep(0.08)
        
        # Phase 2: Final calculation
        self.update_status("🎯 Executing final probability calculation...")
        for i in range(20):
            self.progress_bar['value'] = 80 + i
            self.root.update_idletasks()
            time.sleep(0.05)
        
        # The "complex" result
        result = random.choice(['HEADS', 'TAILS'])
        
        # Hide progress elements
        self.progress_bar.pack_forget()
        self.status_label.pack_forget()
        
        # Show result with dramatic reveal
        self.reveal_result(result)
        
        # Update statistics
        self.update_statistics(result)
        
        # Re-enable button
        self.flip_btn.config(state='normal')
    
    def animate_coin_analysis(self):
        # Spin the coin during analysis
        spin_chars = ['🪙', '⚪', '🟡', '⚪']
        for _ in range(3):
            for char in spin_chars:
                self.coin_label.config(text=char)
                self.root.update_idletasks()
                time.sleep(0.1)
    
    def update_status(self, message):
        self.status_label.config(text=message)
        self.root.update_idletasks()
    
    def reveal_result(self, result):
        # Dramatic coin flip animation
        self.animate_coin_flip()
        
        # Set final coin appearance
        if result == 'HEADS':
            self.coin_label.config(text='🪙', fg='#ffd700')
            result_text = "🎉 ANALYSIS COMPLETE! 🎉\n\n💫 RESULT: HEADS 💫\n\n✨ Probability: 50.000% ✨"
            color = '#ffd700'
        else:
            self.coin_label.config(text='🪙', fg='#c0c0c0')
            result_text = "🎉 ANALYSIS COMPLETE! 🎉\n\n💫 RESULT: TAILS 💫\n\n✨ Probability: 50.000% ✨"
            color = '#c0c0c0'
        
        self.result_label.config(text=result_text, fg=color)
        self.result_label.pack(pady=20)
        
        # Victory animation
        self.animate_victory()
    
    def animate_coin_flip(self):
        # Simulate coin flipping in air
        positions = ['🪙', '⚪', '🟡', '⚪', '🪙', '⚪', '🟡', '⚪']
        for pos in positions:
            self.coin_label.config(text=pos)
            self.root.update_idletasks()
            time.sleep(0.15)
    
    def animate_victory(self):
        # Color celebration
        colors = ['#ffd700', '#ff6b35', '#00ff88', '#00aaff', '#ff69b4']
        for i in range(8):
            color = colors[i % len(colors)]
            self.result_label.config(fg=color)
            self.root.update_idletasks()
            time.sleep(0.2)
    
    def update_statistics(self, result):
        self.flip_count += 1
        
        if result == 'HEADS':
            self.heads_count += 1
        else:
            self.tails_count += 1
        
        heads_pct = (self.heads_count / self.flip_count) * 100 if self.flip_count > 0 else 0
        tails_pct = (self.tails_count / self.flip_count) * 100 if self.flip_count > 0 else 0
        
        stats_text = f"Total Flips: {self.flip_count} | Heads: {self.heads_count} ({heads_pct:.1f}%) | Tails: {self.tails_count} ({tails_pct:.1f}%)"
        self.stats_label.config(text=stats_text)

def main():
    root = tk.Tk()
    app = ProfessionalCoinFlipper(root)
    root.mainloop()

if __name__ == "__main__":
    main()