# Copyright 2018 Datawire. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License

from typing import NamedTuple


class GitInfo(NamedTuple):
    commit: str
    branch: str
    dirty: bool
    description: str


class BuildInfo(NamedTuple):
    version: str
    git: GitInfo


Version = "{{VERSION}}"

Build = BuildInfo(
    version=Version,
    git=GitInfo(
        commit="{{GITCOMMIT}}",
        branch="{{GITBRANCH}}",
        dirty=bool("{{GITDIRTY}}"),
        description="{{GITDESCRIPTION}}",
    )
)

if __name__ == "__main__":
    import sys

    cmd = "--compact"

    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()

    if (cmd == '--version') or (cmd == '-V'):
        print(Version)
    elif cmd == '--desc':
        print(Build.git.description)
    elif cmd == '--branch':
        print(Build.git.branch)
    elif cmd == '--commit':
        print(Build.git.commit)
    elif cmd == '--dirty':
        print(Build.git.dirty)
    elif cmd == '--all':
        print("version:         %s" % Version)
        print("git.branch:      %s" % Build.git.branch)
        print("git.commit:      %s" % Build.git.commit)
        print("git.dirty:       %s" % Build.git.dirty)
        print("git.description: %s" % Build.git.description)
    else:   # compact
        print("%s (%s at %s on %s%s)" %
              (Version, Build.git.description, Build.git.commit, Build.git.branch,
               " - dirty" if Build.git.dirty else ""))
