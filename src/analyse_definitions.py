"""
File containing the function analysis for definitions
"""
import subprocess

def def_cite():
    """
    Latex command name for the definitions
    """
    return "\\defcite"

def analyse_definition(data, definition):
    """
    Function that returns the Latex code for the [definition].
    """
    # Find the file path
    ppath=data['project_path']

    # Command latex
    if 'cmd' not in definition:
        print("[Error] Missing cmd for the definition: {}".format(str(definition)))
        exit(1)
    lcmd = definition['cmd']

    # Matching case
    if 'name' not in definition:
        print("[Error] Missing name for the definition: {}".format(str(definition)))
        exit(1)
    name = definition['name']

    if 'keyword' not in definition:
        match = "\"^{}\"".format(name)
    else:
        match = "^{}.*{}".format(definition['keyword'], name)

    if 'file_type' not in definition:
        cmd=["grep", "-r", "-n", match,ppath]
    else:
        cmd=["grep", "-r", "-n", "--include", \
             "{}".format(definition['file_type']), match,ppath]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, error = process.communicate()

    # Get the first output
    try:
        res = str(output).replace("b\'", '')\
                         .split("\\n")[0]\
                         .replace(ppath, '')\
                         .split(":")
    except:
        print("[Error] {} not found...\n".format(name))
        print(error)
        exit(1)

    path = res[0]
    line = res[1]
    name = name.replace("_", "\\_")

    url = data['base_url'] + path +"\\#L" + line

    # Generation of the Latex code
    return "\\newcommand\\{}{{{}{{{}}}{{{}}}{{{}}}}}\n\n"\
            .format(lcmd, def_cite(), url, name, path + ":" + line)

def analyse_definitons(file, data):
    """
    Function that analyse all the definition of the file
    """
    for d in data['definitions']:
        file.write(analyse_definition(data, d))
