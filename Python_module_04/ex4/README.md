# Handling Errors (Exceptions)

This document explains the types of errors (Exceptions) used in the code and how to handle them.

## 1. FileNotFoundError
* **What is it?** This error happens when you try to `open()` a file that does not exist in the current folder.
* **How we handle it:** Instead of letting the program crash, we catch this specific error and print "Archive not found".

## 2. PermissionError
* **What is it?** This error happens when the file exists, but the operating system tells Python: "You are not allowed to read this."
    * *Example:* Trying to open a system file or a file locked by an administrator.
* **How we handle it:** We catch this error and print "Security protocols deny access".

## 3. The `try` / `except` Block
This is the "Safety Net" logic:

* **`try:`** Run the code inside here. If everything is fine, skip the `except` blocks.
* **`except ErrorName:`** If `ErrorName` happens inside the `try`, stop immediately, jump here, run this code, and then continue the program normally (don't crash).

## 4. How to Test This?
Since we are not allowed to use `os` to create the files automatically:

1.  **For `standard_archive.txt`:** Create a file manually with some text inside.
2.  **For `lost_archive.txt`:** Ensure this file does **not** exist.
3.  **For `classified_vault.txt`:** Create a file manually.
    * *To test PermissionError:* You must manually change the file permissions in your Operating System to "Read Only" or "No Access" for your user.