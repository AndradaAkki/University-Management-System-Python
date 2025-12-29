# 🎓 University Management System

A robust console-based application for managing university students, disciplines, and grades. This project demonstrates a clean **Layered Architecture**, **Dependency Injection**, and **Polymorphic Data Persistence** (supporting Memory, Text, and Binary storage).

![Python](https://img.shields.io/badge/Language-Python_3.x-blue)
![Architecture](https://img.shields.io/badge/Architecture-Layered_MVC-green)
![Testing](https://img.shields.io/badge/Testing-Unittest-orange)

## 📖 Overview
This application is designed to simulate a university registrar system. It allows administrators to manage student enrollments, curriculum (disciplines), and academic performance (grades).

The core focus of this project was to implement a flexible architecture where the **Storage Strategy** can be swapped without changing the business logic or user interface.

## 🏗️ Architectural Design
The codebase follows a strict **Separation of Concerns** using four layers:

| Layer | Responsibility |
| :--- | :--- |
| **Domain** | Defines core entities (`Student`, `Discipline`, `Grade`) with validation logic. |
| **Repository** | Handles data persistence. Implements a **Strategy Pattern** to support In-Memory, Text File, or Binary (Pickle) storage. |
| **Services** | Contains business logic (e.g., preventing duplicate IDs, calculating averages). It relies on Dependency Injection to receive the Repository. |
| **UI** | A console-based interface that captures user input and displays data. |

## ✨ Key Features
* **CRUD Operations:** Full Create, Read, Update, Delete functionality for Students and Disciplines.
* **Grading System:** Assign grades to students for specific disciplines.
* **Search Engine:** Case-insensitive search for students/disciplines by ID or Name.
* **Data Persistence:**
    * **Memory:** Fast, non-persistent storage for testing.
    * **Text File:** Human-readable storage (`.txt`).
    * **Binary:** Efficient serialization using Python `pickle`.
* **Unit Testing:** Comprehensive test suite (`src/ui/testFile.py`) ensuring logic reliability.

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **Libraries:** `pickle` (Serialization), `unittest` (Testing), `numpy` (Random generation).
* **Concepts:** OOP, Layered Architecture, Exception Handling.

## 🚀 How to Run

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YourUsername/University-Management-System.git](https://github.com/YourUsername/University-Management-System.git)
    cd University-Management-System
    ```

2.  **Configure Storage**
    Open `src/ui/UI.py` (bottom of file) and uncomment the repository type you wish to use:
    ```python
    # For Text File Storage:
    # stud_repo = StudentTextFileRepository("student.txt")

    # For Binary Storage (Default):
    stud_repo = StudentBinaryFileRepository("student.pickle")
    ```

3.  **Run the App**
    ```bash
    python -m src.ui.UI
    ```

4.  **Run Tests**
    ```bash
    python -m src.ui.testFile
    ```

## 📂 Project Structure
```text
src/
├── domain/         # Entity classes (Student, Discipline, Grade)
├── repository/     # Storage logic (Memory, Text, Binary)
├── services/       # Business logic (Controllers)
└── ui/             # Console Interface and Unit Tests
