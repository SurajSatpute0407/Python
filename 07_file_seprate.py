import os
import sys
import shutil


try:
    print("Copying Files...")
    for i in os.listdir(r"C:\Users\satpu\OneDrive\Pulpit\Test"):
        filename = r"C:\Users\satpu\OneDrive\Pulpit\Test\\" + i
        file_size = os.stat(filename).st_size / 1000
        # print(f'{i:<25} {file_size}')

        if 0.00 <= file_size <= 1.000:
            shutil.copy(
                filename, r"C:\Users\satpu\OneDrive\Pulpit\File_handling\Less_Than_1KB"
            )
        elif 1.000 < file_size < 5.000:
            shutil.copy(
                filename, r"C:\Users\satpu\OneDrive\Pulpit\File_handling\Less_Than_5KB"
            )
        elif file_size >= 5.000:
            shutil.copy(
                filename, r"C:\Users\satpu\OneDrive\Pulpit\File_handling\More_Than_5KB"
            )

    print("Files Copied Successfully!")

except Exception as e:
    print(f"Something Went Wrong! Error: {e}")
