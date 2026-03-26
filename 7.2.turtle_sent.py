class PostOffice:
    """A Post Office class. Allows users to message each other.
    
    Parameters
    ----------
    usernames : list
        Users for which we should create PO Boxes.

    Attributes
    ----------
    message_id : int
        Incremental id of the last message sent.
    boxes : dict
        Users' inboxes.
    """

    def __init__(self, usernames):
        self.message_id = 0
        self.boxes = {user: [] for user in usernames}
        
    def send_message(self, sender, recipient, message_body, title="", urgent=False):
        """Send a message to a recipient.

        Parameters
        ----------
        sender : str
            The message sender's username.
        recipient : str
            The message recipient's username.
        message_body : str
            The body of the message.
        title : str, optional
            The title of the message.
        urgent : bool, optional
            The urgency of the message.
            Urgent messages appear first.

        Returns
        -------
        int
            The message ID, auto incremented number.

        Raises
        ------
        KeyError
            If the recipient does not exist.
        """
        user_box = self.boxes[recipient]
        self.message_id = self.message_id + 1
        message_details = {
            'id': self.message_id,
            'title': title,
            'body': message_body,
            'sender': sender,
            'is_read': False
        }
        
        if urgent:
            user_box.insert(0, message_details)
        else:
            user_box.append(message_details)
            
        return self.message_id

    def read_inbox(self, username, n=None):
        """Read unread messages from a user's inbox.

        Parameters
        ----------
        username : str
            The username whose inbox is being read.
        n : int, optional
            The number of unread messages to read. If None, reads all unread messages.

        Returns
        -------
        list
            A list of unread message dictionaries.

        Raises
        ------
        KeyError
            If the user does not exist.
        """
        user_box = self.boxes[username]
        
        # Collect all unread messages
        unread_messages = [msg for msg in user_box if not msg['is_read']]
        
        # Slice the list according to the requested number, if provided
        if n is not None:
            messages_to_return = unread_messages[:n]
        else:
            messages_to_return = unread_messages
            
        # Mark the returned messages as read
        for msg in messages_to_return:
            msg['is_read'] = True
            
        return messages_to_return

    def search_inbox(self, username, search_string):
        """Search a user's inbox for messages containing a specific string.

        Parameters
        ----------
        username : str
            The username whose inbox is being searched.
        search_string : str
            The string to search for in message titles or bodies.

        Returns
        -------
        list
            A list of message dictionaries matching the search criteria.

        Raises
        ------
        KeyError
            If the user does not exist.
        """
        user_box = self.boxes[username]
        matching_messages = []
        
        # Iterate through all messages (both read and unread)
        for msg in user_box:
            if search_string in msg['title'] or search_string in msg['body']:
                matching_messages.append(msg)
                
        return matching_messages