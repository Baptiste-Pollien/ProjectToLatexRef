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
        match = "\"^[ ]*{}\"".format(name)
    else:
        match = "^[ ]*{}[ ]*{}".format(definition['keyword'], name)

    if 'file_type' not in definition:
        cmd=["grep", "-r", "-n", match,ppath]
    else:
        cmd=["grep", "-r", "-n", "--include", \
             "{}".format(definition['file_type']), match,ppath]

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, error = process.communicate()

    if name not in str(output):
        print("[Error] The definition {} was not found...".format(name))
        exit(1)

    res = str(output).replace("b\"", '')\
                     .replace("b\'", '')\
                     .split("\\n")

    if len(res) <= 1:
        print("[Error] {} not found...\n".format(name))
        print(error)
        exit(1)

    if len(res) > 2 and ('file' not in definition):
        print("[Warning] Multiple definition of {}. You should use the field \'file\'.".format(name))

    if (len(res) == 2) or ('file' not in definition):
        res = res[0].replace(ppath, '')\
                 .split(":")
    else:
        file = definition['file']
        found = False

        for el in res:
            if file in el:
                found = True
                res = el.replace(ppath, '')\
                        .split(":")
                break
        
        if not found:
            print("[Error] {} not found...\n".format(name))
            exit(1)
        

    path = res[0]
    line = res[1]

    url = data['base_url'] + path +"\\#L" + line

    # Fix Latex Code
    name = name.replace("_", "\\_")
    path = path.replace("_", "\\_")

    # Generation of the Latex code
    return "\\newcommand\\{}{{{}{{{}}}{{{}}}{{{}}}}}\n\n"\
            .format(lcmd, def_cite(), url, name, path + ":" + line)

def analyse_definitons(file, data):
    """
    Function that analyse all the definition of the file
    """
    for d in data['definitions']:
        file.write(analyse_definition(data, d))
