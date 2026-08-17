# Task 5 – Secure File Sharing System

## Project Description

This project is a Secure File Sharing System developed using Python and Flask.

The application allows users to upload files, encrypt them before storing them on the server, and download the files after decrypting them.

## Features

- Upload files through a web interface
- Encrypt uploaded files using Fernet encryption
- Store encrypted files securely on the server
- Download files by entering the filename
- Decrypt files before downloading
- Simple Flask-based web interface

## Technologies Used

- Python
- Flask
- Cryptography (Fernet)
- HTML

## How It Works

### 1. File Upload
The user selects a file and clicks **Upload & Encrypt**.

The application:
- Reads the uploaded file.
- Encrypts the file using Fernet encryption.
- Stores the encrypted data inside the `secure_files` folder.

### 2. File Download
The user enters the filename and clicks **Download**.

The application:
- Finds the encrypted file in the `secure_files` folder.
- Decrypts the file using the encryption key.
- Creates a decrypted copy.
- Sends the decrypted file to the user for download.

## Project Structure

```text
Task_5_Secure_File_Sharing/
│
├── Task5_Report.pdf.docx
├── README.md
└── secure_files_sharing.py
