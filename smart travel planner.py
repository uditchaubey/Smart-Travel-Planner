import tkinter as tk
from tkinter import ttk
#  Travel Database 
travel_data = [

    {"place": "Goa", "mood": "Fun", "budget": "High", "purpose": "Vacation", "weather": "Warm"},
    {"place": "Rishikesh", "mood": "Peace", "budget": "Low", "purpose": "Spiritual", "weather": "Pleasant"},
    {"place": "Varanasi", "mood": "Peace", "budget": "Low", "purpose": "Spiritual", "weather": "Pleasant"},
    {"place": "Amritsar", "mood": "Peace", "budget": "Low", "purpose": "Spiritual", "weather": "Pleasant"},

    {"place": "Manali", "mood": "Adventure", "budget": "Medium", "purpose": "Trip", "weather": "Cold"},
    {"place": "Leh Ladakh", "mood": "Adventure", "budget": "High", "purpose": "Trip", "weather": "Cold"},
    {"place": "Shimla", "mood": "Relax", "budget": "Medium", "purpose": "Trip", "weather": "Cold"},
    {"place": "Coorg", "mood": "Relax", "budget": "Medium", "purpose": "Trip", "weather": "Pleasant"},
    {"place": "Ooty", "mood": "Peace", "budget": "Medium", "purpose": "Trip", "weather": "Cold"},
    {"place": "Gangtok", "mood": "Adventure", "budget": "Medium", "purpose": "Trip", "weather": "Cold"},

    {"place": "Udaipur", "mood": "Romantic", "budget": "Medium", "purpose": "Vacation", "weather": "Pleasant"},
    {"place": "Andaman", "mood": "Romantic", "budget": "High", "purpose": "Vacation", "weather": "Warm"},
    {"place": "Kerala", "mood": "Relax", "budget": "Medium", "purpose": "Vacation", "weather": "Warm"},
    {"place": "Darjeeling", "mood": "Peace", "budget": "Medium", "purpose": "Vacation", "weather": "Cold"},

    {"place": "Jaipur", "mood": "Explore", "budget": "Low", "purpose": "Tour", "weather": "Warm"},
    {"place": "Delhi", "mood": "Explore", "budget": "Low", "purpose": "Tour", "weather": "Warm"},
    {"place": "Hyderabad", "mood": "Explore", "budget": "Medium", "purpose": "Tour", "weather": "Warm"},
    {"place": "Agra", "mood": "Romantic", "budget": "Low", "purpose": "Tour", "weather": "Warm"},
    {"place": "Pune", "mood": "Fun", "budget": "Medium", "purpose": "Tour", "weather": "Pleasant"},
]
#  Suggestion Logic 
def suggest_place():

    mood = mood_var.get()
    budget = budget_var.get()
    purpose = purpose_var.get()
    weather = weather_var.get()

    results = []

    for place in travel_data:

        score = 0

        if place["purpose"] == purpose:
            score += 4

        if place["mood"] == mood:
            score += 3

        if place["weather"] == weather:
            score += 2

        if place["budget"] == budget:
            score += 1

        if score > 0:
            results.append((place["place"], score))

    results.sort(key=lambda x: x[1], reverse=True)

    result_box.delete(0, tk.END)

    if results:
        for place, score in results[:5]:
            result_box.insert(tk.END, place)
    else:
        result_box.insert(tk.END, "No suitable place found")
# Clear Function 
def clear_all():
    mood_var.set("")
    budget_var.set("")
    purpose_var.set("")
    weather_var.set("")
    result_box.delete(0, tk.END)
#  Window 
root = tk.Tk()
root.title("Smart Travel Planner")
root.geometry("520x560")
root.configure(bg="#2a2f35")   # lighter dark
#  Title 
title = tk.Label(
    root,
    text="Smart Travel Planner",
    font=("Segoe UI", 20, "bold"),
    bg="#2a2f35",
    fg="#4fc3f7"
)
title.pack(pady=15)
#  Frame 
frame = tk.Frame(root, bg="#3a3f44", bd=0)
frame.pack(padx=20, pady=10, fill="both", expand=True)
# - Style 
style = ttk.Style()
style.theme_use("default")
style.configure(
    "TCombobox",
    fieldbackground="#e0e0e0",
    background="#e0e0e0"
)
#  Mood 
tk.Label(
    frame,
    text="Select Mood",
    bg="#3a3f44",
    fg="white",
    font=("Segoe UI", 12)
).pack(pady=6)
mood_var = tk.StringVar()
mood_menu = ttk.Combobox(
    frame,
    textvariable=mood_var,
    values=["Relax", "Adventure", "Peace", "Fun", "Romantic", "Explore"],
    state="readonly",
    width=25
)
mood_menu.pack(pady=5)
#  Budget 
tk.Label(
    frame,
    text="Select Budget",
    bg="#3a3f44",
    fg="white",
    font=("Segoe UI", 12)
).pack(pady=6)
budget_var = tk.StringVar()
budget_menu = ttk.Combobox(
    frame,
    textvariable=budget_var,
    values=["Low", "Medium", "High"],
    state="readonly",
    width=25
)
budget_menu.pack(pady=5)
#  Purpose 
tk.Label(
    frame,
    text="Select Purpose",
    bg="#3a3f44",
    fg="white",
    font=("Segoe UI", 12)
).pack(pady=6)
purpose_var = tk.StringVar()
purpose_menu = ttk.Combobox(
    frame,
    textvariable=purpose_var,
    values=["Vacation", "Trip", "Spiritual", "Tour"],
    state="readonly",
    width=25
)
purpose_menu.pack(pady=5)
#  Weather 
tk.Label(
    frame,
    text="Preferred Weather",
    bg="#3a3f44",
    fg="white",
    font=("Segoe UI", 12)
).pack(pady=6)

weather_var = tk.StringVar()
weather_menu = ttk.Combobox(
    frame,
    textvariable=weather_var,
    values=["Cold", "Warm", "Pleasant"],
    state="readonly",
    width=25
)
weather_menu.pack(pady=5)
#  Buttons 
btn_frame = tk.Frame(frame, bg="#3a3f44")
btn_frame.pack(pady=15)
suggest_btn = tk.Button(
    btn_frame,
    text="Suggest Place",
    bg="#4fc3f7",
    fg="black",
    font=("Segoe UI", 11, "bold"),
    width=15,
    command=suggest_place
)
suggest_btn.grid(row=0, column=0, padx=10)
clear_btn = tk.Button(
    btn_frame,
    text="Clear",
    bg="#ef5350",
    fg="white",
    font=("Segoe UI", 11, "bold"),
    width=10,
    command=clear_all
)
clear_btn.grid(row=0, column=1, padx=10)
#  Result 
tk.Label(
    frame,
    text="Suggested Places",
    bg="#3a3f44",
    fg="#4fc3f7",
    font=("Segoe UI", 13, "bold")
).pack(pady=5)
result_box = tk.Listbox(
    frame,
    width=45,
    height=10,
    bg="#dcdcdc",
    fg="black",
    font=("Segoe UI", 11),
    bd=0
)
result_box.pack(pady=10)
#  Footer 
footer = tk.Label(
    root,
    text="AI Based Travel Recommendation System",
    bg="#2a2f35",
    fg="#b0bec5",
    font=("Segoe UI", 9)
)
footer.pack(pady=5)
#  Run 
root.mainloop()