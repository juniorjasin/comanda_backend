import logging
import os

class Logger():
  def __init__(self, name):
    self.debugLogger = self.createLogger(name + '-d', logging.DEBUG)
    self.infoLogger = self.createLogger(name + '-i', logging.INFO)
    self.warningLogger = self.createLogger(name + '-war', logging.WARNING)
    self.errorLogger = self.createLogger(name + '-err', logging.ERROR)
    self.criticalLogger = self.createLogger(name + '-crit', logging.CRITICAL)

    formatterStreamHandler = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    self.debugLogger.addHandler(self.createStreamHandler(formatterStreamHandler, logging.DEBUG))
    self.infoLogger.addHandler(self.createStreamHandler(formatterStreamHandler, logging.INFO))
    self.warningLogger.addHandler(self.createStreamHandler(formatterStreamHandler, logging.WARNING))
    self.errorLogger.addHandler(self.createStreamHandler(formatterStreamHandler, logging.ERROR))
    self.criticalLogger.addHandler(self.createStreamHandler(formatterStreamHandler, logging.CRITICAL))
        
    formatterFileHandler = logging.Formatter('%(asctime)s - %(name)s - %(lineno)d - %(message)s')
    self.debugLogger.addHandler(self.createFileHandler(os.path.join(os.environ['INSTALL_DIR'], 'logs', 'debug.txt'), formatterFileHandler, logging.DEBUG))    
    self.infoLogger.addHandler(self.createFileHandler(os.path.join(os.environ['INSTALL_DIR'], 'logs', 'info.txt'), formatterFileHandler, logging.INFO))    
    self.warningLogger.addHandler(self.createFileHandler(os.path.join(os.environ['INSTALL_DIR'], 'logs', 'warning.txt'), formatterFileHandler, logging.WARNING))    
    self.errorLogger.addHandler(self.createFileHandler(os.path.join(os.environ['INSTALL_DIR'], 'logs', 'error.txt'), formatterFileHandler, logging.ERROR))    
    self.criticalLogger.addHandler(self.createFileHandler(os.path.join(os.environ['INSTALL_DIR'], 'logs', 'critical.txt'), formatterFileHandler, logging.CRITICAL))    
    # Archivo donde loguean todas
    self.debugLogger.addHandler(self.createFileHandler(os.path.join(os.environ['INSTALL_DIR'], 'logs', 'all.txt'), formatterFileHandler, logging.DEBUG))    
    self.infoLogger.addHandler(self.createFileHandler(os.path.join(os.environ['INSTALL_DIR'], 'logs', 'all.txt'), formatterFileHandler, logging.INFO))    
    self.warningLogger.addHandler(self.createFileHandler(os.path.join(os.environ['INSTALL_DIR'], 'logs', 'all.txt'), formatterFileHandler, logging.WARNING))    
    self.errorLogger.addHandler(self.createFileHandler(os.path.join(os.environ['INSTALL_DIR'], 'logs', 'all.txt'), formatterFileHandler, logging.ERROR))    
    self.criticalLogger.addHandler(self.createFileHandler(os.path.join(os.environ['INSTALL_DIR'], 'logs', 'all.txt'), formatterFileHandler, logging.CRITICAL))    

  def createLogger(self, name, level):
    logger = logging.getLogger(name)
    logger.propagate = False
    logger.setLevel(level)
    return logger

  def createStreamHandler(self, formatter, level):
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)
    streamHandler.setLevel(level)
    return streamHandler

  def createFileHandler(self, filename, formatter, level):
    fileHandler = logging.FileHandler(filename)
    fileHandler.setFormatter(formatter)
    fileHandler.setLevel(level)
    return fileHandler

  def debug(self, message):
    self.debugLogger.debug(message)
    

  def info(self, message):
    self.infoLogger.info(message)
    

  def warning(self, message):
    self.warningLogger.warning(message)
    

  def error(self, message):
    self.errorLogger.error(message)
    
   
  def critical(self, message):
    self.criticalLogger.critical(message)
    
