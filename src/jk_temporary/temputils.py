#!/usr/bin/env python3




import os
import codecs
import random




RESERVOIR = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"





#
# Create a path for a temporary file or directory.
#
# @param		string baseDirPath		The base directory the file should reside in.
# @param		string prefix			A prefix to prepend the random file (or directory) name part.
# @param		int randomNameLength	The length in characters of the random file (or directory) name part to create.
# @param		string postfix			A postfix to append the random file (or directory) name part.
# @return		string					Returns a file (or directory) path. No checking is performed if this file or directory already exists.
# 										This method just creates the path.
#
def createRandomFilePath(baseDirPath = "/tmp", prefix = 'tmp_', randomNameLength = 32, postfix = ''):
	s = ''.join(random.choice(RESERVOIR) for _ in range(randomNameLength))
	return os.path.join(baseDirPath, prefix + s + postfix)
#





#
# Create a unique new temporary directory.
#
# @param		string baseDirPath		The directory that serves as a parent for the new directory to create.
# @param		string prefix			A prefix to prepend the random directory name part.
# @param		int randomNameLength	The length in characters of the random directory name part to create.
# @param		string postfix			A postfix to append the random directory name part.
# @param		int dirMode				The UNIX/Linux mode the directory should have on creation.
#										This is 0700 by default to ensure that other users can not read or write to the new directory.
# @return		string					Returns a unique path to a directory that just has been created.
#
def createTempDir(baseDirPath = "/tmp", prefix = 'tmp_', randomNameLength = 32, postfix = '', dirMode = 0o700):
	while True:
		path = createRandomFilePath(baseDirPath, prefix = prefix, randomNameLength = randomNameLength, postfix = postfix)
		if not os.path.exists(path):
			os.mkdir(path, dirMode)
			return path
#




#
# Create a unique new temporary file ready for later writing.
# Please note that temporary file names are generated using a RNG. That implies that if you do not write
# to that file after a call to this function an additional call to <c>createTempFilePath()</c> could produce the same
# file name again. If <c>randomNameLength</c>
# is large enough this is quite unlikely and not a real problem, but you should recognize that at least in
# theory this phenomenon can occur.
#
# @param		string baseDirPath		The directory that serves as a parent for the new directory to create.
# @param		int randomNameLength	The length in characters of the random file name part to create.
# @param		string prefix			A prefix to prepend the random file name part.
# @param		string postfix			A postfix to append the random file name part.
# @param		int fileMode			The UNIX/Linux mode the file should have on creation.
#										This is 0600 by default to ensure that other users can not read or write to the new file.
# @return		string					Returns  the unique path to a file that just has been created.
#
def createTempFilePath(baseDirPath = "/tmp", prefix = 'tmp_', randomNameLength = 32, postfix = '', fileMode = 0o600):
	while True:
		path = createRandomFilePath(baseDirPath, prefix = prefix, randomNameLength = randomNameLength, postfix = postfix)
		if not os.path.exists(path):
			return path
#




#
# Create a unique new temporary file ready for later writing.
#
# @param		string baseDirPath		The directory that serves as a parent for the new directory to create.
# @param		int randomNameLength	The length in characters of the random file name part to create.
# @param		string prefix			A prefix to prepend the random file name part.
# @param		string postfix			A postfix to append the random file name part.
# @param		int fileMode			The UNIX/Linux mode the file should have on creation.
#										This is 0600 by default to ensure that other users can not read or write to the new file.
# @return		string					Returns  the unique path to a file that just has been created.
#
def createTempFile(baseDirPath = "/tmp", prefix = 'tmp_', randomNameLength = 32, postfix = '', fileMode = 0o600):
	while True:
		path = createRandomFilePath(baseDirPath, prefix = prefix, randomNameLength = randomNameLength, postfix = postfix)
		if not os.path.exists(path):
			codecs.open(path, 'w', 'utf-8').close()
			os.chmod(path, fileMode)
			return path
#




#
# Create a unique new temporary file ready for immediate writing.
#
# @param		string baseDirPath		The directory that serves as a parent for the new directory to create.
# @param		int randomNameLength	The length in characters of the random file name part to create.
# @param		string prefix			A prefix to prepend the random file name part.
# @param		string postfix			A postfix to append the random file name part.
# @param		int fileMode			The UNIX/Linux mode the file should have on creation.
#										This is 0600 by default to ensure that other users can not read or write to the new file.
# @return		tuple					Returns a tuple consisting of two elements:
#										- the unique path to a file that just has been created
#										- the open file handle
#
def createTempFileUTF8(baseDirPath = "/tmp", prefix = 'tmp_', randomNameLength = 32, postfix = '', fileMode = 0o600):
	while True:
		path = createRandomFilePath(baseDirPath, prefix = prefix, randomNameLength = randomNameLength, postfix = postfix)
		if not os.path.exists(path):
			fd = codecs.open(path, 'w', 'utf-8')
			os.chmod(path, fileMode)
			return (path, fd)
#





#
# Create a unique new temporary file ready for immediate writing.
#
# @param		string baseDirPath		The directory that serves as a parent for the new directory to create.
# @param		int randomNameLength	The length in characters of the random file name part to create.
# @param		string prefix			A prefix to prepend the random file name part.
# @param		string postfix			A postfix to append the random file name part.
# @param		int fileMode			The UNIX/Linux mode the file should have on creation.
#										This is 0600 by default to ensure that other users can not read or write to the new file.
# @return		tuple					Returns a tuple consisting of two elements:
#										- the unique path to a file that just has been created
#										- the open file handle
#
def createTempFileBinary(baseDirPath = "/tmp", prefix = 'tmp_', randomNameLength = 32, postfix = '', fileMode = 0o600):
	while True:
		path = createRandomFilePath(baseDirPath, prefix = prefix, randomNameLength = randomNameLength, postfix = postfix)
		if not os.path.exists(path):
			fd = open(path, 'wb', fileMode)
			return (path, fd)
#








