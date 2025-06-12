import os
from typing import Any, Iterator


def get_last_file(directory, pattern):
    current = pattern + '000'
    for filename in os.listdir(directory):
        current = max(current, filename)
    return current


class PlayListHandler:
    def __init__(self, config : dict[str, Any]) -> None:
        self._config = config
        self.lastPlst = get_last_file(self._config['playListsPath'], self._config['playListNamePattern'])

    def make_plst(self) -> Iterator[str]:
        dirs_stack = [self._config['rootDir']]
        ignore = self._config['ignore']
        suf = self._config['suf']

        while dirs_stack:
            current = dirs_stack.pop()
            cue_flag = False
            dirs = os.listdir(current)
            if any(i.endswith('.cue') for i in dirs):
                cue_flag = True
            else:
                dirs = sorted(dirs)
            for i in dirs:
                full_path = os.path.join(current, i)
                if os.path.isdir(full_path) and i not in ignore:
                    dirs_stack.append(os.path.join(current, i))
                elif cue_flag and i.endswith('.cue'):
                    yield os.path.join(current, i)
                elif not cue_flag and any(i.endswith(s) for s in suf):
                    yield os.path.join(current, i)

    def upload_plst(self) -> None:
        filename, suf = self.lastPlst.split('.')
        last_idx = str(int(filename[-3:]) + 1)
        last_idx = (3 - len(last_idx)) * '0' + last_idx
        new_plst = os.path.join(self._config['playListsPath'], filename[:-3] + last_idx + '.' + suf)

        plst = sorted([i for i in self.make_plst()], reverse=self._config['reverse']) if self._config['sortedFinal'] else [i for i in self.make_plst()]

        with open(new_plst, 'w') as out:
            out.write('#\n')
            for i in plst:
                out.write(i + '\n')

        self.lastPlst = os.path.basename(new_plst)

    def get_tracks_f_plst(self) -> Iterator[str]:
        with open(f'{self._config['playListsPath']}/{self.lastPlst}', 'r') as playlist:
            for line in playlist:
                line = line[:-1]

                yield line



