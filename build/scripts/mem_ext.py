from glob import glob
from invoke.exceptions import Exit
import struct
import os.path

def apply(c, zip_fn_pattern):
    print("Enabling extended memory limit for Windows.")

    zip_file = glob(os.path.join(c.build.output, zip_fn_pattern))
    if len(zip_file) != 1:
        raise Exit("No matching packages found in output folder: {}".format(c.build.output), 1)

    zip_file = os.path.relpath(zip_file[0], c.cwd)

    main_exe = None
    result = c.run("zipinfo -1 '{}'".format(zip_file), hide=True)
    for r in result.stdout.splitlines():
        if len(r.split("/")) == 2 and r.endswith(".exe"):
            main_exe = os.path.basename(r)
            break

    if not main_exe:
        raise Exit("Main game executable not found in package: {}".format(zip_file), 1)

    target_match = ["/{}".format(main_exe), "/pythonw.exe"]
    target_files = []
    for r in result.stdout.splitlines():
        if any([r.endswith(x) for x in target_match]):
            target_files.append(r)

    tmp_dir = os.path.join(c.build.cache, "mem_ext")
    target_files_args = ' '.join(["'{}'".format(x) for x in target_files])

    c.run("mkdir -p {}".format(tmp_dir))
    c.run("unzip -qo '{}' {} -d '{}'".format(
        zip_file,
        target_files_args,
        tmp_dir
    ))

    for fn in target_files:
        tmp_fn = os.path.join(tmp_dir, fn)
        set_large_address_aware(tmp_fn, fn)

    print("Updating: {}".format(zip_file))
    with c.cd(tmp_dir):
        relpath = os.path.relpath(zip_file, tmp_dir)
        c.run("zip '{}' {}".format(relpath, target_files_args), hide=True)

    c.run("rm -rf '{}'".format(tmp_dir))


def set_large_address_aware(filename, info=None):
    # See http://en.wikibooks.org/wiki/X86_Disassembly/Windows_Executable_Files#PE_Header
    # and https://msdn.microsoft.com/en-us/library/ms680349%28v=vs.85%29.aspx
    IMAGE_FILE_LARGE_ADDRESS_AWARE = 0x0020
    PE_HEADER_OFFSET = 60
    CHARACTERISTICS_OFFSET = 18

    info = info or filename

    with open(filename, 'rb+') as f:
        if f.read(2) != b'MZ':
            print('MZ header was not found: {}'.format(info))
            return

        # Get PE header location
        f.seek(PE_HEADER_OFFSET)
        pe_loc, = struct.unpack('i', f.read(4))
        f.seek(pe_loc)
        if f.read(4) != b'PE\0\0':
            print('Error in PE header: {}'.format(info))
            return

        # Get Characteristics
        char_loc = pe_loc + 4 + CHARACTERISTICS_OFFSET
        f.seek(char_loc)
        bits, = struct.unpack('h', f.read(2))

        # Check if bit flag is set
        if (bits & IMAGE_FILE_LARGE_ADDRESS_AWARE) != IMAGE_FILE_LARGE_ADDRESS_AWARE:
            print('Setting LAA flag: {}'.format(info))
            f.seek(char_loc)
            bytes = struct.pack('h', (bits | IMAGE_FILE_LARGE_ADDRESS_AWARE))
            f.write(bytes)
            return

        print('Found LAA flag: {}'.format(info))
