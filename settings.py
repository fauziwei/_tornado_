# coding: utf-8
import os
import errno
import logging.config

basedir = os.path.join(
	os.path.dirname(os.path.realpath(__file__))
)

settings = {
	'debug': False,
}


def getLogDirectory():
	'''Get log directory.

	Will create the directory (recursively) if it does not exist.

	Raise if the directory can not be created.
	'''
	log_directory = os.path.join(basedir, 'logs')

	if not os.path.exists(log_directory):
		try:
			os.makedirs(log_directory)
		except OSError as error:
			if error.errno == errno.EEXIST and os.path.isdir(log_directory):
				pass
			else:
				pass

	return log_directory


def configureLogging(logger_name, level=None, format=None):
	'''Configure `loggerName` loggers with console and file handler.

	Optionally specify log *level* (default WARNING)

	Optionally set *format*, default:
	`%(asctime)s - %(name)s - %(levelname)s - %(message)s`.
	'''

	# provide default values for level and format
	format = format or '[%(asctime)s] %(message)s'
	level = level or logging.WARNING

	log_directory = getLogDirectory()
	logfile = os.path.join(log_directory, logger_name)

	logging_settings = {
		'version': 1,
		'disable_existing_loggers': False,
		'handlers': {
			'console': {
				'class': 'logging.StreamHandler',
				'level': logging._levelNames[level],
				'formatter': 'file',
				'stream': 'ext://sys.stdout',
			},
			'file': {
				'class': 'logging.handlers.RotatingFileHandler',
				'level': 'DEBUG',
				'formatter': 'file',
				'filename': logfile,
				'mode': 'a',
				'maxBytes': 10485760,
				'backupCount': 5,
			},
		},
		'formatters': {
			'file': {
				'format': format
			}
		},
		'loggers': {
			'': {
				'level': 'DEBUG',
				'handlers': ['console', 'file']
			}
		}
	}

	# Set default logging settings.
	logging.config.dictConfig(logging_settings)

	# Redirect warnings to log so can be debugged.
	logging.captureWarnings(True)

	# Log out the file output.
	# logging.info(u'Saving log file to: %s' % logfile)



# Create filename 'debug'
configureLogging('debug')
