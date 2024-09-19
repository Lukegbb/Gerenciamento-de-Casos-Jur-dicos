# Legal Case Management System

This project is a legal case management system developed with Flask and SQLite for data storage. It allows lawyers and legal professionals to add, view, and manage information about legal cases.

## Features

- Add Legal Cases Register new cases with information such as case number, client, status, responsible lawyer, and description.
- Case Listing Displays all registered cases in a table.
- Reports Generates summary reports with case details filtered by status or lawyer.

## Technologies Used

- Python 3.6+
- Flask Web framework for Python.
- SQLite Lightweight database for data storage.
- HTMLCSS For the user interface.

## Project Structure

```plaintext
Legal_Case_Management
│
├── app.py               # Main Flask file
├── models.py            # Data models for legal cases
├── database.py          # Functions for interacting with the SQLite database
├── templates           # Directory for HTML files
│   ├── base.html        # Base layout for the application
│   ├── index.html       # Main page with form and case listing
│   └── report.html      # Reports page
├── static              # Directory for CSS 
│   └── style.css        # Custom CSS file for styling the interface
├── requirements.txt     # List of dependencies
