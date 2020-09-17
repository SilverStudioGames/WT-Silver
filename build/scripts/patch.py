from scripts import compression
from fnmatch import fnmatch
import os.path
import progressbar
import re


def patch_source(c):
    return os.path.join(c.build.cache, "patch")


def build_patch(c):
    ref = c.build.patch.reference
    version = c.build.version
    print("Building a patch from {} to {}".format(ref, version))

    updated = exclude_files(c, get_updated_files(c, ref))
    deleted = exclude_files(c, get_deleted_files(c, ref))

    bar = progressbar.ProgressBar(max_value=len(updated)+len(deleted), redirect_stdout=True)

    print("Preparing files.")

    patch_dir = patch_source(c)
    c.run("rm -rf '{}'".format(patch_dir))
    c.run("mkdir -p '{}'".format(patch_dir))

    # Copy updated files
    for fn in updated:
        source_fn = os.path.join(c.build.project, fn)
        target_dir = os.path.dirname(os.path.join(patch_dir, fn))
        c.run("mkdir -p '{0}' && cp '{1}' '{0}'".format(target_dir, source_fn))

        bar.update(bar.value + 1)

    # Make empty deleted files
    for fn in deleted:
        target_fn = os.path.join(patch_dir, fn)
        target_dir = os.path.dirname(target_fn)
        c.run("mkdir -p '{0}' && touch '{1}'".format(target_dir, target_fn))

        # Clear obsolete rpyc files
        if target_fn.endswith('.rpy'):
            c.run("touch '{}c'".format(target_fn))

        bar.update(bar.value + 1)

    bar.finish()

    # Compress patch if needed for target
    compression.compress_all(c, patch=True)

    for target in c.build.target:
        patch_dir = c.build.targets[target].source or patch_source(c)
        output_dir = c.build.output

        # Create patch zip
        c.run("mkdir -p '{}'".format(patch_dir))
        c.run("mkdir -p '{}'".format(output_dir))
        target_fn = os.path.join(output_dir, c.build.patch.filename.format(reference=ref, version=version, target=target))
        with c.cd(patch_dir):
            relpath = os.path.relpath(target_fn, patch_dir)
            c.run("zip -r '{}' ./".format(relpath), hide=True)


def get_updated_files(c, ref):
    with c.cd(c.build.project):
        result = c.run("git diff --name-only --diff-filter=ACMR '{}'".format(ref), hide=True)
        return result.stdout.splitlines()


def get_deleted_files(c, ref):
    with c.cd(c.build.project):
        result = c.run("git diff --name-only --diff-filter=D '{}'".format(ref), hide=True)
        files = result.stdout.splitlines()

        # Old filenames from renames
        result = c.run("git diff --stat --diff-filter=R '{}'".format(ref), hide=True)
        pattern = r"\{(.*) => .*\}"
        for line in result.stdout.splitlines():
            ps = line.rsplit('|', 1)
            if len(ps) == 2:
                fn = re.sub(pattern, '\\1', ps[0]).strip(" '\"")
                files.append(fn)

        return files

def exclude_files(c, files):
    for p in c.build.exclude:
        files = [n for n in files if not fnmatch(n, p)]

    return files
