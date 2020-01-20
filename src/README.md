jk_temporary
============

Introduction
------------

This python module is a collection of utility functions and classes to manage temporary data.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/python-module-jk-temporary)
* [pypi.python.org](https://pypi.python.org/pypi/jk_temporary)

The functions this module provides
----------------------------------

This module provides the following functions:

```python
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
def createRandomFilePath(baseDirPath = "/tmp", prefix = 'tmp_', randomNameLength = 32, postfix = '')
```

```python
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
def createTempDir(baseDirPath = "/tmp", prefix = 'tmp_', randomNameLength = 32, postfix = '', dirMode = 0o700)
```

```python
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
def createTempFilePath(baseDirPath = "/tmp", prefix = 'tmp_', randomNameLength = 32, postfix = '', fileMode = 0o600)
```

```python
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
def createTempFile(baseDirPath = "/tmp", prefix = 'tmp_', randomNameLength = 32, postfix = '', fileMode = 0o600)
```

```python
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
def createTempFileUTF8(baseDirPath = "/tmp", prefix = 'tmp_', randomNameLength = 32, postfix = '', fileMode = 0o600)
```

```python
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
def createTempFileBinary(baseDirPath = "/tmp", prefix = 'tmp_', randomNameLength = 32, postfix = '', fileMode = 0o600)
```

The object ``TempDir`` this module provides
-------------------------------------------

This module provides the class ``TempDir`` that contains the following methods:

```python
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
	baseDirPath = '/tmp', namePrefix = 'tmp-', namePostfix = None, defaultExtension = None,
	randomNameLength = 32, defaultAccessModeFiles = 0o600, defaultAccessModeDirectories = 0o700)
```

```python
#
# Remove all files in the temporary directory. Please note that temporary directories remain untouched!
#
def clear(self)
```

```python
#
# Create a new file path.
# Please note that temporary file names are generated using a RNG. That implies that if you do not write
# to that file after a call to this method an additional call to <c>createFilePath()</c> could produce the same
# file name again. If <c>randomNameLength</c>
# is large enough this is quite unlikely and not a real problem, but you should recognize that at least in
# theory this phenomenon can occur.
#
# @param		string extension		An optional file name extension. If you do not specify anything here the default
#										extension will be used as specified during construction.
# @return		string					Returns the full qualified file path that furtheron can be used for writing.
#
def createFilePath(self, extension = None)
```

```python
#
# Create a new directory path.
# Please note that temporary directory names are generated using a RNG. That implies that if you do not create
# that directory after a call to this method an additional call to <c>createFilePath()</c> could produce the same
# directory name again. If <c>randomNameLength</c>
# is large enough this is quite unlikely and not a real problem, but you should recognize that at least in
# theory this phenomenon can occur.
#
# @return		string					Returns the full qualified file path that furtheron can be used for writing.
#
def createDirPath(self)
```

```python
#
# Create a new temporary file.
#
# @param		string extension		An optional file name extension. If you do not specify anything here the default
#										extension will be used as specified during construction.
# @param		int accessMode			An optional mode value that defines basic access rights for the file.
# @return		string					Returns  the unique path to a file that just has been created.
#
def createFile(self, extension = None, accessMode = None)
```

```python
#
# Create a new temporary file.
#
# @param		string extension		An optional file name extension. If you do not specify anything here the default
#										extension will be used as specified during construction.
# @param		int accessMode			An optional mode value that defines basic access rights for the file.
# @return		(string, handle)		Returns a tuple: The full qualified file path and the file handle that can be used for writing.
#
def createFileBinary(self, extension = None, accessMode = None)
```

```python
#
# Create a new temporary file.
#
# @param		string extension		An optional file name extension. If you do not specify anything here the default
#										extension will be used as specified during construction.
# @param		int accessMode			An optional mode value that defines basic access rights for the file.
# @return		(string, handle)		Returns a tuple: The full qualified file path and the file handle that can be used for writing.
#
def createFileUTF8(self, extension = None, accessMode = None)
```

Contact information
-------------------

This is Open Source code. That not only gives you the possibility of freely using this code it also
allows you to contribute. Feel free to contact the author(s) of this software listed below, either
for comments, collaboration requests, suggestions for improvement or reporting bugs:

* Jürgen Knauth: jknauth@uni-goettingen.de, pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0


