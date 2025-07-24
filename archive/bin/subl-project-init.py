#! /usr/bin/env python3

"""
Author: James Perretta
"""

import os
import argparse


def main():
    args = parse_args()
    project_type = args.project_type.lower().strip()

    if project_type not in project_templates:
        template = generic_template
    else:
        template = project_templates[project_type]

    with open(args.project_name + '.sublime-project', 'w') as project_file:
        project_file.write(template)

    workspace_file = args.project_name + '.sublime-workspace'
    if not os.path.isfile(workspace_file):
        with open(workspace_file, 'w') as f:
            f.write('{}')


def parse_args():
    parser = argparse.ArgumentParser(
        description="Initialize a Sublime Text project.")

    parser.add_argument(
        "--project_type", "-t",
        nargs="?",
        default="default",
        help=("Currently supported values: [{0}]\n"
              "If this value is not specified, a default template will be "
              "used.".format(", ".join(project_templates.keys())))
    )

    parser.add_argument("project_name", help="The name of the project.")

    args = parser.parse_args()
    return args

# -----------------------------------------------------------------------------

c_cpp_template = """{{
    "folders":
    [
        {{
            "path": ".",
            "folder_exclude_patterns": [],
            "file_exclude_patterns": ["*.o", "*.d", "*.orig"]
        }}
    ],

    "tab_size": 2,
    "translate_tabs_to_spaces": true,

    "settings":
    {{
        "sublimegdb_workingdir": "build",
        // NOTE: You MUST provide --interpreter=mi for the plugin to work
        "sublimegdb_commandline": "gdb --interpreter=mi ./executable"
    }},

    "SublimeLinter":
    {{
        "linters": {{
            "clang": {{
                "@disable": false,
                "args": [],
                "excludes": [],
                "extra_flags": "-Wextra -pedantic {language_flag}",
                "include_dirs": [
                    "${{project}}",
                    "/usr/local/include",
                    "/usr/include",
                    "/usr/include/c++/4.8.1",
                    "/usr/include/x86_64-linux-gnu",
                    "/usr/include/x86_64-linux-gnu/c++/4.8.1",
                    "/opt/clang/lib/clang/3.5.0/include"
                ]
            }},
        }}
    }}
}}
"""

generic_template = """{
    "folders":
    [
        {
            "path": ".",
            "folder_exclude_patterns": [],
            "file_exclude_patterns": []
        }
    ],
}
"""

c89_template = c_cpp_template.format(language_flag="--std=c89")
cpp98_template = c_cpp_template.format(language_flag="--std=c++98")
cpp11_template = c_cpp_template.format(language_flag="--std=c++11")

project_templates = {"c++11": cpp11_template, "cpp11": cpp11_template,
                     "cpp98": cpp98_template, "c++98": cpp98_template,
                     "c89": c89_template,
                     "default": generic_template}

if __name__ == '__main__':
    main()

# experimental build system
# blah =  """   "build_systems":
#     [
#         {
#             "name": "Build",
#             "cmd":
#             [
#                 "make",
#                 "-j",
#                 "8"
#             ],
#             "file_regex": "^(..[^:]*):([0-9]+):?([0-9]+)?:? (.*)$",
#             "working_dir": "$project_path",
#             "variants":
#             [
#                 {
#                     "name": "Clean",
#                     "cmd":
#                     [
#                         "make",
#                         "clean"
#                     ]
#                 }
#             ]
#         }
#     ],"""
