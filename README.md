## Duplicate File Detector



This Python script utilizes the Tkinter library for GUI-based file selection, hashlib for generating file hashes, and pandas for handling and saving the results. The script identifies duplicate files within a selected directory and saves the outcomes in two separate CSV files: duplicated_file.csv containing information about duplicate files and hashid_file.csv containing file names and their corresponding hash IDs.

## How it works

1. The script defines a class DetectDuplicate with methods to select files, calculate hash IDs, identify duplicates, and save the results.
2. The select_file method prompts the user to select a folder, walks through the directory, calculates the hash ID for each file, and identifies duplicate files.
3. The save_outcome method saves the results in a CSV file.
4. The run_code method executes the file selection and outcome saving processes.