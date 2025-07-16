import tkinter as tk
from tkinter import ttk
import time
import threading
import random
import string

class ProfessionalPasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Password Generator™ - Pentagon Security Division")
        self.root.geometry("750x650")
        self.root.configure(bg='#0d1117')
        
        # Security clearance simulation
        self.security_level = 0
        self.passwords_generated = 0
        
        # Main frame
        main_frame = tk.Frame(root, bg='#0d1117', padx=30, pady=25)
        main_frame.pack(expand=True, fill='both')
        
        # Top secret header
        header_frame = tk.Frame(main_frame, bg='#ff0000', relief='ridge', bd=3)
        header_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(
            header_frame,
            text="🔴 TOP SECRET - CLEARANCE LEVEL ALPHA 🔴",
            font=('Courier', 12, 'bold'),
            fg='#ffffff',
            bg='#ff0000'
        ).pack(pady=5)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="🔒 PENTAGON PASSWORD GENERATOR 🔒",
            font=('Courier', 20, 'bold'),
            fg='#00ff41',
            bg='#0d1117'
        )
        title_label.pack(pady=(0, 10))
        
        # Subtitle
        subtitle_label = tk.Label(
            main_frame,
            text="Military-Grade Cryptographic Security Engine v3.7",
            font=('Courier', 12, 'italic'),
            fg='#58a6ff',
            bg='#0d1117'
        )
        subtitle_label.pack(pady=(0, 20))
        
        # Security warning
        warning_frame = tk.Frame(main_frame, bg='#ffa500', relief='ridge', bd=2)
        warning_frame.pack(fill='x', pady=(0, 25))
        
        tk.Label(
            warning_frame,
            text="⚠️ WARNING: This system accesses classified algorithms ⚠️",
            font=('Courier', 10, 'bold'),
            fg='#000000',
            bg='#ffa500'
        ).pack(pady=8)
        
        # Configuration frame
        config_frame = tk.Frame(main_frame, bg='#161b22', relief='ridge', bd=3)
        config_frame.pack(fill='x', pady=(0, 20))
        
        config_title = tk.Label(
            config_frame,
            text="⚙️ SECURITY CONFIGURATION MATRIX ⚙️",
            font=('Courier', 14, 'bold'),
            fg='#f0e68c',
            bg='#161b22'
        )
        config_title.pack(pady=10)
        
        # Password length selector
        length_frame = tk.Frame(config_frame, bg='#161b22')
        length_frame.pack(pady=10)
        
        tk.Label(
            length_frame,
            text="Password Length (Security Factor):",
            font=('Courier', 11),
            fg='#ffffff',
            bg='#161b22'
        ).pack(side=tk.LEFT, padx=(20, 10))
        
        self.length_var = tk.StringVar(value="8")
        length_combo = ttk.Combobox(
            length_frame,
            textvariable=self.length_var,
            values=["4", "6", "8", "10", "12", "16"],
            state="readonly",
            font=('Courier', 11),
            width=10
        )
        length_combo.pack(side=tk.LEFT)
        
        # Security level display
        security_frame = tk.Frame(config_frame, bg='#161b22')
        security_frame.pack(pady=10)
        
        tk.Label(
            security_frame,
            text="Current Security Clearance:",
            font=('Courier', 11),
            fg='#ffffff',
            bg='#161b22'
        ).pack(side=tk.LEFT, padx=(20, 10))
        
        self.security_display = tk.Label(
            security_frame,
            text="CLASSIFIED",
            font=('Courier', 11, 'bold'),
            fg='#ff0000',
            bg='#161b22'
        )
        self.security_display.pack(side=tk.LEFT)
        
        # Generation button
        self.generate_btn = tk.Button(
            config_frame,
            text="🚀 INITIATE PENTAGON PROTOCOL 🚀",
            font=('Courier', 14, 'bold'),
            bg='#dc143c',
            fg='#ffffff',
            padx=30,
            pady=15,
            command=self.generate_password,
            cursor='hand2'
        )
        self.generate_btn.pack(pady=20)
        
        # Processing frame
        self.processing_frame = tk.Frame(main_frame, bg='#0d1117')
        self.processing_frame.pack(fill='x', pady=20)
        
        # Multiple security stages
        self.stage_frames = []
        self.stage_labels = []
        self.stage_progress = []
        
        stage_names = [
            "🔐 Cryptographic Analysis",
            "🛡️ Pentagon Database Access", 
            "🔍 Security Validation",
            "⚡ Quantum Encryption"
        ]
        
        for stage_name in stage_names:
            frame = tk.Frame(self.processing_frame, bg='#0d1117')
            
            label = tk.Label(
                frame,
                text=stage_name,
                font=('Courier', 10, 'bold'),
                fg='#ffa500',
                bg='#0d1117'
            )
            
            progress = ttk.Progressbar(
                frame,
                length=600,
                mode='determinate'
            )
            
            self.stage_frames.append(frame)
            self.stage_labels.append(label)
            self.stage_progress.append(progress)
        
        # Status monitor
        self.status_frame = tk.Frame(main_frame, bg='#000000', relief='ridge', bd=2)
        self.status_frame.pack(fill='x', pady=20)
        
        status_title = tk.Label(
            self.status_frame,
            text="📡 PENTAGON SECURITY MONITOR 📡",
            font=('Courier', 12, 'bold'),
            fg='#00ff00',
            bg='#000000'
        )
        status_title.pack(pady=5)
        
        self.status_label = tk.Label(
            self.status_frame,
            text="STATUS: Awaiting Authorization",
            font=('Courier', 10),
            fg='#00ff00',
            bg='#000000'
        )
        self.status_label.pack(pady=5)
        
        # Result frame
        self.result_frame = tk.Frame(main_frame, bg='#1a1a1a', relief='ridge', bd=3)
        self.result_frame.pack(fill='x', pady=20)
        
        result_title = tk.Label(
            self.result_frame,
            text="🎯 CLASSIFIED PASSWORD OUTPUT 🎯",
            font=('Courier', 14, 'bold'),
            fg='#ffff00',
            bg='#1a1a1a'
        )
        result_title.pack(pady=10)
        
        self.password_display = tk.Label(
            self.result_frame,
            text="",
            font=('Courier', 18, 'bold'),
            fg='#00ff00',
            bg='#1a1a1a'
        )
        
        self.copy_btn = tk.Button(
            self.result_frame,
            text="📋 COPY TO SECURE CLIPBOARD",
            font=('Courier', 10, 'bold'),
            bg='#4169e1',
            fg='#ffffff',
            command=self.copy_password,
            cursor='hand2'
        )
        
        # Statistics
        self.stats_frame = tk.Frame(main_frame, bg='#2d2d2d', relief='ridge', bd=2)
        self.stats_frame.pack(fill='x', pady=10)
        
        self.stats_label = tk.Label(
            self.stats_frame,
            text="Passwords Generated: 0 | Security Incidents: 0 | Clearance Level: RESTRICTED",
            font=('Courier', 9),
            fg='#cccccc',
            bg='#2d2d2d'
        )
        self.stats_label.pack(pady=8)
        
        # Pentagon security messages
        self.security_messages = [
            "🔐 Accessing Pentagon mainframe...",
            "🛡️ Authenticating security credentials...",
            "🔍 Scanning for security vulnerabilities...",
            "💻 Consulting NSA databases...",
            "🌍 Synchronizing with global security network...",
            "⚡ Activating quantum encryption protocols...",
            "🎯 Applying military-grade algorithms...",
            "🚀 Initializing cryptographic sequences...",
            "🧬 Analyzing DNA-based security patterns...",
            "📡 Connecting to satellite encryption systems...",
            "🔬 Running Pentagon security simulations...",
            "🎲 Generating secure random entropy..."
        ]
        
        # Simple passwords for the joke
        self.simple_passwords = [
            "password123", "admin123", "letmein", "qwerty123", 
            "welcome1", "123456", "password1", "admin", 
            "user123", "login123", "secure1", "pass123"
        ]
        
        self.generated_password = ""
        
        # Center window
        self.center_window()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
    
    def generate_password(self):
        # Hide previous results
        self.password_display.pack_forget()
        self.copy_btn.pack_forget()
        
        # Disable button
        self.generate_btn.config(state='disabled')
        
        # Start the "Pentagon security process"
        thread = threading.Thread(target=self.perform_security_generation)
        thread.daemon = True
        thread.start()
    
    def perform_security_generation(self):
        # Phase 1: Security clearance verification
        self.update_status("🔒 Verifying security clearance...")
        time.sleep(1)
        
        # Show security stages
        selected_messages = random.sample(self.security_messages, 4)
        
        for i, (message, stage_frame, stage_label, progress_bar) in enumerate(
            zip(selected_messages, self.stage_frames, self.stage_labels, self.stage_progress)
        ):
            # Show current stage
            stage_frame.pack(pady=5, fill='x')
            stage_label.pack(pady=(0, 5))
            progress_bar.pack(pady=(0, 10))
            
            self.update_status(message)
            
            # Animate progress
            for j in range(100):
                progress_bar['value'] = j + 1
                self.root.update_idletasks()
                time.sleep(0.08)
            
            # Brief pause between stages
            time.sleep(0.5)
        
        # Final security check
        self.update_status("🎯 Finalizing password generation...")
        time.sleep(1)
        
        # Generate the "secure" password (actually simple)
        password_length = int(self.length_var.get())
        
        if password_length <= 8:
            # Use simple passwords for shorter lengths
            password = random.choice(self.simple_passwords)
        else:
            # For longer lengths, add some numbers to a simple base
            base_password = random.choice(["password", "admin", "secure", "login"])
            numbers = ''.join(random.choices('123456789', k=password_length - len(base_password)))
            password = base_password + numbers
        
        self.generated_password = password
        
        # Hide progress bars
        for frame in self.stage_frames:
            frame.pack_forget()
        
        # Update security level (fake)
        self.security_level += 1
        clearance_levels = ["RESTRICTED", "CONFIDENTIAL", "SECRET", "TOP SECRET", "COSMIC"]
        current_clearance = clearance_levels[min(self.security_level, len(clearance_levels) - 1)]
        self.security_display.config(text=current_clearance)
        
        # Show result
        self.show_password_result(password)
        
        # Update statistics
        self.passwords_generated += 1
        self.update_statistics()
        
        # Re-enable button
        self.generate_btn.config(state='normal')
        
        # Final status
        self.update_status("STATUS: Password generation complete - CLASSIFIED")
    
    def update_status(self, message):
        self.status_label.config(text=f"STATUS: {message}")
        self.root.update_idletasks()
    
    def show_password_result(self, password):
        # Display with dramatic effect
        self.password_display.config(text=f"🔐 {password} 🔐")
        self.password_display.pack(pady=15)
        
        self.copy_btn.pack(pady=(0, 15))
        
        # Security animation
        self.animate_security_effect()
    
    def animate_security_effect(self):
        # Flashing security colors
        security_colors = ['#ff0000', '#00ff00', '#ffff00', '#00ffff']
        for i in range(8):
            color = security_colors[i % len(security_colors)]
            self.password_display.config(fg=color)
            self.root.update_idletasks()
            time.sleep(0.2)
        
        # Final secure green
        self.password_display.config(fg='#00ff00')
    
    def copy_password(self):
        if self.generated_password:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.generated_password)
            
            # Show copy confirmation
            original_text = self.copy_btn.cget('text')
            self.copy_btn.config(text="✅ COPIED TO SECURE CLIPBOARD", bg='#008000')
            self.root.after(2000, lambda: self.copy_btn.config(text=original_text, bg='#4169e1'))
    
    def update_statistics(self):
        stats_text = f"Passwords Generated: {self.passwords_generated} | Security Incidents: 0 | Clearance Level: {self.security_display.cget('text')}"
        self.stats_label.config(text=stats_text)

def main():
    root = tk.Tk()
    app = ProfessionalPasswordGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()