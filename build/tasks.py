from invoke import task, call, main
from invoke.exceptions import Exit
from scripts import checks, compression, patch, mem_ext, target_names, version_up
from glob import glob
import os

@task
def run(c, renpy=None):
    """
    Run the project using Ren'Py SDK.
    """
    checks.all(c, [checks.tools])
    install_renpy(c, renpy)
    c.run("renutil -r '{}' launch {} --direct '{}' run".format(
        c.renpy.registry,
        c.renpy.version,
        c.build.project
    ))


@task
def clean(c):
    """
    Clean cached data.
    """
    print("Cleaning build cache: {}".format(c.build.cache))
    c.run("rm -rf {}".format(c.build.cache))
    print("Cleaning bytecode files: *.rpyc, *.pyc")
    c.run("find {} \\( -name '*.rpyc' -o -name '*.pyc' \\) -delete".format(c.build.project))


@task
def check(c, all=False):
    """
    Check the build environment.
    """
    if all:
        checks.all(c)
        print("All systems are go!")
    else:
        checks.check_basic(c)
        print("Build environment is ready!")


@task
def checksum(c):
    """
    Compute checksums for build output.
    """
    print("Computing checksums.")
    with c.cd(c.build.output):
        if c.run("compgen -G '*.zip' || compgen -G '*.apk'", warn=True, hide=True).ok:
            c.run("shopt -s nullglob; sha256sum *.{zip,apk} | tee /dev/tty > checksums.txt; shopt -u nullglob")
        else:
            print("No packages found: {}".format(c.build.output))


@task
def install_renpy(c, version=None):
    """
    Install Ren'Py SDK and RAPT.
    """
    if version:
        c.renpy.version = version

    checks.all(c, [checks.tools])
    if not os.path.exists(os.path.join(c.renpy.registry, c.renpy.version)):
        c.run("renutil -r '{}' install {}".format(
            c.renpy.registry,
            c.renpy.version
        ))
    else:
        print("Ren'Py SDK {} is installed.".format(c.renpy.version))


@task(
    help={
        'target': "Target platform(s). (default: pc, mac, android)",
        'quality': "Compression quality. (default: depends on target)"
    },
    iterable=['target']
)
def compress(c, target=None, quality=None):
    """
    Compress a copy of the project.
    """
    if target:
        c.build.target = target

    if quality:
        c.build.quality = quality

    checks.all(c, [checks.tools])
    compression.compress_all(c)


@task(
    help={
        'target': "Target platform(s). (default: pc, mac, android)"
    },
    iterable=['target'],
    pre=[install_renpy],
    post=[checksum]
)
def build(c, version, target=None):
    """
    Build the project for target platforms.
    """
    c.build.version = version
    if target:
        c.build.target = target

    checks.check_build(c)

    compression.compress_all(c)
    c.run("mkdir -p '{}'".format(c.build.output))
    for t in target:
        if t == 'android':
            c.run("renutil -r '{}' launch '{}' android_build '{}' assembleRelease --destination '{}'".format(
                c.renpy.registry,
                c.renpy.version,
                c.build.targets.android.source or c.build.project,
                c.build.output
            ))
        else:
            c.run("renutil -r '{}' launch '{}' distribute '{}' --destination '{}' {}".format(
                c.renpy.registry,
                c.renpy.version,
                c.build.targets.pc.source or c.build.project,
                c.build.output,
                "--package {}".format(t)
            ))
            if t == 'pc' and c.build.targets.pc.extended_memory:
                mem_ext.apply(c, "*-pc.zip")


@task(
    name='patch',
    help={
        'version': "Release version.",
        'reference': "Reference version. Must be a git tag.",
        # 'target': "Target platform(s). (default: pc)"
    },
    iterable=['target'],
    post=[checksum]
)
def build_patch(c, version, reference=None):
    """
    Build a patch from changes in version control.
    """
    c.build.target = ['pc'] # pc only
    c.build.version = version
    c.build.patch.reference = reference if reference else '.'.join(version.split('.')[:2])
    checks.check_patch(c)
    patch.build_patch(c)


@task(
    help={
        'version': "Updated version.",
        'release': "Set release flag(s) and make a tagged commit on the release branch. (default: no)",
        'push': "Push changes to the remote repository. (default: no)",
    }
)
def update(c, version, release=False, push=False):
    """
    Update the project version.
    """
    c.build.version = version
    checks.check_update(c)

    version_up.update_version_files(c)
    checks.all(c, [checks.version_files])

    # TODO Discuss if we want release commits or not
    if release:
        version_up.set_release_flags(c, True)
        c.run("git commit --all -m 'Update version to {}'".format(version))
        branch = version_up.current_branch(c)
        # Fast-forward merge on release branch, see: https://stackoverflow.com/a/17722977
        c.run("git fetch origin {}:{}".format(branch, c.build.branch))
        c.run("git tag -a -m 'Version {0}' {0}".format(version))
        if push:
            c.run("git push --follow-tags origin {} {}".format(branch, c.build.branch))

    # Release flags should only be True on release commits
    version_up.set_release_flags(c, False)
