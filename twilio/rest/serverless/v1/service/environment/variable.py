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


class VariableList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, environment_sid):
        """
        Initialize the VariableList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the Variable resource is associated with
        :param environment_sid: The SID of the environment in which the variable exists

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariableList
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableList
        """
        super(VariableList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'environment_sid': environment_sid, }
        self._uri = '/Services/{service_sid}/Environments/{environment_sid}/Variables'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams VariableInstance records from the API as a generator stream.
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
        :rtype: list[twilio.rest.serverless.v1.service.environment.variable.VariableInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists VariableInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.environment.variable.VariableInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of VariableInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariablePage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return VariablePage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of VariableInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariablePage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return VariablePage(self._version, response, self._solution)

    def create(self, key, value):
        """
        Create a new VariableInstance

        :param unicode key: A string by which the Variable resource can be referenced
        :param unicode value: A string that contains the actual value of the variable

        :returns: Newly created VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        data = values.of({'Key': key, 'Value': value, })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return VariableInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            environment_sid=self._solution['environment_sid'],
        )

    def get(self, sid):
        """
        Constructs a VariableContext

        :param sid: The SID of the Variable resource to fetch

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        """
        return VariableContext(
            self._version,
            service_sid=self._solution['service_sid'],
            environment_sid=self._solution['environment_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a VariableContext

        :param sid: The SID of the Variable resource to fetch

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        """
        return VariableContext(
            self._version,
            service_sid=self._solution['service_sid'],
            environment_sid=self._solution['environment_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.VariableList>'


class VariablePage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the VariablePage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Service that the Variable resource is associated with
        :param environment_sid: The SID of the environment in which the variable exists

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariablePage
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariablePage
        """
        super(VariablePage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of VariableInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        return VariableInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            environment_sid=self._solution['environment_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.VariablePage>'


class VariableContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, environment_sid, sid):
        """
        Initialize the VariableContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Variable resource from
        :param environment_sid: The SID of the environment with the Variable resource to fetch
        :param sid: The SID of the Variable resource to fetch

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        """
        super(VariableContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'environment_sid': environment_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Environments/{environment_sid}/Variables/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a VariableInstance

        :returns: Fetched VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return VariableInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            environment_sid=self._solution['environment_sid'],
            sid=self._solution['sid'],
        )

    def update(self, key=values.unset, value=values.unset):
        """
        Update the VariableInstance

        :param unicode key: A string by which the Variable resource can be referenced
        :param unicode value: A string that contains the actual value of the variable

        :returns: Updated VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        data = values.of({'Key': key, 'Value': value, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return VariableInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            environment_sid=self._solution['environment_sid'],
            sid=self._solution['sid'],
        )

    def delete(self):
        """
        Deletes the VariableInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.VariableContext {}>'.format(context)


class VariableInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, service_sid, environment_sid, sid=None):
        """
        Initialize the VariableInstance

        :returns: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        super(VariableInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload['sid'],
            'account_sid': payload['account_sid'],
            'service_sid': payload['service_sid'],
            'environment_sid': payload['environment_sid'],
            'key': payload['key'],
            'value': payload['value'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_updated': deserialize.iso8601_datetime(payload['date_updated']),
            'url': payload['url'],
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'environment_sid': environment_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: VariableContext for this VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableContext
        """
        if self._context is None:
            self._context = VariableContext(
                self._version,
                service_sid=self._solution['service_sid'],
                environment_sid=self._solution['environment_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the Variable resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the Variable resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the Variable resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def environment_sid(self):
        """
        :returns: The SID of the environment in which the variable exists
        :rtype: unicode
        """
        return self._properties['environment_sid']

    @property
    def key(self):
        """
        :returns: A string by which the Variable resource can be referenced
        :rtype: unicode
        """
        return self._properties['key']

    @property
    def value(self):
        """
        :returns: A string that contains the actual value of the variable
        :rtype: unicode
        """
        return self._properties['value']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the Variable resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the Variable resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Variable resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a VariableInstance

        :returns: Fetched VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        return self._proxy.fetch()

    def update(self, key=values.unset, value=values.unset):
        """
        Update the VariableInstance

        :param unicode key: A string by which the Variable resource can be referenced
        :param unicode value: A string that contains the actual value of the variable

        :returns: Updated VariableInstance
        :rtype: twilio.rest.serverless.v1.service.environment.variable.VariableInstance
        """
        return self._proxy.update(key=key, value=value, )

    def delete(self):
        """
        Deletes the VariableInstance

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.VariableInstance {}>'.format(context)
