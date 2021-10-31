from tracardi.domain.context import Context
from tracardi.domain.entity import Entity
from tracardi.domain.event import Event
from tracardi.domain.profile import Profile
from tracardi.domain.session import Session
from tracardi_plugin_sdk.service.plugin_runner import run_plugin

from tracardi_add_joint_operation.plugin import JoinAction

init = {"join_string": ",",
        "array": "event@id"}
payload = {}
profile = Profile(id="profile-id")
event = Event(id="event-id",
              type="event-type",
              profile=profile,
              session=Session(id="session-id"),
              source=Entity(id="source-id"),
              context=Context())
result = run_plugin(JoinAction, init, payload,
                    profile,event=event)

print("OUTPUT:", result.output)
print("PROFILE:", result.profile)
