// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

/** Defines the event types generated by SignalingClient and the underlying WebSocket connection. */
export enum SignalingClientEventType {
  WebSocketConnecting,
  WebSocketOpen,
  WebSocketError,
  WebSocketClosing,
  WebSocketClosed,
  WebSocketFailed,
  WebSocketMessage,
  WebSocketSendMessageFailure,
  WebSocketSentMessage,
  ProtocolDecodeFailure,
  ReceivedSignalFrame,
  WebSocketSkippedMessage,
}

export default SignalingClientEventType;
