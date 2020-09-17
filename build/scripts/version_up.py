import json
import os
import re


def update_version_files(c):
    print("Updating version files.")
    version = c.build.version
    code = numeric_version(version)
    for fn, *patterns in c.build.version_files:
        fn = os.path.join(c.build.project, fn)
        if not os.path.isfile(fn):
            print("Version file was not found: {}".format(fn))
            continue

        text = ""
        with open(fn) as f:
            text = f.read()
            for p in patterns:
                text = replace_version(text, p, version, code)

        with open(fn, 'w') as f:
            f.write(text)


def set_release_flags(c, is_release):
    for fn, (on, off) in c.build.release_flags:
        fn = os.path.join(c.build.project, fn)
        if not os.path.isfile(fn):
            print("Release flag file was not found: {}".format(fn))
            continue

        with open(fn) as f:
            old = off if is_release else on
            new = on if is_release else off
            text = f.read()
            text = text.replace(old, new)

        with open(fn, 'w') as f:
            f.write(text)


def numeric_version(version):
    # Numeric version is the multiplied version sequence
    # E.g: 1.2.3 becomes 10203, 1.23.4 becomes 12304, 1.2 becomes 10200
    vs = list(map(int, version.split('.')))
    vs += [0] * (3 - len(vs))
    return vs[0] * 10000 + vs[1] * 100 + vs[2]

    # TODO Consider alternative numeric version, which is maybe more reliable, but less intuitive
    # Numeric version is the number of commits on the release branch
    # return c.run("git rev-list --count --first-parent {}".format(c.build.branch)).stdout


def replace_version(text, pattern, version, code):
    version_string = pattern.format(version=version, code=code)
    r = re.escape(pattern) \
        .replace('\\{version\\}', r'[\d\.]+') \
        .replace('\\{code\\}', r'\d+')
    return re.sub(r, version_string, text)


def current_branch(c):
    return c.run("git branch --show-current", hide=True).stdout.strip()


def is_valid(version):
    return True if re.match(r'^\d\.\d\d?(\.\d)?$', version) else False
