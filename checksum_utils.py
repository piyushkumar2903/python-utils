import hashlib
import logging
import os
import shutil
import sys

LOGGER = logging.getLogger()

_MISSING_FILE_PATH_MSG = "Missing parameter file_path: %s"

def generate_sha256_checksum(file_path):
    '''
    Purpose:    Calculate the SHA256 checksum of a given file
    Parameters: Path to file
    Returns:    The SHA256 checksum or None if something went wrong during calculation
    '''
    if not file_path \
    or not os.path.isfile(file_path):
        LOGGER.debug(_MISSING_FILE_PATH_MSG, str(file_path))
        return None

    sha_hash = hashlib.sha256()
    buffer = 4096
    with open(file_path, 'rb') as sha_file:
        while True:
            data = sha_file.read(buffer)
            if not data:
                break
            sha_hash.update(data)

    return sha_hash.hexdigest()
 

def generate_md5_checksum(file_path):
    '''
    Purpose:    Will calculate a file's checksum (md5)
    Returns:    either False or the MD5 checksum of the file
    Parameters: path to file
    '''
    if not file_path:
        LOGGER.debug(_MISSING_FILE_PATH_MSG, str(file_path))
        return None

    checksum_readable = ""
    if os.path.isfile(file_path):
        with open(file_path, mode='rb') as checksum_file:
            checksum = hashlib.md5()
            for buf in iter(partial(checksum_file.read, 128), b''):
                checksum.update(buf)
        checksum_readable = checksum.hexdigest()
    else:
        return None

    return checksum_readable
