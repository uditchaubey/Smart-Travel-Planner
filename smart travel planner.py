import tkinter as tk
from tkinter import ttk
import random

travel_data = [
    {"place": "Goa", "mood": "Relax", "budget": "High", "purpose": "Vacation"},
    {"place": "Manali", "mood": "Adventure", "budget": "Medium", "purpose": "Trip"},
    {"place": "Rishikesh", "mood": "Peace", "budget": "Low", "purpose": "Spiritual"},
    {"place": "Mumbai", "mood": "Fun", "budget": "High", "purpose": "Tour"},
    {"place": "Udaipur", "mood": "Romantic", "budget": "Medium", "purpose": "Vacation"},
    {"place": "Jaipur", "mood": "Explore", "budget": "Low", "purpose": "Tour"},
    {"place": "Shimla", "mood": "Relax", "budget": "Medium", "purpose": "Trip"},
    {"place": "Kerala", "mood": "Relax", "budget": "Medium", "purpose": "Vacation"},
    {"place": "Kashmir", "mood": "Romantic", "budget": "High", "purpose": "Vacation"},
    {"place": "Leh Ladakh", "mood": "Adventure", "budget": "High", "purpose": "Trip"},
    {"place": "Delhi", "mood": "Explore", "budget": "Low", "purpose": "Tour"},
    {"place": "Coorg", "mood": "Relax", "budget": "Medium", "purpose": "Trip"}
]

def suggest_place():
    mood = mood_var.get()
    budget = budget_var.get()
    purpose = purpose_var.get()

    matches = []

    for place in travel_data:
        if place["mood"] == mood and place["budget"] == budget and place["purpose"] == purpose:
            matches.append(place["place"])

    if not matches:
        for place in travel_data:
            if place["mood"] == mood or place["budget"] == budget or place["purpose"] == purpose:
                matches.append(place["place"])

    if not matches:
        matches = [random.choice(travel_data)["place"]]

    result_box.delete(0, tk.END)

    for r in matches:
        result_box.insert(tk.END, r)

def clear_all():
    mood_var.set("")
    budget_var.set("")
    purpose_var.set("")
    result_box.delete(0, tk.END)

root = tk.Tk()
root.title("Smart Travel Planner")
root.geometry("520x480")
root.configure(bg="#1f1f1f")

title = tk.Label(root,
                 text="Smart Travel Planner",
                 font=("Segoe UI", 20, "bold"),
                 bg="#1f1f1f",
                 fg="#00bcd4")
title.pack(pady=15)

frame = tk.Frame(root, bg="#2b2b2b", bd=2)
frame.pack(padx=20, pady=10, fill="both", expand=True)

style = ttk.Style()
style.theme_use("default")
style.configure("TCombobox",
                fieldbackground="#3a3a3a",
                background="#3a3a3a",
                foreground="black")

# Mood
tk.Label(frame, text="Select Mood",
         bg="#2b2b2b", fg="#e6e6e6",
         font=("Segoe UI", 12)).pack(pady=5)

mood_var = tk.StringVar()
mood_menu = ttk.Combobox(frame, textvariable=mood_var,
                         values=["Relax", "Adventure", "Peace", "Fun", "Romantic", "Explore"])
mood_menu.pack(pady=5)

# Budget
tk.Label(frame, text="Select Budget",
         bg="#2b2b2b", fg="#e6e6e6",
         font=("Segoe UI", 12)).pack(pady=5)

budget_var = tk.StringVar()
budget_menu = ttk.Combobox(frame, textvariable=budget_var,
                           values=["Low", "Medium", "High"])
budget_menu.pack(pady=5)

# Purpose
tk.Label(frame, text="Select Purpose",
         bg="#2b2b2b", fg="#e6e6e6",
         font=("Segoe UI", 12)).pack(pady=5)

purpose_var = tk.StringVar()
purpose_menu = ttk.Combobox(frame, textvariable=purpose_var,
                            values=["Vacation", "Trip", "Spiritual", "Tour"])
purpose_menu.pack(pady=5)

btn_frame = tk.Frame(frame, bg="#2b2b2b")
btn_frame.pack(pady=15)

tk.Button(btn_frame,
          text="Suggest Place",
          bg="#4CAF50",
          fg="white",
          font=("Segoe UI", 11, "bold"),
          command=suggest_place).grid(row=0, column=0, padx=10)

tk.Button(btn_frame,
          text="Clear",
          bg="#f44336",
          fg="white",
          font=("Segoe UI", 11, "bold"),
          command=clear_all).grid(row=0, column=1, padx=10)

tk.Label(frame,
         text="Suggested Places",
         bg="#2b2b2b",
         fg="#00bcd4",
         font=("Segoe UI", 13, "bold")).pack()

result_box = tk.Listbox(frame,
                        width=40,
                        height=10,
                        bg="#3a3a3a",
                        fg="white",
                        font=("Segoe UI", 11),
                        bd=0)
result_box.pack(pady=10)

root.mainloop()