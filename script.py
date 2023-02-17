import subprocess

# Run the `df -h` command and capture its output
df_output = subprocess.check_output(["df", "-h"])

# Convert the output to a string and split it into lines
df_lines = df_output.decode("utf-8").strip().split("\n")

# Loop over the lines, skipping the first one (the header)
for line in df_lines[1:]:
    # Split the line into fields
    fields = line.split()

    # Skip any lines that end with "tmpfs" (these are temporary files)
    if fields[5].endswith("tmpfs"):
        continue

    # Extract the percentage used from the "Use%" field
    use_percent = int(fields[4].rstrip("%"))

    # If the percentage used is over 90%, print a message
    if use_percent > 90:
        print(f"{fields[0]} is over 90% used ({fields[4]})")
    else:
        print("OK")
# This script uses the subprocess module to run the df -h command and capture its output. It then processes the output, skipping any lines that end with "tmpfs" (which are temporary files), and checking if any file systems have over 90% usage. If any do, it prints a message indicating which file system is over 90% used. Otherwise, it prints "OK".




