import pstats
import os


with open(os.environ['INSTALL_DIR'] + 'PEF/profiling/stats-login.txt', 'w') as stream:
    stats = pstats.Stats(os.environ['INSTALL_DIR'] + 'PEF/profiling/test-login.txt', stream=stream)
    stats.strip_dirs()
    stats.sort_stats('cumulative', 'time', 'calls')
    stats.print_stats(0.2, 'app.py|Repo.py|Handler.py|Service.py')

    # (r"/([a-zA-Z0-9]+)/menu/?", MenuHandler),
    