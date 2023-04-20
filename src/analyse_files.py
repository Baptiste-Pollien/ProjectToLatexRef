"""
File containing the function analysis for files
"""
import subprocess

def file_cite():
    return "\\filecite"

def analyse_file_name(data, file_name):
    """
    Analysis of a file
    """

    # Verification of the parameters
    if 'name' not in file_name:
        print("[Error] Missing name for the file: {}".format(str(file_name)))
        exit(1)
    name = file_name['name']

    if 'cmd' not in file_name:
        print("[Error] Missing cmd for the file: {}".format(str(file_name)))
        exit(1)

    # Generation and execution of the Linux command
    ppath=data['project_path']
    cmd="find {} -name {}".format(ppath, name)

    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, _ = process.communicate()

    path=str(output).replace("b\'"+ppath, '')\
                    .replace("b\""+ppath, '')\
                    .replace('\\n\'', '')

    if name not in path:
        print("[Error] The file {} was not found...".format(name))
        exit(1)

    if "\\n" in path:
        print("[Error] Multiple definition of {}...".format(name))
        exit(1)

    url = data['base_url'] + path
    path = path.replace("_", "\\_")
    name = name.replace("_", "\\_")

    # Generation of the Latex code
    return "\\newcommand\\{}{{{}{{{}}}{{{}}}{{{}}}}}\n\n".format(file_name['cmd'], file_cite(), url, name, path)

def analyse_file_names(file, data):
    """
    Analysis of all the file
    """
    for f in data['files']:
        file.write(analyse_file_name(data, f))
