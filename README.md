# Time-Decimal Converter

This project consists of a Python script that provides functionality for converting time to decimal format and vice versa. It includes a main script for the conversion, and an additional script for testing the conversion accuracy.

## Features

- **Time to Decimal Conversion**: Converts standard time format (e.g., 08:00 AM) into a decimal format.
- **Decimal to Time Conversion**: Converts decimal time format back into standard time format.
- **Automated Testing**: A script to run the main script repeatedly and ensure the accuracy of conversions.

## Using as Imported Libraries

These scripts can also be used as imported libraries in other Python projects. This allows you to leverage the time-decimal conversion functionality within different Python applications.
<details>
<summary>More Information</summary>
<br>


### Importing the Libraries

1. **Import `TimeToDec` from `main.py`:**
   This function converts standard time format to decimal format.
   ```python
   from main import TimeToDec
   from py2 import decToTime

Using TimeToDec Function:

```python
timeInput = "09:30AM"
decimalResult = TimeToDec(timeInput)
print(f"Converted Decimal Time: {decimalResult}")
```
Using decToTime Function:

```python
decInput = "15.5"
timeResult = decToTime(decInput)
print(f"Converted Standard Time: {timeResult}")
```
You can integrate these functions in a scheduling application to convert event times into decimal format for easier calculation of durations, or in any application where time format conversion is needed.

Ensure that the scripts are in your Python project's path or properly installed as packages if you have packaged them.
The functions expect specific input formats (standard time format for TimeToDec and decimal format for decToTime), so validate inputs accordingly in your application.
</details>

## How to Use

1. **Running the Conversion:**
   - Run the main script.
   - Choose the conversion type (Time to Decimal or Decimal to Time).
   - Input the time or decimal value as instructed.
   - The script will output the converted value.

2. **Automated Testing:**
   - Set the path to the main script and the number of runs in the testing script.
   - The script will execute the main script repeatedly and calculate the success rate of conversions.

## Components

- `main.py`: Contains the `TimeToDec` function for converting time to decimal.
- `py2.py`: Contains the `decToTime` function for converting decimal to time.
- `test_script.py`: Contains the functionality to test the conversion methods for accuracy.

## Requirements

- Python 3.x
- `math` and `re` Python modules for mathematical and regex operations, respectively.
- `subprocess` module for running the script for automated testing.

## Examples

1. **Time to Decimal Conversion:**
```python
   timeInput = "08:00AM"
   decimalResult = TimeToDec(timeInput)
   print(f"TIME TO DECIMAL: {decimalResult}")
``` 
2. **Decimal to Time Conversion:**
```python
  decInput = "12.5"
  timeResult = decToTime(decInput)
  print(f"DECIMAL TO TIME: {timeResult}")
```
### Testing
The automated testing script ensures the conversion accuracy by comparing the output of multiple runs.
Adjust the script_path and num_runs in the testing script as needed.

### Notes
Ensure the input format is correct for the conversions to work properly.
The testing script is intended to validate the reliability of conversion functions.


