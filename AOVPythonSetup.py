def groupNodeSetup(parent):
    group = NodegraphAPI.CreateNode('Group', parent)
    group.addOutputPort('groupOut')
    groupReturn = group.getReturnPort('out')

    return group

def connectTwoNodes(nodeOutput, nodeInput, outValue, inValue):

    nodeOutPort = nodeOutput.getOutputPort(outValue)
    nodeInPort = nodeInput.getInputPort(inValue)
 
    nodeOutPort.connect(nodeInPort)

def connectInGroup(nodeOutput, group, nodeOut):

    nodeOutPort = nodeOutput.getOutputPort(nodeOut)
    groupReturn = group.getReturnPort('groupOut')

    nodeOutPort.connect(groupReturn)

root = NodegraphAPI.GetRootNode()

channel = 'diffuse'
lightExpression = 'C<RD>.*'

layerGroup =  groupNodeSetup(root)

arnoldChannelDefine = NodegraphAPI.CreateNode('ArnoldOutputChannelDefine', layerGroup)
arnoldChannelDefine.getParameter('name').setValue(channel, 0)
arnoldChannelDefine.getParameter('channel').setValue(channel, 0)
arnoldChannelDefine.getParameter('lightPathExpression').setValue('C<RD>.*', 0)

channelDefine = NodegraphAPI.CreateNode('RenderOutputDefine', layerGroup)
channelDefine.getParameter('outputName').setValue(channel, 0)

connectTwoNodes(arnoldChannelDefine, channelDefine, 'out', 'input')

channelDefine.getParameter('outputName').setValue(channel, 0)
channelDefine.checkDynamicParameters()

parameter = channelDefine.getParameter('args.renderSettings.outputs.outputName.rendererSettings.channel.value')
parameter.setValue(channel, 0)
parameter.finalizeValue()


connectInGroup(channelDefine, layerGroup, 'out')


renderSettings = NodegraphAPI.CreateNode('RenderSettings', root)

connectTwoNodes(layerGroup, renderSettings, 'groupOut', 'input')
