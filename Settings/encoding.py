def check_encoding(file_path):
    """
    Check the encoding of a text file,
    ensuring it uses UTF-8-NOBOM.
    """
    logging.info("Check encoding of {0} before installation".format(file_path))

    # Open it, read just the area containing the byte mark
    with open(file_path, "rb") as encode_check:
        encoding = encode_check.readline(3)

    if (
        # The settings file uses UTF-8-BOM encoding
        encoding == b"\xef\xbb\xbf"
        # The settings file uses UCS-2 Big Endian encoding
        or encoding == b"\xfe\xff\x00"
        # The settings file uses UCS-2 Little Endian
        or encoding == b"\xff\xfe/"
    ):
        # The encoding is not correct
        return False

    # The file used the proper encoding
    else:
        return True
