from tracardi_plugin_sdk.action_runner import ActionRunner
from tracardi_plugin_sdk.domain.register import Plugin, Spec, MetaData
from tracardi_plugin_sdk.domain.result import Result


class JoinAction(ActionRunner):

    def __init__(self, **kwargs):
        pass

    async def run(self, payload):
        return Result(port="payload", value=payload)


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
            init={}
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