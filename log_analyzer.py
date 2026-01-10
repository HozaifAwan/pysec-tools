
def analyze_log(file_path):
    error_count = 0
    failed_count = 0
    total_lines = 0

    try:
        with open(file_path, "r") as file:
            for line in file:
                total_lines += 1
                lower = line.lower()
                
                if "error" in lower:
                    error_count += 1
                if "failed" in lower:
                    failed_count += 1
    
    except FileNotFoundError:
        print("File not found.")
        return
    except PermissionError:
        print("Could not open the file. Permission denied.")
        return
    
    total_lines = len(lines)
    error_count = 0
    failed_count = 0

    for line in lines:
        lower = line.lower()
        if "error" in lower:
            error_count += 1
        if "failed" in lower:
            failed_count += 1
    
    print("Log Analysis Report")
    print("-------------------")
    print("Total Lines: ", total_lines)
    print("Error Lines: ", error_count)
    print("Failures found: ", failed_count)

log_file = input("Enter log file name: ")
analyze_log(log_file)
