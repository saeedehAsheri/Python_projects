# 🐍 Python Errors: Guid

In programming, things go wrong. Files go missing, users type text instead of numbers, and servers go offline. **Error Handling** is how we stop our programs from crashing when these things happen.

## 1. Types of Errors

There are generally two main categories of errors in Python:

### ❌ Syntax Errors
These are grammar mistakes. Python doesn't understand what you wrote.
* *Example:* Forgetting a colon `:` at the end of an `if` statement.
* *Result:* The program **never starts**.

### 💥 Exceptions (Runtime Errors)
These happen while the program is running. The syntax is correct, but something illegal occurred.
* **`ValueError`**: The data is the right type but wrong value (e.g., trying to turn "abc" into a number).
* **`TypeError`**: Doing math with strings (e.g., `"cat" + 5`).
* **`ZeroDivisionError`**: Trying to divide by zero.
* **`FileNotFoundError`**: Trying to open a file that doesn't exist.

---

## 2. The Tools: try, except, finally, & raise

Think of error handling like a **Fire Drill**.

### 🟢 `try`
"Try to do this dangerous thing."
* This is where you put the code that *might* crash.

### 🔴 `except`
"If a fire starts, do this!"
* This block only runs if an error happens in the `try` block. It catches the error so the program doesn't crash.

### 🔵 `finally`
"No matter what happens, do this at the end."
* This runs **always**, whether there was an error or not. It is used for cleanup (like closing files or turning off water).

### 📢 `raise` (Not "rain"!)
"I am starting a fire drill manually!"
* Sometimes Python thinks everything is fine, but you know it's not. You use `raise` to force an error to happen intentionally.

---

## 3. How to Use Them (The Pattern)

The logic flows like this:

1.  **Attempt** the code in `try`.
2.  **If successful:** Skip `except`, run `else` (optional), then run `finally`.
3.  **If failed:** Stop immediately, jump to `except`, then run `finally`.



---

## 4. Complete Example

Here is a simple "Garden Water Tank" program that uses all these concepts.

```python
def fill_water_tank(liters):
    try:
        # 1. THE DANGEROUS PART
        print(f"Attempting to add {liters} liters...")
        
        # Check for invalid input types
        if not isinstance(liters, int):
            raise TypeError("Liters must be a whole number!")
            
        # Check for impossible values (Manual Error)
        if liters < 0:
            raise ValueError("You cannot add negative water!")

        # Simulating a calculation error
        result = 100 / liters
        print(f"Tank filled! Efficiency calculated: {result}")

    except TypeError as e:
        # 2. CATCHING SPECIFIC ERRORS
        print(f"❌ Type Error caught: {e}")

    except ValueError as e:
        print(f"❌ Value Error caught: {e}")

    except ZeroDivisionError:
        print("❌ Error: You cannot divide by zero (0 liters)!")

    except Exception as e:
        # Catch-all for any other unknown errors
        print(f"❌ Unknown error: {e}")

    finally:
        # 3. CLEANUP (Always runs)
        print("🔄 Closing the water valve safely.\n")

# --- Testing the Example ---

fill_water_tank(50)      # Works perfect
fill_water_tank(-10)     # Raises ValueError
fill_water_tank("five")  # Raises TypeError
fill_water_tank(0)       # Raises ZeroDivisionError