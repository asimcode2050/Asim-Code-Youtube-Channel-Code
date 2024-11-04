import subprocess
def get_startup_programs():
    command = 'wmic startup get caption, command'
    output = subprocess.check_output(
        command, shell=True).decode().strip().splitlines()
    startup_programs = []
    for line in output[1:]:
        if line.strip():
            startup_programs.append(line.strip())
    return startup_programs


def main():
    programs = get_startup_programs()
    print("Startup Programs:")
    for program in programs:
        print(program)


if __name__ == "__main__":
    main()
