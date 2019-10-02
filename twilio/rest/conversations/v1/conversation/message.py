# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class MessageList(ListResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, conversation_sid):
        """
        Initialize the MessageList

        :param Version version: Version that contains the resource
        :param conversation_sid: The unique id of the Conversation for this message.

        :returns: twilio.rest.conversations.v1.conversation.message.MessageList
        :rtype: twilio.rest.conversations.v1.conversation.message.MessageList
        """
        super(MessageList, self).__init__(version)

        # Path Solution
        self._solution = {'conversation_sid': conversation_sid, }
        self._uri = '/Conversations/{conversation_sid}/Messages'.format(**self._solution)

    def create(self, author=values.unset, body=values.unset,
               date_created=values.unset, date_updated=values.unset,
               attributes=values.unset, media_sid=values.unset):
        """
        Create a new MessageInstance

        :param unicode author: The channel specific identifier of the message's author.
        :param unicode body: The content of the message.
        :param datetime date_created: The date that this resource was created.
        :param datetime date_updated: The date that this resource was last updated.
        :param unicode attributes: A string metadata field you can use to store any data you wish.
        :param unicode media_sid: The Media Sid to be attached to the new Message.

        :returns: Newly created MessageInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.MessageInstance
        """
        data = values.of({
            'Author': author,
            'Body': body,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'Attributes': attributes,
            'MediaSid': media_sid,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return MessageInstance(self._version, payload, conversation_sid=self._solution['conversation_sid'], )

    def stream(self, limit=None, page_size=None):
        """
        Streams MessageInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.conversation.message.MessageInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists MessageInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.conversations.v1.conversation.message.MessageInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of MessageInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of MessageInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.MessagePage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return MessagePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of MessageInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of MessageInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.MessagePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return MessagePage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a MessageContext

        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.conversations.v1.conversation.message.MessageContext
        :rtype: twilio.rest.conversations.v1.conversation.message.MessageContext
        """
        return MessageContext(self._version, conversation_sid=self._solution['conversation_sid'], sid=sid, )

    def __call__(self, sid):
        """
        Constructs a MessageContext

        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.conversations.v1.conversation.message.MessageContext
        :rtype: twilio.rest.conversations.v1.conversation.message.MessageContext
        """
        return MessageContext(self._version, conversation_sid=self._solution['conversation_sid'], sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.MessageList>'


class MessagePage(Page):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, response, solution):
        """
        Initialize the MessagePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param conversation_sid: The unique id of the Conversation for this message.

        :returns: twilio.rest.conversations.v1.conversation.message.MessagePage
        :rtype: twilio.rest.conversations.v1.conversation.message.MessagePage
        """
        super(MessagePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MessageInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.conversations.v1.conversation.message.MessageInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.MessageInstance
        """
        return MessageInstance(self._version, payload, conversation_sid=self._solution['conversation_sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Conversations.V1.MessagePage>'


class MessageContext(InstanceContext):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    def __init__(self, version, conversation_sid, sid):
        """
        Initialize the MessageContext

        :param Version version: Version that contains the resource
        :param conversation_sid: The unique id of the Conversation for this message.
        :param sid: A 34 character string that uniquely identifies this resource.

        :returns: twilio.rest.conversations.v1.conversation.message.MessageContext
        :rtype: twilio.rest.conversations.v1.conversation.message.MessageContext
        """
        super(MessageContext, self).__init__(version)

        # Path Solution
        self._solution = {'conversation_sid': conversation_sid, 'sid': sid, }
        self._uri = '/Conversations/{conversation_sid}/Messages/{sid}'.format(**self._solution)

    def update(self, author=values.unset, body=values.unset,
               date_created=values.unset, date_updated=values.unset,
               attributes=values.unset):
        """
        Update the MessageInstance

        :param unicode author: The channel specific identifier of the message's author.
        :param unicode body: The content of the message.
        :param datetime date_created: The date that this resource was created.
        :param datetime date_updated: The date that this resource was last updated.
        :param unicode attributes: A string metadata field you can use to store any data you wish.

        :returns: Updated MessageInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.MessageInstance
        """
        data = values.of({
            'Author': author,
            'Body': body,
            'DateCreated': serialize.iso8601_datetime(date_created),
            'DateUpdated': serialize.iso8601_datetime(date_updated),
            'Attributes': attributes,
        })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return MessageInstance(
            self._version,
            payload,
            conversation_sid=self._solution['conversation_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the MessageInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def fetch(self):
        """
        Fetch a MessageInstance

        :returns: Fetched MessageInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.MessageInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return MessageInstance(
            self._version,
            payload,
            conversation_sid=self._solution['conversation_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.MessageContext {}>'.format(context)


class MessageInstance(InstanceResource):
    """ PLEASE NOTE that this class contains beta products that are subject to
    change. Use them with caution. """

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    def __init__(self, version, payload, conversation_sid, sid=None):
        """
        Initialize the MessageInstance

        :returns: twilio.rest.conversations.v1.conversation.message.MessageInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.MessageInstance
        """
        super(MessageInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'conversation_sid': payload['conversation_sid'],
            'sid': payload['sid'],
            'index': deserialize.integer(payload['index']),
            'author': payload['author'],
            'body': payload['body'],
            'media': payload['media'],
            'attributes': payload['attributes'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {'conversation_sid': conversation_sid, 'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: MessageContext for this MessageInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.MessageContext
        """
        if self._context is None:
            self._context = MessageContext(
                self._version,
                conversation_sid=self._solution['conversation_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The unique id of the Account responsible for this message.
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def conversation_sid(self):
        """
        :returns: The unique id of the Conversation for this message.
        :rtype: unicode
        """
        return self._properties['conversation_sid']

    @property
    def sid(self):
        """
        :returns: A 34 character string that uniquely identifies this resource.
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def index(self):
        """
        :returns: The index of the message within the Conversation.
        :rtype: unicode
        """
        return self._properties['index']

    @property
    def author(self):
        """
        :returns: The channel specific identifier of the message's author.
        :rtype: unicode
        """
        return self._properties['author']

    @property
    def body(self):
        """
        :returns: The content of the message.
        :rtype: unicode
        """
        return self._properties['body']

    @property
    def media(self):
        """
        :returns: An array of objects that describe the Message's media if attached, otherwise, null.
        :rtype: dict
        """
        return self._properties['media']

    @property
    def attributes(self):
        """
        :returns: A string metadata field you can use to store any data you wish.
        :rtype: unicode
        """
        return self._properties['attributes']

    @property
    def date_created(self):
        """
        :returns: The date that this resource was created.
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date that this resource was last updated.
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: An absolute URL for this message.
        :rtype: unicode
        """
        return self._properties['url']

    def update(self, author=values.unset, body=values.unset,
               date_created=values.unset, date_updated=values.unset,
               attributes=values.unset):
        """
        Update the MessageInstance

        :param unicode author: The channel specific identifier of the message's author.
        :param unicode body: The content of the message.
        :param datetime date_created: The date that this resource was created.
        :param datetime date_updated: The date that this resource was last updated.
        :param unicode attributes: A string metadata field you can use to store any data you wish.

        :returns: Updated MessageInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.MessageInstance
        """
        return self._proxy.update(
            author=author,
            body=body,
            date_created=date_created,
            date_updated=date_updated,
            attributes=attributes,
        )

    def delete(self):
        """
        Deletes the MessageInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def fetch(self):
        """
        Fetch a MessageInstance

        :returns: Fetched MessageInstance
        :rtype: twilio.rest.conversations.v1.conversation.message.MessageInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Conversations.V1.MessageInstance {}>'.format(context)
