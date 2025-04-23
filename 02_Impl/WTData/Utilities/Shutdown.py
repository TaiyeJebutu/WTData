# Standard

# External

# Local


class Shutdown:
    """ Class for cooperative shutting down"""

    SHUTDOWN = False

    @classmethod
    def shutdown(cls):
        cls.SHUTDOWN = True

    @classmethod
    def shutting_down(cls) -> bool:
        return cls.SHUTDOWN

    @classmethod
    def reset_shutdown(cls):
        """Resets the shutdown flag
        only to be used for testing purposes"""
        cls.SHUTDOWN = True
