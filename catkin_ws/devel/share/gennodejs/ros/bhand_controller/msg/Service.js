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

class Service {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Service
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Service
    let len;
    let data = new Service(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a message object
    return 'bhand_controller/Service';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c09093085862e16e122942cf27b990b9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # constants
    int32 INIT_HAND = 1
    int32 CLOSE_GRASP = 2
    int32 OPEN_GRASP = 3
    int32 SET_GRASP_1 = 4
    int32 SET_GRASP_2 = 5
    int32 CLOSE_HALF_GRASP = 6
    int32 TARE_FTS = 7
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Service(null);
    return resolved;
    }
};

// Constants for message
Service.Constants = {
  INIT_HAND: 1,
  CLOSE_GRASP: 2,
  OPEN_GRASP: 3,
  SET_GRASP_1: 4,
  SET_GRASP_2: 5,
  CLOSE_HALF_GRASP: 6,
  TARE_FTS: 7,
}

module.exports = Service;
