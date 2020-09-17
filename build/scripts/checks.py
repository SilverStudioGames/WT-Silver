from invoke.exceptions import Exit
from scripts import target_names, version_up
import os.path

def all(c, checks=None, force=False):
    if checks is None:
        checks = [
            tools, jdk, rapt, target,
            git, git_branch, git_clean, git_patch,
            version_valid, version_files,
        ]

    ok = True
    for check in checks:
        ok &= check(c)

    if not (ok or force):
        raise Exit(code=1)

    return ok


def check_basic(c, force=False):
    return all(c, [tools, git, jdk], force)


def check_patch(c, force=False):
    return all(c, [tools, target, git, git_clean, git_branch, git_patch, version_valid, version_files], force)


def check_build(c, force=False):
    return all(c, [tools, target, git, git_clean, git_branch, version_valid, version_files]
        + ([jdk, rapt] if 'android' in c.build.target else []), force)


def check_update(c, force=False):
    return all(c, [tools, git, git_clean, version_valid, version_tag], force)


def tools(c):
    missing = []
    for tool in "renutil cwebp git zip rsync sha256sum".split():
        result = c.run("command -v {}".format(tool), hide=True, warn=True)
        if not result.ok:
            missing.append(tool)

    if missing:
        print("Some tools were not found: {}".format(", ".join(missing)))
        return False

    return True


def jdk(c):
    java = None
    java_home = os.getenv("JAVA_HOME")
    if java_home and os.path.isfile(os.path.join(java_home, "/bin/java")):
        java = os.path.join(java_home, "/bin/java")
    elif c.run("command -v java", hide=True, warn=True).ok:
        java = "java"

    if java:
        result = c.run("{} -version".format(java), hide=True)
        version = result.stderr.splitlines()[0].split('"')[1]
        if not version.startswith("1.8."):
            java = None

    if not java:
        print("JDK8 java was not found.")
        return False

    return True


def rapt(c):
    android_json = os.path.join(c.build.project, ".android.json")
    if not os.path.isfile(android_json):
        print("RAPT configuration file was not found: {}".format(android_json))
        return False

    return True


def version_valid(c):
    version = c.build.version
    if not version or not version_up.is_valid(version):
        print("Invalid version: {}".format(version))
        return False

    ref = c.build.patch.reference
    if ref and tuple(map(int, ref.split('.'))) >= tuple(map(int, version.split('.'))):
        print("Reference version is higher than build version.")
        return False

    return True


def version_files(c):
    failed = False
    version = c.build.version
    if version:
        numeric_version = version_up.numeric_version(version)
        for fn, *patterns in c.build.version_files:
            fn = os.path.join(c.build.project, fn)
            if not os.path.isfile(fn):
                failed = True
                print("Version file was not found: {}".format(fn))
                continue

            with open(fn) as f:
                text = f.read()
                for p in patterns:
                    setting = p.format(version=version, code=numeric_version)
                    if setting not in text:
                        failed = True
                        print("Version was not set: `{}` {}".format(setting, fn))

        if failed:
            print("Use `inv update {}` to update the version files.".format(version))

    return not failed


def version_tag(c):
    version = c.build.version
    c.run("git fetch --tags")
    result = c.run("git rev-parse -q --verify '{}'".format(version), hide=True, warn=True)
    if result.ok:
        print("Version tag already exists: {}".format(version))
        return False

    return True


def git(c):
    # Check project is git repository
    git_dir = os.path.join(c.build.project, ".git")
    if not os.path.isdir(git_dir):
        print("Project is not under version control.")
        return False

    return True


def git_branch(c):
    # Check if current branch is release branch
    if version_up.current_branch(c) != c.build.branch:
        print("Current branch is not {}.".format(c.build.branch))
        # return False

    return True


def git_clean(c):
    # Check if there are no uncommitted changes
    result = c.run("git status --porcelain", hide=True, warn=True)
    if result.stdout:
        print("There are uncommitted changes.")
        # return False

    return True


def git_patch(c):
    # Check if patch reference exists
    ref = c.build.patch.reference
    if ref:
        result = c.run("git show-ref '{}'".format(ref), hide=True, warn=True)
        if not result.ok:
            print("Patch reference commit was not found: {}".format(ref))
            return False

    return True


def target(c):
    # Check if targets are defined
    failed = False
    for t in c.build.target:
        if t not in c.build.targets:
            failed = True
            print("Build target is not defined: {}".format(t))

    return not failed
