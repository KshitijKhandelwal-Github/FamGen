# 👨‍👩‍👧‍👦 FamGen – Family Tree Visualizer

**FamGen** is a simple and interactive web application that lets you **visualize family trees** from CSV or Excel files. Upload your data, and instantly view a directed graph that maps out your family relationships.

Built with **Streamlit**, **pandas**, and **NetworkX**, the app is lightweight and deployable on platforms like **AWS EC2**, **Streamlit Cloud**, or any server with Python support.

Check out the live website: [famgen.streamlit.app](https://famgen.streamlit.app/)

---

## ✨ Features

- 📄 Upload `.csv` or `.xlsx` files
- 👪 Automatically builds a family tree from `Parent` → `Child` data
- 🌐 Web-based UI built with Streamlit
- 🧠 Error handling for invalid files or formats
- ⚡ Fast rendering, even for moderately large trees

---

## 🗂️ File Format

Your file should look like this:

<img width="718" height="181" alt="Screenshot 2025-07-21 at 11 39 06" src="https://github.com/user-attachments/assets/8bd27c7a-9f53-4a12-9818-6ecae7217187" />

Here is the downoadable version of the file: [Example File](https://github.com/KshitijKhandelwal-Github/FamGen/blob/main/ftexample.xlsx)

- ID - The first 2 letters of the first name and last name combined
- Sex - The gender of the person
- First Name / Last Name - the first and last name of the person
- DoB - Date of birth in DDMMYY format
- DoD - Date of death in DDMMYY format
- FatherID - ID or Father (if any)
- MotherID - ID of Mother (if any)
- SpouseID - ID of Spouse (if any)
- Place of Birth - Place of birth of person
- Job - Job of the person (optional)
