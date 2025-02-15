import nltk
import random
import string
import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

pairs = [
    
    [r"hello|hi|hey", ["Hello! 😊", "Hi there! How can I help?", "Hey! Need any help?"]],
    [r"how are you", ["I'm great! How about you?", "Feeling good today! What about you?"]],
    [r"what is your name", ["I'm ChatBot 2.0!", "You can call me SmartBot."]],
    [r"what is the best car brand", ["Popular car brands include Tesla, BMW, Mercedes, Toyota, and Audi! 🚗"]],
    [r"what is the best smartphone brand", ["Top smartphone brands include Apple, Samsung, Google, and OnePlus! 📱"]],
    [r"what is the most popular fast food", ["Burgers, pizza, and fried chicken are among the most popular fast foods worldwide! 🍔🍕🍗"]],
    [r"what is the tallest building in the world", ["The Burj Khalifa in Dubai is currently the tallest building, standing at 828 meters! 🏙"]],
    [r"what is the best laptop brand", ["There are many great brands like Apple, Dell, HP, and Lenovo! 💻"]],
    [r"what is the best RAM for gaming", ["For gaming, 16GB or 32GB DDR5 RAM is a great choice! ⚡"]],
    [r"who is the best football player", ["That's a tough question! Some say Messi, others say Ronaldo!"]],
    [r"what is the best phone company", ["There are many great companies like Apple, Samsung, and Xiaomi! "]],
    [r"who invented the light bulb", ["The light bulb was developed by Thomas Edison in 1879! 💡"]],
    [r"how many planets are in the solar system", ["There are 8 planets in our solar system! 🪐"]],
    [r"tell me a joke", ["Why don’t skeletons play football? Because they don’t have the heart! 😂", "Why did the scarecrow win an award? Because he was outstanding in his field! 😂"]],
    [r"(.*) weather", ["I can't check the weather right now, but you can try a weather app!", "I don't have live updates, but I hope it's sunny!"]],
    [r"(.*)", ["I'm not sure I understand, could you rephrase?", "Hmm, can you ask in another way?"]],
]
chatbot = Chat(pairs, reflections)
class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 Chatbot")
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f4f4")
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, state='disabled', font=("Arial", 12), bg="white")
        self.chat_display.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.user_input = tk.Entry(root, width=40, font=("Arial", 12))
        self.user_input.grid(row=1, column=0, padx=10, pady=10)
        self.user_input.bind("<Return>", self.send_message) 

        self.send_button = tk.Button(root, text="Send", command=self.send_message, font=("Arial", 12), bg="#4CAF50", fg="white")
        self.send_button.grid(row=1, column=1, padx=5, pady=10)

        
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_chat, font=("Arial", 12), bg="#FF5733", fg="white")
        self.clear_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.update_chat("🤖 Chatbot: Hello!")

    def send_message(self, event=None):
        user_text = self.user_input.get().strip().lower()
        if user_text:
            self.update_chat("You: " + user_text)
            response = chatbot.respond(user_text)
            if response:
                self.update_chat("🤖 Chatbot: " + response)
            else:
                self.update_chat("🤖 Chatbot: I'm not sure I understand, could you rephrase?")
            self.user_input.delete(0, tk.END)

    def update_chat(self, message):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message + "\n\n")
        self.chat_display.config(state='disabled')
        self.chat_display.yview(tk.END)

    def clear_chat(self):
        self.chat_display.config(state='normal')
        self.chat_display.delete('1.0', tk.END)
        self.chat_display.config(state='disabled')
        self.update_chat("🤖 Chatbot: Hello!")

if __name__ == "__main__":
    root = tk.Tk()
    chat_gui = ChatbotGUI(root)
    root.mainloop()