## Build tools

Command line tools to make releasing the game easier.

All commands are intended to be run from the build directory.


### Setup

Requirements:
- Linux, WSL, or MacOS
- python
- pipenv
- git
- cwebp
- zip, rsync, sha256sum
- java (JDK8)

`pipenv install` Installs the build environment.

`pipenv run inv check` Checks basic requirements.

Ren'Py and RAPT will be installed automatically when needed.


### Usage

`pipenv shell` Starts a shell in the build environment.

In this environment, `inv`(`oke`) provides some useful build tasks.

`inv -l` Lists available tasks.

`inv -h <task>` Shows help for the given task.

`inv <task>` Runs the given task.


### Examples

In the following examples, `1.10.5` is the new version.

`inv update 1.10.5`

`inv build 1.10.5 -t pc -t mac`

`inv patch 1.10.5`


### Configuration

Task options should normally be passed as command line arguments,
but some settings can only be changed in the configuration file.

Refer to `invoke.yml` for the complete list of settings.

Most settings are best left at their current value, but below are the ones that might have to be changed every now and then:

`renpy.version` Which Ren'Py SDK version is used.

`build.targets.*.quality` Compression quality (if any) for a target platform.

`build.version_files` Which files contain version strings, and the formats of these strings.

`build.patch.file` Format of the patch filename.

### Notes

A version is assumed to be a dot-separated sequence of two or three numbers (e.g. `1.2` or `1.2.3`). Other formats are not compatible.

For Android the version will be converted to a decimal version code where each of the version numbers is represented by two digits
(so `1.2` becomes `10200`, and `1.2.3` becomes `10203`).
This is to make sure the version code is always incremental, while allowing for many version increments.
