import argparse
import os
import shutil
import venv
import subprocess


def main():
    args = parse_args()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    proj_settings_dir = os.path.join(args.project_name, '.vscode')
    os.makedirs(proj_settings_dir, exist_ok=True)

    shutil.copy2(os.path.join(script_dir, 'python_settings.json'),
                 os.path.join(proj_settings_dir, 'settings.json'))
    shutil.copy2(os.path.join(script_dir, '..', 'my.editorconfig'),
                 os.path.join(args.project_name, '.editorconfig'))

    venv.create(os.path.join(args.project_name, 'venv'), with_pip=True)

    os.chdir(args.project_name)
    subprocess.run(['bash', os.path.join(script_dir, 'install_py_tools.bash')])


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('project_name')

    return parser.parse_args()


if __name__ == '__main__':
    main()
