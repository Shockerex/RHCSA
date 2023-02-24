import subprocess
df_output = subprocess.check_output(["df", "-h"])

df_lines = df_output.decode("utf-8").strip().split("\n")

for line in df_lines[1:]:
    fields = line.split()

    if fields[5].endswith("tmpfs"):
        continue

    use_percent = int(fields[4].rstrip("%"))

    if use_percent > 90:
        print(f"{fields[0]} is over 90% used ({fields[4]})")
    else:
        print("OK")



