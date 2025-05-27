import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Máy Tính Đơn Giản")
        
        # Tạo các biến để lưu trữ các widget nhập liệu
        self.num1_var = tk.StringVar()
        self.num2_var = tk.StringVar()
        self.result_var = tk.StringVar()
        
        # Thiết kế giao diện
        self.create_widgets()
        
    def create_widgets(self):
        # Tạo khung chứa các widget
        main_frame = tk.Frame(self.root, padx=20, pady=10)
        main_frame.pack(expand=True)
        
        # Nhãn và ô nhập số thứ nhất
        tk.Label(main_frame, text="Số thứ nhất:").grid(row=0, column=0, sticky='w', pady=5)
        num1_entry = tk.Entry(main_frame, textvariable=self.num1_var)
        num1_entry.grid(row=0, column=1, padx=5, pady=5)
        
        # Nhãn và ô nhập số thứ hai
        tk.Label(main_frame, text="Số thứ hai:").grid(row=1, column=0, sticky='w', pady=5)
        num2_entry = tk.Entry(main_frame, textvariable=self.num2_var)
        num2_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Khung chứa các nút phép tính
        button_frame = tk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Các nút phép tính
        operations = [('+', self.add), ('-', self.subtract),
                     ('×', self.multiply), ('÷', self.divide)]
        
        for i, (symbol, command) in enumerate(operations):
            tk.Button(button_frame, text=symbol, width=5,
                     command=command).grid(row=0, column=i, padx=5)
        
        # Nhãn kết quả
        tk.Label(main_frame, text="Kết quả:").grid(row=3, column=0, sticky='w', pady=5)
        result_label = tk.Label(main_frame, textvariable=self.result_var,
                              width=20, relief='sunken')
        result_label.grid(row=3, column=1, padx=5, pady=5)
    
    def validate_input(self):
        """Kiểm tra tính hợp lệ của dữ liệu nhập vào"""
        try:
            # Lấy giá trị từ ô nhập liệu và chuyển thành số nguyên
            num1 = int(self.num1_var.get())
            num2 = int(self.num2_var.get())
            
            # Kiểm tra số âm
            if num1 < 0 or num2 < 0:
                messagebox.showerror("Lỗi", "Vui lòng nhập số tự nhiên (không âm)")
                return None, None
            
            return num1, num2
            
        except ValueError:
            messagebox.showerror("Lỗi", "Vui lòng nhập số tự nhiên hợp lệ")
            return None, None
    
    def add(self):
        """Thực hiện phép cộng"""
        num1, num2 = self.validate_input()
        if num1 is not None and num2 is not None:
            self.result_var.set(str(num1 + num2))
    
    def subtract(self):
        """Thực hiện phép trừ"""
        num1, num2 = self.validate_input()
        if num1 is not None and num2 is not None:
            self.result_var.set(str(num1 - num2))
    
    def multiply(self):
        """Thực hiện phép nhân"""
        num1, num2 = self.validate_input()
        if num1 is not None and num2 is not None:
            self.result_var.set(str(num1 * num2))
    
    def divide(self):
        """Thực hiện phép chia"""
        num1, num2 = self.validate_input()
        if num1 is not None and num2 is not None:
            # Kiểm tra chia cho 0
            if num2 == 0:
                messagebox.showerror("Lỗi", "Không thể chia cho 0")
                return
            # Thực hiện phép chia và làm tròn đến 2 chữ số thập phân
            result = round(num1 / num2, 2)
            self.result_var.set(str(result))

# Tạo cửa sổ chính và khởi chạy ứng dụng
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()