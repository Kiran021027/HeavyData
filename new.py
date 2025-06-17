def generate_large_python_file(filename, target_size_mb=24):
    size_in_bytes = target_size_mb * 1024 * 1024
    with open(filename, "w") as f:
        f.write("data = [\n")
        current_size = f.tell()
        i = 0
        while current_size < size_in_bytes:
            line = f"    'item_{i}',\n"
            f.write(line)
            current_size += len(line)
            i += 1
        f.write("]\n")
    print(f"{filename} created with size ~{current_size / (1024*1024):.2f} MB and {i} items")

# Generate a file ~24MB
generate_large_python_file("large_data_24mb.py")
