## 📌 Overview

Renaming over 300+ files manually is time-consuming and prone to errors. This Python script automates the process by renaming letters based on a standardised naming convention.

## 📂 Background

Our company group consists of four separate limited companies, with over 300 company letters dating back to 2019 between all companies. Originally, letters were stored in separate folders for each company:

```
Letters/
  |-- Hurak Learning/
      |-- 2019/
      |-- 2020/
      |-- 2021/
      |-- 2022/
      |-- 2023/
      |-- 2024/
      |-- 2025/
  |-- Hurak Marketplace/
      |-- 2023/
      |-- 2024/
      |-- 2025/
  |-- Securak/
      |-- 2021/
      |-- 2022/
      |-- 2023/
      |-- 2024/
      |-- 2025/
  |-- Tutorak/
      |-- 2021/
      |-- 2022/
      |-- 2023/
      |-- 2024/
      |-- 2025/
```

We wanted to move all letters into a single top-level 'Letters' folder to allow us to quickly see the newest letters based on the 'Date Modified' column. However, we needed to be able to differentiate letters easily based on the company they belonged to. We decided to rename the files with:

- A shorter date format: YYYY.MM.DD → YY.MM.DD
- The company’s initials after the date

### 🔄 Example Filename Transformations

| Company           | Original Filename                   | New Filename                        |
| ----------------- | ----------------------------------- | ----------------------------------- |
| Hurak Learning    | 2025.01.01_HMRC PAYE.pdf            | 25.01.01_HL_HMRC PAYE.pdf           |
| Hurak Marketplace | 2025.01.10_HMRC Employer Ref.pdf    | 25.01.10_HMP_HMRC Employer Ref.pdf  |
| Securak           | 2025.01.15_HMRC Corporation Tax.pdf | 25.01.15_S_HMRC Corporation Tax.pdf |
| Tutorak           | 2025.01.20_HMRC Tax Code.pdf        | 25.01.20_T_HMRC Tax Code.pdf        |

## ⚙️ How the Script Works

The Python script automates this renaming process in two steps:

1️⃣ Format the Date:

- Extracts the date from the filename.
- Converts the format from YYYY.MM.DD to YY.MM.DD.
- If the day is missing (e.g., YYYY.MM), it defaults to 01 as the day.
- Renames the file accordingly.

2️⃣ Add Company Initials

- Extracts the modified date from the filename.
- Appends the company initials (HL, HMP, T or S) after the date.
- Renames the file with the new format.

## 🚀 How to Use

1️⃣ Setup

Ensure you have Python3 installed on your machine. Then, clone this repository:

```
git clone https://github.com/adil-rahman1/bulk-rename-files.git
cd bulk-rename-files
```

2️⃣ Run the Script

Execute the script with:

```
python3 main.py
```

You will be prompted to enter:

- The name of the directory that contains the files to be renamed.
- The company initials that should be appended to each file name after the date.

Notes:

- The directory containing the files to be renamed should be stored in the same directory as main.py and must not contain any subdirectories.
- Each directory that contains the files to be renamed should belong to only one company.

Run the script as many times as the number of folders where files need to be renamed.

3️⃣ Verify the Changes

After running the script, check the specified directory to ensure files have been renamed correctly.

## 📂 Example Directory Structure

Below is an example of how your project directory should be structured:

```
bulk-rename-files/
  |-- main.py
  |-- README.md
  |-- Hurak_Learning_Letters/
  |-- Hurak_Marketplace_Letters/
  |-- Securak_Letters/
  |-- Tutorak_Letters/
```
