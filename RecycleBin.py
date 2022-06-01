import os.path as path
import os
import time
import shutil
import schedule
import hashlib


def RemoveDuplicateFiles(Dir_Name=os.getcwd()):
    Unique = {}
    Count = 0
    try:
        if os.path.exists(Dir_Name) or os.path.isdir(Dir_Name):
            Abs_Path = os.path.join(os.getcwd(), Dir_Name)
            for files in os.listdir(Abs_Path):
                File_Name = os.path.join(Abs_Path, files)
                if os.path.isfile(File_Name) and not os.path.isdir(File_Name):
                    Count += 1
                    file_Hash = hashlib.md5(open(File_Name, "rb").read()).hexdigest()
                    if file_Hash not in Unique:
                        Unique[file_Hash] = File_Name
                    else:
                        if not os.path.exists(os.path.join(os.getcwd(), "RecycleBin")):
                            os.mkdir("RecycleBin")
                        else:
                            Rc_File = os.path.join(os.getcwd(), "RecycleBin", File_Name)
                            fd = open(Rc_File, "w")
                            fd.write(" ")
                            fd.close()
                            shutil.move(File_Name, os.path.join(os.getcwd(), "RecycleBin"))
                            print(File_Name.split("\\")[-1], ' successfully moved to Recycle Bin')

    except Exception as obj:
        print("Exception Occurred : ", obj)

    print(f"Total {Count} Files Scanned\n")


def CheckFiles(days=30):
    iCnt = 0
    FoundFiles = 0
    Absolute_Path = os.path.join(os.getcwd(), "RecycleBin")
    if os.path.exists(Absolute_Path):
        for file in os.listdir(Absolute_Path):
            iCnt += 1
            file = os.path.join(Absolute_Path, file)
            file_time = path.getmtime(file)
            val = (time.time() - file_time) / 3600 > 24 * days
            if val:
                FoundFiles += 1
                os.remove(file)
                print(file.split("\\")[-1], ' File Successfully Deleted')

        print(f"Total {iCnt} files Scanned from Recycle Bin")
        print(f"Total {FoundFiles} files Found Which is older than 30 days "
              f"and get deleted")


def main():
    try:
        schedule.every(10).hours.do(RemoveDuplicateFiles)
        schedule.every(1).hours.do(CheckFiles)

    except Exception as Err:
        print("Exception Occurred : ", Err)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
