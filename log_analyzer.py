
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

    