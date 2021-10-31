from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result
from tracardi_add_joint_operation.model.models import Module


def join(array, string):
    return string.join(array)


class JoinAction(ActionRunner):

    def __init__(self, **kwargs):
        self.config = Module(**kwargs)

    async def run(self, payload):
        dot = self._get_dot_accessor(payload)
        array = dot[self.config.array]
        return Result(port="payload", value=join(array, self.config.join_string))


def register() -> Plugin:
    return Plugin(
        start=False,
        spec=Spec(
            module='tracardi_add_joint_operation.plugin',
            className='JoinAction',
            inputs=["payload"],
            outputs=['payload'],
            version='0.1',
            license="MIT",
            author="Patryk Migaj",
            init={"join_string": "None"}
        ),
        metadata=MetaData(
            name='tracardi-add-joint-operation',
            desc='Extend an existing plug-in that appends and removes items from the list. And add an operation that joins the items in the list and outputs joint string',
            type='flowNode',
            width=200,
            height=100,
            icon='icon',
            group=["General"]
        )
    )
