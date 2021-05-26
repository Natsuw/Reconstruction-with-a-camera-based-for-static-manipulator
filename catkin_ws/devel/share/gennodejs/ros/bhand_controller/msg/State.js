// Auto-generated. Do not edit!

// (in-package bhand_controller.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class State {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.state = null;
      this.control_mode = null;
      this.hand_initialized = null;
      this.desired_freq = null;
      this.real_freq = null;
      this.state_description = null;
      this.temp_f1 = null;
      this.temp_f2 = null;
      this.temp_f3 = null;
      this.temp_spread = null;
    }
    else {
      if (initObj.hasOwnProperty('state')) {
        this.state = initObj.state
      }
      else {
        this.state = 0;
      }
      if (initObj.hasOwnProperty('control_mode')) {
        this.control_mode = initObj.control_mode
      }
      else {
        this.control_mode = '';
      }
      if (initObj.hasOwnProperty('hand_initialized')) {
        this.hand_initialized = initObj.hand_initialized
      }
      else {
        this.hand_initialized = false;
      }
      if (initObj.hasOwnProperty('desired_freq')) {
        this.desired_freq = initObj.desired_freq
      }
      else {
        this.desired_freq = 0.0;
      }
      if (initObj.hasOwnProperty('real_freq')) {
        this.real_freq = initObj.real_freq
      }
      else {
        this.real_freq = 0.0;
      }
      if (initObj.hasOwnProperty('state_description')) {
        this.state_description = initObj.state_description
      }
      else {
        this.state_description = '';
      }
      if (initObj.hasOwnProperty('temp_f1')) {
        this.temp_f1 = initObj.temp_f1
      }
      else {
        this.temp_f1 = new Array(2).fill(0);
      }
      if (initObj.hasOwnProperty('temp_f2')) {
        this.temp_f2 = initObj.temp_f2
      }
      else {
        this.temp_f2 = new Array(2).fill(0);
      }
      if (initObj.hasOwnProperty('temp_f3')) {
        this.temp_f3 = initObj.temp_f3
      }
      else {
        this.temp_f3 = new Array(2).fill(0);
      }
      if (initObj.hasOwnProperty('temp_spread')) {
        this.temp_spread = initObj.temp_spread
      }
      else {
        this.temp_spread = new Array(2).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type State
    // Serialize message field [state]
    bufferOffset = _serializer.int32(obj.state, buffer, bufferOffset);
    // Serialize message field [control_mode]
    bufferOffset = _serializer.string(obj.control_mode, buffer, bufferOffset);
    // Serialize message field [hand_initialized]
    bufferOffset = _serializer.bool(obj.hand_initialized, buffer, bufferOffset);
    // Serialize message field [desired_freq]
    bufferOffset = _serializer.float32(obj.desired_freq, buffer, bufferOffset);
    // Serialize message field [real_freq]
    bufferOffset = _serializer.float32(obj.real_freq, buffer, bufferOffset);
    // Serialize message field [state_description]
    bufferOffset = _serializer.string(obj.state_description, buffer, bufferOffset);
    // Check that the constant length array field [temp_f1] has the right length
    if (obj.temp_f1.length !== 2) {
      throw new Error('Unable to serialize array field temp_f1 - length must be 2')
    }
    // Serialize message field [temp_f1]
    bufferOffset = _arraySerializer.float32(obj.temp_f1, buffer, bufferOffset, 2);
    // Check that the constant length array field [temp_f2] has the right length
    if (obj.temp_f2.length !== 2) {
      throw new Error('Unable to serialize array field temp_f2 - length must be 2')
    }
    // Serialize message field [temp_f2]
    bufferOffset = _arraySerializer.float32(obj.temp_f2, buffer, bufferOffset, 2);
    // Check that the constant length array field [temp_f3] has the right length
    if (obj.temp_f3.length !== 2) {
      throw new Error('Unable to serialize array field temp_f3 - length must be 2')
    }
    // Serialize message field [temp_f3]
    bufferOffset = _arraySerializer.float32(obj.temp_f3, buffer, bufferOffset, 2);
    // Check that the constant length array field [temp_spread] has the right length
    if (obj.temp_spread.length !== 2) {
      throw new Error('Unable to serialize array field temp_spread - length must be 2')
    }
    // Serialize message field [temp_spread]
    bufferOffset = _arraySerializer.float32(obj.temp_spread, buffer, bufferOffset, 2);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type State
    let len;
    let data = new State(null);
    // Deserialize message field [state]
    data.state = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [control_mode]
    data.control_mode = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [hand_initialized]
    data.hand_initialized = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [desired_freq]
    data.desired_freq = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [real_freq]
    data.real_freq = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [state_description]
    data.state_description = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [temp_f1]
    data.temp_f1 = _arrayDeserializer.float32(buffer, bufferOffset, 2)
    // Deserialize message field [temp_f2]
    data.temp_f2 = _arrayDeserializer.float32(buffer, bufferOffset, 2)
    // Deserialize message field [temp_f3]
    data.temp_f3 = _arrayDeserializer.float32(buffer, bufferOffset, 2)
    // Deserialize message field [temp_spread]
    data.temp_spread = _arrayDeserializer.float32(buffer, bufferOffset, 2)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.control_mode.length;
    length += object.state_description.length;
    return length + 53;
  }

  static datatype() {
    // Returns string type for a message object
    return 'bhand_controller/State';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '43dbdaf8df84846b4d0203e0d6845e11';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # constants
    int32 INIT_STATE = 100
    int32 STANDBY_STATE = 200
    int32 READY_STATE = 300
    int32 EMERGENCY_STATE = 400
    int32 FAILURE_STATE = 500
    int32 SHUTDOWN_STATE = 600
    
    
    # state of the component
    int32 state
    # Control mode
    string control_mode
    # Flag active when the hand position has been initialized
    bool hand_initialized
    # desired control loop frecuency
    float32 desired_freq
    # real frecuency 
    float32 real_freq
    # Description of the state
    string state_description
    # [temp_motor, temp_puck]
    float32[2] temp_f1
    # [temp_motor, temp_puck]
    float32[2] temp_f2
    # [temp_motor, temp_puck]
    float32[2] temp_f3
    # [temp_motor, temp_puck]
    float32[2] temp_spread
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new State(null);
    if (msg.state !== undefined) {
      resolved.state = msg.state;
    }
    else {
      resolved.state = 0
    }

    if (msg.control_mode !== undefined) {
      resolved.control_mode = msg.control_mode;
    }
    else {
      resolved.control_mode = ''
    }

    if (msg.hand_initialized !== undefined) {
      resolved.hand_initialized = msg.hand_initialized;
    }
    else {
      resolved.hand_initialized = false
    }

    if (msg.desired_freq !== undefined) {
      resolved.desired_freq = msg.desired_freq;
    }
    else {
      resolved.desired_freq = 0.0
    }

    if (msg.real_freq !== undefined) {
      resolved.real_freq = msg.real_freq;
    }
    else {
      resolved.real_freq = 0.0
    }

    if (msg.state_description !== undefined) {
      resolved.state_description = msg.state_description;
    }
    else {
      resolved.state_description = ''
    }

    if (msg.temp_f1 !== undefined) {
      resolved.temp_f1 = msg.temp_f1;
    }
    else {
      resolved.temp_f1 = new Array(2).fill(0)
    }

    if (msg.temp_f2 !== undefined) {
      resolved.temp_f2 = msg.temp_f2;
    }
    else {
      resolved.temp_f2 = new Array(2).fill(0)
    }

    if (msg.temp_f3 !== undefined) {
      resolved.temp_f3 = msg.temp_f3;
    }
    else {
      resolved.temp_f3 = new Array(2).fill(0)
    }

    if (msg.temp_spread !== undefined) {
      resolved.temp_spread = msg.temp_spread;
    }
    else {
      resolved.temp_spread = new Array(2).fill(0)
    }

    return resolved;
    }
};

// Constants for message
State.Constants = {
  INIT_STATE: 100,
  STANDBY_STATE: 200,
  READY_STATE: 300,
  EMERGENCY_STATE: 400,
  FAILURE_STATE: 500,
  SHUTDOWN_STATE: 600,
}

module.exports = State;
