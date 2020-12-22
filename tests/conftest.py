from pyannotate_runtime import collect_types


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    collect_types.init_types_collection()
    collect_types.start()


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    collect_types.stop()
    collect_types.dump_stats("annotations")


def pytest_unconfigure(config):
    """
    called before test process is exited.
    """
