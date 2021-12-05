

import os
import typing
import string
import random








class TempDir(object):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	# @param		string	baseDirPath					The directory that serves as a parent for the new files and directories to create.
	# @param		string	namePrefix					A prefix to prepend the random file name part. The default is: "<c>tmp-</c>".
	# @param		string	namePostfix					A postfix to append the random file name part. The default is: <c>None</c>.
	# @param		string	defaultExtension			A file extension to append the random file name part
	#													after the postfix). This applies to file names only. the default is: <c>None</c>.
	# @param		int	randomNameLength				The length in characters of the random file name part to create.
	# @param		int	defaultAccessModeFiles			The UNIX/Linux mode files should have on creation. This is 0600 by default to
	#													ensure that other users can not read or write to the new file.
	# @param		int	defaultAccessModeDirectories	The UNIX/Linux mode directories should have on creation. This is 0700 by default
	#													to ensure that other users can not read or write to the new directory.
	#
	def __init__(self,
			baseDirPath = "/tmp",
			namePrefix = "tmp-",
			namePostfix = None,
			defaultExtension:str = None,
			randomNameLength = 32,
			defaultAccessModeFiles = 0o600,
			defaultAccessModeDirectories = 0o700,
		):

		if not os.path.isdir(baseDirPath):
			raise Exception("No such directory: " + baseDirPath)

		# ----

		self.__dirPath = baseDirPath

		self.__defaultAccessModeFiles = defaultAccessModeFiles

		self.__defaultAccessModeDirectories = defaultAccessModeDirectories

		if namePrefix is None:
			namePrefix = ""
		self.__namePrefix = namePrefix

		if namePostfix is None:
			namePostfix = ""
		self.__namePostfix = namePostfix

		self.__randomNameLength = randomNameLength

		if defaultExtension is None:
			defaultExtension = ""
		self.__defaultExtension = defaultExtension
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	#
	# Remove all files in the temporary directory. Please note that temporary directories remain untouched!
	#
	def clear(self) -> None:
		for fileName in os.listdir(self.__dirPath):
			filePath = os.path.join(self.__dirPath, fileName)
			if os.path.isfile(filePath):
				os.unlink(filePath)
	#

	#
	# Create a new file path.
	# Please note that temporary file names are generated using a RNG. That implies that if you do not write
	# to that file after a call to this method an additional call to <c>createFilePath()</c> could produce the same
	# file name again. If <c>randomNameLength</c>
	# is large enough this is quite unlikely and not a real problem, but you should recognize that at least in
	# theory this phenomenon can occur.
	#
	# @param		str extension		An optional file name extension. If you do not specify anything here the default
	#										extension will be used as specified during construction.
	# @return		str					Returns the full qualified file path that furtheron can be used for writing.
	#
	def createFilePath(self, extension:str = None) -> str:
		if extension != None:
			if not extension.startswith("."):
				extension = "." + extension
		else:
			extension = self.__defaultExtension

		while True:
			reservoir = string.ascii_lowercase + string.ascii_uppercase + string.digits
			random_chars = ""
			for x in range(self.__randomNameLength):
				random_chars += random.choice(reservoir)
			tmpFilePath = os.path.join(self.__dirPath, self.__namePrefix + random_chars + self.__namePostfix + extension)
			if not os.path.exists(tmpFilePath):
				return tmpFilePath
	#

	#
	# Create a new directory path.
	# Please note that temporary directory names are generated using a RNG. That implies that if you do not create
	# that directory after a call to this method an additional call to <c>createFilePath()</c> could produce the same
	# directory name again. If <c>randomNameLength</c>
	# is large enough this is quite unlikely and not a real problem, but you should recognize that at least in
	# theory this phenomenon can occur.
	#
	# @return		str					Returns the full qualified file path that furtheron can be used for writing.
	#
	def createDirPath(self) -> str:
		while True:
			reservoir = string.ascii_lowercase + string.ascii_uppercase + string.digits
			random_chars = ""
			for x in range(self.__randomNameLength):
				random_chars += random.choice(reservoir)
			tmpFilePath = os.path.join(self.__dirPath, self.__namePrefix + random_chars + self.__namePostfix)
			if not os.path.exists(tmpFilePath):
				return tmpFilePath
	#

	#
	# Create a new temporary file.
	#
	# @param		str extension			An optional file name extension. If you do not specify anything here the default
	#										extension will be used as specified during construction.
	# @param		int accessMode			An optional mode value that defines basic access rights for the file.
	# @return		str						Returns  the unique path to a file that just has been created.
	#
	def createFile(self, extension:str = None, accessMode:int = None) -> str:
		if accessMode == None:
			accessMode = self.__defaultAccessModeFiles
		tmpFilePath = self.createFilePath(extension)

		umask_original = os.umask(0)
		try:
			fdesc = os.open(tmpFilePath, os.O_WRONLY | os.O_CREAT | os.O_EXCL, accessMode)
		finally:
			os.umask(umask_original)

		os.fdopen(fdesc, "wb").close()

		return tmpFilePath
	#

	#
	# Create a new temporary file.
	#
	# @param		str extension			An optional file name extension. If you do not specify anything here the default
	#										extension will be used as specified during construction.
	# @param		int accessMode			An optional mode value that defines basic access rights for the file.
	# @return		str						Returns  the unique path to a file that just has been created.
	#
	def writeFile(self, extension:str = None, accessMode:int = None, content:typing.Union[str,bytes,bytearray] = None) -> str:
		if accessMode == None:
			accessMode = self.__defaultAccessModeFiles
		tmpFilePath = self.createFilePath(extension)

		umask_original = os.umask(0)
		try:
			fdesc = os.open(tmpFilePath, os.O_WRONLY | os.O_CREAT | os.O_EXCL, accessMode)
		finally:
			os.umask(umask_original)

		if content is None:
			os.fdopen(fdesc, "wb").close()
		elif isinstance(content, str):
			with os.fdopen(fdesc, "w", encoding="UTF-8") as fout:
				fout.write(content)
		else:
			with os.fdopen(fdesc, "wb") as fout:
				fout.write(content)

		return tmpFilePath
	#

	#
	# Create a new temporary file.
	#
	# @param		str extension				An optional file name extension. If you do not specify anything here the default
	#											extension will be used as specified during construction.
	# @param		int accessMode				An optional mode value that defines basic access rights for the file.
	# @return		tuple<str,fileobj>			Returns a tuple: The full qualified file path and the file handle that can be used for writing.
	#
	def createFileBinary(self, extension:str = None, accessMode:str = None) -> tuple:
		if accessMode == None:
			accessMode = self.__defaultAccessModeFiles
		tmpFilePath = self.createFilePath(extension)

		umask_original = os.umask(0)
		try:
			fdesc = os.open(tmpFilePath, os.O_WRONLY | os.O_CREAT | os.O_EXCL, accessMode)
		finally:
			os.umask(umask_original)

		fileObj = os.fdopen(fdesc, "wb")

		return (tmpFilePath, fileObj)
	#

	#
	# Create a new temporary file.
	#
	# @param		str extension				An optional file name extension. If you do not specify anything here the default
	#											extension will be used as specified during construction.
	# @param		int accessMode				An optional mode value that defines basic access rights for the file.
	# @return		tuple<str,fileobj>			Returns a tuple: The full qualified file path and the file handle that can be used for writing.
	#
	def createFileUTF8(self, extension:str = None, accessMode:str = None) -> tuple:
		if accessMode == None:
			accessMode = self.__defaultAccessModeFiles
		tmpFilePath = self.createFilePath(extension)

		umask_original = os.umask(0)
		try:
			fdesc = os.open(tmpFilePath, os.O_WRONLY | os.O_CREAT | os.O_EXCL, accessMode)
		finally:
			os.umask(umask_original)

		fileObj = os.fdopen(fdesc, "w", encoding="utf-8")

		return (tmpFilePath, fileObj)
	#

#











