#!/usr/bin/env python3
"""
ai-model-compare - AI模型对比工具
工具编号: tool-065
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

class App:
    def __init__(self, root):
        self.root = root
        root.title("AI模型对比工具 v1.0")
        root.geometry("900x700")
        self.setup_ui()
    
    def setup_ui(self):
        # 标题
        title_frame = tk.Frame(self.root, bg="#673AB7", height=60)
        title_frame.pack(fill="x")
        title_frame.pack_propagate(False)
        tk.Label(title_frame, text="🤖 AI模型对比工具", font=("Arial", 18, "bold"),
                 fg="white", bg="#673AB7").pack(pady=15)
        
        # 主区域
        main = tk.Frame(self.root, padx=20, pady=15)
        main.pack(fill="both", expand=True)
        
        # API设置
        api_frame = tk.LabelFrame(main, text="🔑 API 设置", font=("Arial", 10, "bold"))
        api_frame.pack(fill="x", pady=10)
        
        tk.Label(api_frame, text="API Key:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.api_key_var = tk.StringVar()
        tk.Entry(api_key_var, show="*", width=40).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(api_frame, text="模型:").grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.model_var = tk.StringVar(value="gpt-3.5-turbo")
        model_combo = ttk.Combobox(api_frame, textvariable=self.model_var,
                                    values=["gpt-3.5-turbo", "gpt-4", "claude-3"], width=20)
        model_combo.grid(row=0, column=3, padx=5, pady=5)
        
        # 输入区
        input_frame = tk.LabelFrame(main, text="📝 输入", font=("Arial", 10, "bold"))
        input_frame.pack(fill="both", expand=True, pady=10)
        
        self.input_text = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD,
                                                     font=("Arial", 11), height=8)
        self.input_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        # 按钮
        btn_frame = tk.Frame(main)
        btn_frame.pack(fill="x", pady=10)
        
        tk.Button(btn_frame, text="🚀 发送请求", command=self.send_request,
                  bg="#673AB7", fg="white", font=("Arial", 11, "bold"),
                  padx=25, pady=10).pack(side="left", padx=10)
        tk.Button(btn_frame, text="🗑️ 清空", command=self.clear_all,
                  bg="#f44336", fg="white", padx=15, pady=10).pack(side="left")
        
        # 输出区
        output_frame = tk.LabelFrame(main, text="📄 结果", font=("Arial", 10, "bold"))
        output_frame.pack(fill="both", expand=True, pady=10)
        
        self.output_text = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD,
                                                      font=("Arial", 11), height=10)
        self.output_text.pack(fill="both", expand=True, padx=5, pady=5)
        
        # 状态
        self.status_var = tk.StringVar(value="就绪 - 请输入内容并发送请求")
        tk.Label(main, textvariable=self.status_var, fg="gray").pack(fill="x")
    
    def send_request(self):
        input_text = self.input_text.get(1.0, tk.END).strip()
        if not input_text:
            messagebox.showwarning("提示", "请输入内容！")
            return
        
        self.status_var.set("处理中...")
        self.output_text.delete(1.0, tk.END)
        
        # 模拟AI响应
        response = f"""已收到您的请求！

输入内容:
{input_text}

模型: {self.model_var.get()}

⚠️ 注意: 这是一个演示版本。
要使用真实的AI功能，请:
1. 在设置中输入您的API Key
2. 确保已安装相应依赖 (pip install openai anthropic)
3. 检查网络连接

功能开发中..."""
        
        self.output_text.insert(1.0, response)
        self.status_var.set("✅ 完成")
    
    def clear_all(self):
        self.input_text.delete(1.0, tk.END)
        self.output_text.delete(1.0, tk.END)
        self.status_var.set("已清空")

def main():
    root = tk.Tk()
    App(root)
    root.mainloop()

if __name__ == "__main__":
    main()
