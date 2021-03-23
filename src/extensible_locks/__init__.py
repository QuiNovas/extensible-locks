from threading import Lock as _Lock, RLock as _RLock


class Lock(object):
    def __init__(self):
        self.__lock = _Lock()

    def __enter__(self):
        return self.__lock.__enter__()

    def __exit__(self, *args):
        return self.__lock.__exit__(*args)

    def __repr__(self):
        return self.__lock.__repr__()

    def acquire(self, *args):
        self.__lock.acquire(*args)

    def release(self):
        self.__lock.release()

    def locked(self):
        return self.__lock.locked()


class RLock(object):
    def __init__(self):
        self.__lock = _RLock()

    def __enter__(self):
        return self.__lock.__enter__()

    def __exit__(self, *args):
        return self.__lock.__exit__(*args)

    def __repr__(self):
        return self.__lock.__repr__()

    def acquire(self, *args):
        self.__lock.acquire(*args)

    def release(self):
        self.__lock.release()


__all__ = ["Lock", "RLock"]
