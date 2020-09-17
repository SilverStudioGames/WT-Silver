from glob import glob
from invoke.exceptions import Exit
from scripts import target_names, patch
import os.path
import progressbar


def compress_all(c, patch=False):
    for target in c.build.target:
        compress(c, target, patch)


def compress(c, target, patch=False):
    target_name = target_names.get(target, target)

    quality = c.build.targets[target].quality or c.build.quality
    if quality == 100 or not quality:
        print("Compression is not needed for {}.".format(target_name))
        return

    if patch:
        print("Compressing patch at {}% quality for {}.".format(quality, target_name))
        source_path = patch.patch_source(c)
        cache_path = os.path.join(c.build.cache, "compress-patch", target)
        c.build.targets[target].patch = cache_path
    else:
        print("Compressing project at {}% quality for {}.".format(quality, target_name))
        source_path = c.build.targets[target].source or c.build.project
        cache_path = os.path.join(c.build.cache, "compress-project", target)
        c.build.targets[target].source = cache_path

    if os.path.exists(cache_path):
        pass
    else:
        c.run("mkdir -p '{}'".format(cache_path))

    excludes = ["build", ".git", "game/cache", "game/saves", "*.webp"]
    exclude_args = " ".join(["--exclude '{}'".format(x) for x in excludes])
    c.run("rsync -r {} '{}' '{}'".format(exclude_args, source_path, cache_path))

    pattern = os.path.join(source_path, "**/*.webp")
    webp_files = [(x, os.path.join(cache_path, os.path.relpath(x, source_path))) for x in glob(pattern, recursive=True)]

    # TODO If in patch mode, only compress changed webp files

    total_size = sum(map(os.path.getsize, webp_files))
    size = 0
    bar = progressbar.ProgressBar(max_value=total_size, redirect_stdout=True)
    for fn in webp_files:
        s = os.path.getsize(fn)
        size += s

        # Skip empty webp files in patch mode
        if patch and s == 0:
            continue

        c.run("cwebp -quiet -mt -q {} '{}' -o '{}'".format(quality, *fn))
        bar.update(size)
