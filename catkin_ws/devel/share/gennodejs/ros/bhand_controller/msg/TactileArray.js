// Auto-generated. Do not edit!

// (in-package bhand_controller.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class TactileArray {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.finger1 = null;
      this.finger2 = null;
      this.finger3 = null;
      this.palm = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('finger1')) {
        this.finger1 = initObj.finger1
      }
      else {
        this.finger1 = [];
      }
      if (initObj.hasOwnProperty('finger2')) {
        this.finger2 = initObj.finger2
      }
      else {
        this.finger2 = [];
      }
      if (initObj.hasOwnProperty('finger3')) {
        this.finger3 = initObj.finger3
      }
      else {
        this.finger3 = [];
      }
      if (initObj.hasOwnProperty('palm')) {
        this.palm = initObj.palm
      }
      else {
        this.palm = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type TactileArray
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [finger1]
    bufferOffset = _arraySerializer.float32(obj.finger1, buffer, bufferOffset, null);
    // Serialize message field [finger2]
    bufferOffset = _arraySerializer.float32(obj.finger2, buffer, bufferOffset, null);
    // Serialize message field [finger3]
    bufferOffset = _arraySerializer.float32(obj.finger3, buffer, bufferOffset, null);
    // Serialize message field [palm]
    bufferOffset = _arraySerializer.float32(obj.palm, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type TactileArray
    let len;
    let data = new TactileArray(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [finger1]
    data.finger1 = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [finger2]
    data.finger2 = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [finger3]
    data.finger3 = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [palm]
    data.palm = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 4 * object.finger1.length;
    length += 4 * object.finger2.length;
    length += 4 * object.finger3.length;
    length += 4 * object.palm.length;
    return length + 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'bhand_controller/TactileArray';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c13cabdf3bf4be5ec7e27247c9867860';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    # Units in N/cm2
    # array sensor of the finger 1
    float32[] finger1
    # array sensor of the finger 2
    float32[] finger2
    # array sensor of the finger 3
    float32[] finger3
    # array sensor of the palm
    float32[] palm
    
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new TactileArray(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.finger1 !== undefined) {
      resolved.finger1 = msg.finger1;
    }
    else {
      resolved.finger1 = []
    }

    if (msg.finger2 !== undefined) {
      resolved.finger2 = msg.finger2;
    }
    else {
      resolved.finger2 = []
    }

    if (msg.finger3 !== undefined) {
      resolved.finger3 = msg.finger3;
    }
    else {
      resolved.finger3 = []
    }

    if (msg.palm !== undefined) {
      resolved.palm = msg.palm;
    }
    else {
      resolved.palm = []
    }

    return resolved;
    }
};

module.exports = TactileArray;
