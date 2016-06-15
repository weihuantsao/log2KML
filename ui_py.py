import subprocess ,  sys  , os

save_data_path = '/logdata/'
save_data_path = sys.path[0] + save_data_path

print 'python txt2kml.py %slog.txt' % save_data_path

cmd = 'python txt2kml.py %slog.txt' % save_data_path
retcode = subprocess.call(cmd ,shell = True)