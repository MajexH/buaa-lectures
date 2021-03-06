# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import landing_pb2 as landing__pb2


class LandingServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.talk = channel.unary_unary(
        '/LandingService/talk',
        request_serializer=landing__pb2.TalkRequest.SerializeToString,
        response_deserializer=landing__pb2.TalkResponse.FromString,
        )
    self.talkChunk = channel.unary_stream(
        '/LandingService/talkChunk',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=landing__pb2.TalkChunk.FromString,
        )


class LandingServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def talk(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def talkChunk(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LandingServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'talk': grpc.unary_unary_rpc_method_handler(
          servicer.talk,
          request_deserializer=landing__pb2.TalkRequest.FromString,
          response_serializer=landing__pb2.TalkResponse.SerializeToString,
      ),
      'talkChunk': grpc.unary_stream_rpc_method_handler(
          servicer.talkChunk,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=landing__pb2.TalkChunk.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'LandingService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
