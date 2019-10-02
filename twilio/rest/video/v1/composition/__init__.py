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


class CompositionList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the CompositionList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.video.v1.composition.CompositionList
        :rtype: twilio.rest.video.v1.composition.CompositionList
        """
        super(CompositionList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Compositions'.format(**self._solution)

    def stream(self, status=values.unset, date_created_after=values.unset,
               date_created_before=values.unset, room_sid=values.unset, limit=None,
               page_size=None):
        """
        Streams CompositionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param CompositionInstance.Status status: Read only Composition resources with this status
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone
        :param unicode room_sid: Read only Composition resources with this Room SID
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.composition.CompositionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(
            status=status,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            room_sid=room_sid,
            page_size=limits['page_size'],
        )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, status=values.unset, date_created_after=values.unset,
             date_created_before=values.unset, room_sid=values.unset, limit=None,
             page_size=None):
        """
        Lists CompositionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param CompositionInstance.Status status: Read only Composition resources with this status
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone
        :param unicode room_sid: Read only Composition resources with this Room SID
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.video.v1.composition.CompositionInstance]
        """
        return list(self.stream(
            status=status,
            date_created_after=date_created_after,
            date_created_before=date_created_before,
            room_sid=room_sid,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, status=values.unset, date_created_after=values.unset,
             date_created_before=values.unset, room_sid=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of CompositionInstance records from the API.
        Request is executed immediately

        :param CompositionInstance.Status status: Read only Composition resources with this status
        :param datetime date_created_after: Read only Composition resources created on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone
        :param datetime date_created_before: Read only Composition resources created before this ISO 8601 date-time with time zone
        :param unicode room_sid: Read only Composition resources with this Room SID
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionPage
        """
        params = values.of({
            'Status': status,
            'DateCreatedAfter': serialize.iso8601_datetime(date_created_after),
            'DateCreatedBefore': serialize.iso8601_datetime(date_created_before),
            'RoomSid': room_sid,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return CompositionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CompositionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CompositionPage(self._version, response, self._solution)

    def create(self, room_sid, video_layout=values.unset,
               audio_sources=values.unset, audio_sources_excluded=values.unset,
               resolution=values.unset, format=values.unset,
               status_callback=values.unset, status_callback_method=values.unset,
               trim=values.unset):
        """
        Create a new CompositionInstance

        :param unicode room_sid: The SID of the Group Room with the media tracks to be used as composition sources
        :param dict video_layout: An object that describes the video layout of the composition
        :param unicode audio_sources: An array of track names from the same group room to merge
        :param unicode audio_sources_excluded: An array of track names to exclude
        :param unicode resolution: A string that describes the columns (width) and rows (height) of the generated composed video in pixels
        :param CompositionInstance.Format format: The container format of the composition's media files
        :param unicode status_callback: The URL we should call to send status information to your application
        :param unicode status_callback_method: The HTTP method we should use to call status_callback
        :param bool trim: Whether to clip the intervals where there is no active media in the composition

        :returns: Newly created CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """
        data = values.of({
            'RoomSid': room_sid,
            'VideoLayout': serialize.object(video_layout),
            'AudioSources': serialize.map(audio_sources, lambda e: e),
            'AudioSourcesExcluded': serialize.map(audio_sources_excluded, lambda e: e),
            'Resolution': resolution,
            'Format': format,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
            'Trim': trim,
        })

        payload = self._version.create(
            'POST',
            self._uri,
            data=data,
        )

        return CompositionInstance(self._version, payload, )

    def get(self, sid):
        """
        Constructs a CompositionContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.video.v1.composition.CompositionContext
        :rtype: twilio.rest.video.v1.composition.CompositionContext
        """
        return CompositionContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a CompositionContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.video.v1.composition.CompositionContext
        :rtype: twilio.rest.video.v1.composition.CompositionContext
        """
        return CompositionContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.CompositionList>'


class CompositionPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the CompositionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.video.v1.composition.CompositionPage
        :rtype: twilio.rest.video.v1.composition.CompositionPage
        """
        super(CompositionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CompositionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.video.v1.composition.CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """
        return CompositionInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Video.V1.CompositionPage>'


class CompositionContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sid):
        """
        Initialize the CompositionContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.video.v1.composition.CompositionContext
        :rtype: twilio.rest.video.v1.composition.CompositionContext
        """
        super(CompositionContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Compositions/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a CompositionInstance

        :returns: Fetched CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return CompositionInstance(self._version, payload, sid=self._solution['sid'], )

    def delete(self):
        """
        Deletes the CompositionInstance

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
        return '<Twilio.Video.V1.CompositionContext {}>'.format(context)


class CompositionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Status(object):
        ENQUEUED = "enqueued"
        PROCESSING = "processing"
        COMPLETED = "completed"
        DELETED = "deleted"
        FAILED = "failed"

    class Format(object):
        MP4 = "mp4"
        WEBM = "webm"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the CompositionInstance

        :returns: twilio.rest.video.v1.composition.CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """
        super(CompositionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'status': payload['status'],
            'date_created': deserialize.iso8601_datetime(payload['date_created']),
            'date_completed': payload['date_completed'],
            'date_deleted': payload['date_deleted'],
            'sid': payload['sid'],
            'room_sid': payload['room_sid'],
            'audio_sources': payload['audio_sources'],
            'audio_sources_excluded': payload['audio_sources_excluded'],
            'video_layout': payload['video_layout'],
            'resolution': payload['resolution'],
            'trim': payload['trim'],
            'format': payload['format'],
            'bitrate': deserialize.integer(payload['bitrate']),
            'size': deserialize.integer(payload['size']),
            'duration': deserialize.integer(payload['duration']),
            'url': payload['url'],
            'links': payload['links'],
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CompositionContext for this CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionContext
        """
        if self._context is None:
            self._context = CompositionContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def status(self):
        """
        :returns: The status of the composition
        :rtype: CompositionInstance.Status
        """
        return self._properties['status']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_completed(self):
        """
        :returns: Date when the media processing task finished
        :rtype: unicode
        """
        return self._properties['date_completed']

    @property
    def date_deleted(self):
        """
        :returns: The ISO 8601 date and time in GMT when the composition generated media was deleted
        :rtype: unicode
        """
        return self._properties['date_deleted']

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def room_sid(self):
        """
        :returns: The SID of the Group Room that generated the audio and video tracks used in the composition
        :rtype: unicode
        """
        return self._properties['room_sid']

    @property
    def audio_sources(self):
        """
        :returns: The array of track names to include in the composition
        :rtype: unicode
        """
        return self._properties['audio_sources']

    @property
    def audio_sources_excluded(self):
        """
        :returns: The array of track names to exclude from the composition
        :rtype: unicode
        """
        return self._properties['audio_sources_excluded']

    @property
    def video_layout(self):
        """
        :returns: An object that describes the video layout of the composition
        :rtype: dict
        """
        return self._properties['video_layout']

    @property
    def resolution(self):
        """
        :returns: The dimensions of the video image in pixels expressed as columns (width) and rows (height)
        :rtype: unicode
        """
        return self._properties['resolution']

    @property
    def trim(self):
        """
        :returns: Whether to remove intervals with no media
        :rtype: bool
        """
        return self._properties['trim']

    @property
    def format(self):
        """
        :returns: The container format of the composition's media files as specified in the POST request that created the Composition resource
        :rtype: CompositionInstance.Format
        """
        return self._properties['format']

    @property
    def bitrate(self):
        """
        :returns: The average bit rate of the composition's media
        :rtype: unicode
        """
        return self._properties['bitrate']

    @property
    def size(self):
        """
        :returns: The size of the composed media file in bytes
        :rtype: unicode
        """
        return self._properties['size']

    @property
    def duration(self):
        """
        :returns: The duration of the composition's media file in seconds
        :rtype: unicode
        """
        return self._properties['duration']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The URL of the media file associated with the composition
        :rtype: unicode
        """
        return self._properties['links']

    def fetch(self):
        """
        Fetch a CompositionInstance

        :returns: Fetched CompositionInstance
        :rtype: twilio.rest.video.v1.composition.CompositionInstance
        """
        return self._proxy.fetch()

    def delete(self):
        """
        Deletes the CompositionInstance

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
        return '<Twilio.Video.V1.CompositionInstance {}>'.format(context)
