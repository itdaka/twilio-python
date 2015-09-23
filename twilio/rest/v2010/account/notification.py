# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest import serialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class NotificationList(ListResource):

    def __init__(self, domain, account_sid):
        super(NotificationList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Notifications".format(**self._instance_kwargs)

    def read(self, log=values.unset, message_date_before=values.unset,
             message_date=values.unset, message_date_after=values.unset, limit=None,
             page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({
            "Log": log,
            "MessageDate<": serialize.iso8601_date(message_date_before),
            "MessageDate": serialize.iso8601_date(message_date),
            "MessageDate>": serialize.iso8601_date(message_date_after),
        })
        params.update(kwargs)
        
        return self._domain.read(
            self,
            NotificationInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, log=values.unset, message_date_before=values.unset,
             message_date=values.unset, message_date_after=values.unset,
             page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            "Log": log,
            "MessageDate<": serialize.iso8601_date(message_date_before),
            "MessageDate": serialize.iso8601_date(message_date),
            "MessageDate>": serialize.iso8601_date(message_date_after),
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._domain.page(
            self,
            NotificationInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )


class NotificationContext(InstanceContext):

    def __init__(self, domain, account_sid, sid):
        super(NotificationContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/Notifications/{sid}.json".format(**self._instance_kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._domain.fetch(
            NotificationInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        return self._domain.delete("delete", self._uri)


class NotificationInstance(InstanceResource):

    def __init__(self, domain, payload, account_sid, sid=None):
        super(NotificationInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._api_version = payload['api_version']
        self._call_sid = payload['call_sid']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._error_code = payload['error_code']
        self._log = payload['log']
        self._message_date = deserialize.iso8601_datetime(payload['message_date'])
        self._message_text = payload['message_text']
        self._more_info = payload['more_info']
        self._request_method = payload['request_method']
        self._request_url = payload['request_url']
        self._request_variables = payload['request_variables']
        self._response_body = payload['response_body']
        self._response_headers = payload['response_headers']
        self._sid = payload['sid']
        self._uri = payload['uri']
        
        # Context
        self._lazy_context = None
        self._context_account_sid = account_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = NotificationContext(
                self._domain,
                self._context_account_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The unique sid that identifies this account """
        return self._account_sid

    @property
    def api_version(self):
        """ The version of the Twilio API in use """
        return self._api_version

    @property
    def call_sid(self):
        """ The string that uniquely identifies the call """
        return self._call_sid

    @property
    def date_created(self):
        """ The date this resource was created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date this resource was last updated """
        return self._date_updated

    @property
    def error_code(self):
        """ A unique error code corresponding to the notification """
        return self._error_code

    @property
    def log(self):
        """ An integer log level """
        return self._log

    @property
    def message_date(self):
        """ The date the notification was generated """
        return self._message_date

    @property
    def message_text(self):
        """ The text of the notification. """
        return self._message_text

    @property
    def more_info(self):
        """ A URL for more information about the error code """
        return self._more_info

    @property
    def request_method(self):
        """ HTTP method used with the request url """
        return self._request_method

    @property
    def request_url(self):
        """ URL of the resource that generated the notification """
        return self._request_url

    @property
    def request_variables(self):
        """ Twilio-generated HTTP variables sent to the server """
        return self._request_variables

    @property
    def response_body(self):
        """ The HTTP body returned by your server. """
        return self._response_body

    @property
    def response_headers(self):
        """ The HTTP headers returned by your server. """
        return self._response_headers

    @property
    def sid(self):
        """ A string that uniquely identifies this notification """
        return self._sid

    @property
    def uri(self):
        """ The URI for this resource """
        return self._uri

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()