# ProjectToLatexRef

Python script that converts a list of references of functions or
definitions and generates the references in Latex.

## Using the project

The project can be used with the following command:

```[bash]
python3 projectToLatexRef.py [configuration file]
```

The content of the configuration file is described later.

## Example

The folder `example` is an example of a project using
`ProjectToLatexRef`. This folder contains the following:

- `project_refs.json`: The configuration file of this project
- `run_example.sh`: A script that will launch `ProjectToLatexRef` and then
  build the latex example using `latexmk`.
- `code_ref.tex`: The Latex file produced by `ProjectToLatexRef`.
- `main.tex`: A short example of Latex file that uses the references.
- `src`: The source code of the project.

## Configuration file

The configuration file is a JSON file that contains all the information
needed to build the Latex references. You can look at
`example/project_refs.json` an example of a configuration file and
`example/code_ref.tex` the file generated. Here is a description of the required field:

- `base_url`: The URL of the GitHub project that will be appended to the
  beginning the relative path found.
- `project_path`: Path of the project where the (it must corresponds the
  folder of the clone of the URL).
- `output_file`: The output Latex file containing the references.
- `function_code`: The Latex code for the functions. The code can use 3
  parameters (the url, the name, and the path of the file in the project).
- `files`: The list of files to analyse.

    * `name`: The name of the file to search.
    * `cmd`: The name of the Latex command of the file referenced.

- `def_code`: The Latex code for the definitions. The code can use 3
  parameters (the url of the definition, the name, and the path of the file
  in the project).
- `definitions`: The list of the definitions to search.
    * `name`: The name of the definition to search.
    * `cmd`: The name of the Latex command of the definition referenced.
    * `keyword`: The keyword before the definition. This parameter is
      optinnal.
    * `file_type`: The type of file to search. For example `*.c`, to
      restrict the research to C files.
    * `file`: Specify the name of the file containing the definition. If
      there is multiple definitions, the first found is returned.
    * `href`: boolean value to define if an href should be generated
      (`\href{$url}{\texttt{$name}}`). The name will be `name`++`Href`.
    * `end_parse`: specify a matching string to add after the name. If this
      option is not used, the last matching definition will be taken.

- `disable_macro`: This boolean parameter is optional and disables the
  generation of `\filecite` and `\defcite` commands. It can be useful if
  you want to define this macro externally or if you use this tool for
  multiple projects.