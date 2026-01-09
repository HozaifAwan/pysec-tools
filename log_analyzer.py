
def analyze_log(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
    except:
        print("Could not open the file.")
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
