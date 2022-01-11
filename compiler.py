# make a function to install all dependecies from requirements.txt
def pip_install():
    import subprocess
    subprocess.call(['pip3', 'install', '-r', 'requirements.txt'])


def compile():
    import subprocess
    subprocess.call(['pyinstaller', 'app.py', '--onefile'])


def delete_unwanted():
    import os
    unwanted_files_and_directories = ['__pycache__', 'build',
                                      'research', 'app.spec', 'app.py', 'app.spec', 'dist', 'compiler.py', 'requirements.txt']
    for i in unwanted_files_and_directories:
        os.remove(i)


# move all of the files in the dist folder to the parent directory


def move():
    import os
    import shutil
    for i in os.listdir('dist'):
        shutil.move(f'dist/{i}', '.')
    os.rmdir('dist')


def main():
    pip_install()
    compile()
    move()
    delete_unwanted()
    print("Process complete. Compiled the app and deleted all of the unwanted file and folders.")


main()
