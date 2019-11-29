def showMessage(message, character='-', size=0):
    """
    -> Show a message between two blocks of characters
    :param message: will be showed
    :param character: will be used to create the blocks. By default it will use a dash -
    :param size: size of the block. By default it will be used the size of the message
    :return: no returns
    """
    # global newMessage  # instead of create a new scope for 'newMessage' we will use the global scope of the
    # variable. The variable newMessage must be created as a global variable, obviously
    if size == 0:
        size = len(message)
    print(character * size)
    print(message)
    print(character * size)
