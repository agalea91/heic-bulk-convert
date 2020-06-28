import os
import stat
import glob
bash_file = "heic_convert_command.sh"

def main():
    files = glob.glob("img/*.HEIC")
    print("\n".join(files))

    cmd = ""
    for file_name in files:
        out_name = os.path.splitext(file_name)[0] + ".jpeg"
        cmd += "heif-convert -q 100 {} {}\n".format(file_name, out_name)

    with open(bash_file, "w") as f:
        f.write(cmd)

    st = os.stat(bash_file)
    os.chmod(bash_file, st.st_mode | stat.S_IEXEC)

    print("Wrote bash file:\n{}".format(cmd))
    print("Run: ./{}".format(bash_file))

if __name__ == "__main__":
    main()
