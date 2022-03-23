# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class ChannelList(ListResource):

    def __init__(self, version):
        """
        Initialize the ChannelList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.chat.v3.channel.ChannelList
        :rtype: twilio.rest.chat.v3.channel.ChannelList
        """
        super(ChannelList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self, service_sid, sid):
        """
        Constructs a ChannelContext

        :param service_sid: Service Sid.
        :param sid: A string that uniquely identifies this Channel.

        :returns: twilio.rest.chat.v3.channel.ChannelContext
        :rtype: twilio.rest.chat.v3.channel.ChannelContext
        """
        return ChannelContext(self._version, service_sid=service_sid, sid=sid, )

    def __call__(self, service_sid, sid):
        """
        Constructs a ChannelContext

        :param service_sid: Service Sid.
        :param sid: A string that uniquely identifies this Channel.

        :returns: twilio.rest.chat.v3.channel.ChannelContext
        :rtype: twilio.rest.chat.v3.channel.ChannelContext
        """
        return ChannelContext(self._version, service_sid=service_sid, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V3.ChannelList>'


class ChannelPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ChannelPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.chat.v3.channel.ChannelPage
        :rtype: twilio.rest.chat.v3.channel.ChannelPage
        """
        super(ChannelPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ChannelInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.chat.v3.channel.ChannelInstance
        :rtype: twilio.rest.chat.v3.channel.ChannelInstance
        """
        return ChannelInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Chat.V3.ChannelPage>'


class ChannelContext(InstanceContext):

    def __init__(self, version, service_sid, sid):
        """
        Initialize the ChannelContext

        :param Version version: Version that contains the resource
        :param service_sid: Service Sid.
        :param sid: A string that uniquely identifies this Channel.

        :returns: twilio.rest.chat.v3.channel.ChannelContext
        :rtype: twilio.rest.chat.v3.channel.ChannelContext
        """
        super(ChannelContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Channels/{sid}'.format(**self._solution)

    def update(self, type=values.unset, messaging_service_sid=values.unset,
               x_twilio_webhook_enabled=values.unset):
        """
        Update the ChannelInstance

        :param ChannelInstance.ChannelType type: The Type for this Channel to migrate to.
        :param unicode messaging_service_sid: The unique ID of the Messaging Service this channel belongs to.
        :param ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.chat.v3.channel.ChannelInstance
        """
        data = values.of({'Type': type, 'MessagingServiceSid': messaging_service_sid, })
        headers = values.of({'X-Twilio-Webhook-Enabled': x_twilio_webhook_enabled, })

        payload = self._version.update(method='POST', uri=self._uri, data=data, headers=headers, )

        return ChannelInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V3.ChannelContext {}>'.format(context)


class ChannelInstance(InstanceResource):

    class ChannelType(object):
        PUBLIC = "public"
        PRIVATE = "private"

    class WebhookEnabledType(object):
        TRUE = "true"
        FALSE = "false"

    def __init__(self, version, payload, service_sid=None, sid=None):
        """
        Initialize the ChannelInstance

        :returns: twilio.rest.chat.v3.channel.ChannelInstance
        :rtype: twilio.rest.chat.v3.channel.ChannelInstance
        """
        super(ChannelInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'friendly_name': payload.get('friendly_name'),
            'unique_name': payload.get('unique_name'),
            'attributes': payload.get('attributes'),
            'type': payload.get('type'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'created_by': payload.get('created_by'),
            'members_count': deserialize.integer(payload.get('members_count')),
            'messages_count': deserialize.integer(payload.get('messages_count')),
            'messaging_service_sid': payload.get('messaging_service_sid'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid'],
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: ChannelContext for this ChannelInstance
        :rtype: twilio.rest.chat.v3.channel.ChannelContext
        """
        if self._context is None:
            self._context = ChannelContext(
                self._version,
                service_sid=self._solution['service_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def attributes(self):
        """
        :returns: The JSON string that stores application-specific data
        :rtype: unicode
        """
        return self._properties['attributes']

    @property
    def type(self):
        """
        :returns: The visibility of the channel. Can be: `public` or `private`
        :rtype: ChannelInstance.ChannelType
        """
        return self._properties['type']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def created_by(self):
        """
        :returns: The identity of the User that created the channel
        :rtype: unicode
        """
        return self._properties['created_by']

    @property
    def members_count(self):
        """
        :returns: The number of Members in the Channel
        :rtype: unicode
        """
        return self._properties['members_count']

    @property
    def messages_count(self):
        """
        :returns: The number of Messages that have been passed in the Channel
        :rtype: unicode
        """
        return self._properties['messages_count']

    @property
    def messaging_service_sid(self):
        """
        :returns: The unique ID of the Messaging Service this channel belongs to.
        :rtype: unicode
        """
        return self._properties['messaging_service_sid']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Channel resource
        :rtype: unicode
        """
        return self._properties['url']

    def update(self, type=values.unset, messaging_service_sid=values.unset,
               x_twilio_webhook_enabled=values.unset):
        """
        Update the ChannelInstance

        :param ChannelInstance.ChannelType type: The Type for this Channel to migrate to.
        :param unicode messaging_service_sid: The unique ID of the Messaging Service this channel belongs to.
        :param ChannelInstance.WebhookEnabledType x_twilio_webhook_enabled: The X-Twilio-Webhook-Enabled HTTP request header

        :returns: The updated ChannelInstance
        :rtype: twilio.rest.chat.v3.channel.ChannelInstance
        """
        return self._proxy.update(
            type=type,
            messaging_service_sid=messaging_service_sid,
            x_twilio_webhook_enabled=x_twilio_webhook_enabled,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Chat.V3.ChannelInstance {}>'.format(context)
