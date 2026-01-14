try:
        with open(file_path, 'r') as file:
            for line in file:
                line= line.strip()
                if not line:
                    continue
                
                log = json.loads(line)
            set_productivity(log)

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")