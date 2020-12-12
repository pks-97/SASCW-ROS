// Auto-generated. Do not edit!

// (in-package fovis_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class FovisInfo {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.change_reference_frame = null;
      this.fast_threshold = null;
      this.num_total_detected_keypoints = null;
      this.num_detected_keypoints = null;
      this.num_total_keypoints = null;
      this.num_keypoints = null;
      this.motion_estimate_status_code = null;
      this.motion_estimate_status = null;
      this.motion_estimate_valid = null;
      this.num_matches = null;
      this.num_inliers = null;
      this.num_reprojection_failures = null;
      this.runtime = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('change_reference_frame')) {
        this.change_reference_frame = initObj.change_reference_frame
      }
      else {
        this.change_reference_frame = false;
      }
      if (initObj.hasOwnProperty('fast_threshold')) {
        this.fast_threshold = initObj.fast_threshold
      }
      else {
        this.fast_threshold = 0;
      }
      if (initObj.hasOwnProperty('num_total_detected_keypoints')) {
        this.num_total_detected_keypoints = initObj.num_total_detected_keypoints
      }
      else {
        this.num_total_detected_keypoints = 0;
      }
      if (initObj.hasOwnProperty('num_detected_keypoints')) {
        this.num_detected_keypoints = initObj.num_detected_keypoints
      }
      else {
        this.num_detected_keypoints = [];
      }
      if (initObj.hasOwnProperty('num_total_keypoints')) {
        this.num_total_keypoints = initObj.num_total_keypoints
      }
      else {
        this.num_total_keypoints = 0;
      }
      if (initObj.hasOwnProperty('num_keypoints')) {
        this.num_keypoints = initObj.num_keypoints
      }
      else {
        this.num_keypoints = [];
      }
      if (initObj.hasOwnProperty('motion_estimate_status_code')) {
        this.motion_estimate_status_code = initObj.motion_estimate_status_code
      }
      else {
        this.motion_estimate_status_code = 0;
      }
      if (initObj.hasOwnProperty('motion_estimate_status')) {
        this.motion_estimate_status = initObj.motion_estimate_status
      }
      else {
        this.motion_estimate_status = '';
      }
      if (initObj.hasOwnProperty('motion_estimate_valid')) {
        this.motion_estimate_valid = initObj.motion_estimate_valid
      }
      else {
        this.motion_estimate_valid = false;
      }
      if (initObj.hasOwnProperty('num_matches')) {
        this.num_matches = initObj.num_matches
      }
      else {
        this.num_matches = 0;
      }
      if (initObj.hasOwnProperty('num_inliers')) {
        this.num_inliers = initObj.num_inliers
      }
      else {
        this.num_inliers = 0;
      }
      if (initObj.hasOwnProperty('num_reprojection_failures')) {
        this.num_reprojection_failures = initObj.num_reprojection_failures
      }
      else {
        this.num_reprojection_failures = 0;
      }
      if (initObj.hasOwnProperty('runtime')) {
        this.runtime = initObj.runtime
      }
      else {
        this.runtime = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FovisInfo
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [change_reference_frame]
    bufferOffset = _serializer.bool(obj.change_reference_frame, buffer, bufferOffset);
    // Serialize message field [fast_threshold]
    bufferOffset = _serializer.int32(obj.fast_threshold, buffer, bufferOffset);
    // Serialize message field [num_total_detected_keypoints]
    bufferOffset = _serializer.int32(obj.num_total_detected_keypoints, buffer, bufferOffset);
    // Serialize message field [num_detected_keypoints]
    bufferOffset = _arraySerializer.int32(obj.num_detected_keypoints, buffer, bufferOffset, null);
    // Serialize message field [num_total_keypoints]
    bufferOffset = _serializer.int32(obj.num_total_keypoints, buffer, bufferOffset);
    // Serialize message field [num_keypoints]
    bufferOffset = _arraySerializer.int32(obj.num_keypoints, buffer, bufferOffset, null);
    // Serialize message field [motion_estimate_status_code]
    bufferOffset = _serializer.int32(obj.motion_estimate_status_code, buffer, bufferOffset);
    // Serialize message field [motion_estimate_status]
    bufferOffset = _serializer.string(obj.motion_estimate_status, buffer, bufferOffset);
    // Serialize message field [motion_estimate_valid]
    bufferOffset = _serializer.bool(obj.motion_estimate_valid, buffer, bufferOffset);
    // Serialize message field [num_matches]
    bufferOffset = _serializer.int32(obj.num_matches, buffer, bufferOffset);
    // Serialize message field [num_inliers]
    bufferOffset = _serializer.int32(obj.num_inliers, buffer, bufferOffset);
    // Serialize message field [num_reprojection_failures]
    bufferOffset = _serializer.int32(obj.num_reprojection_failures, buffer, bufferOffset);
    // Serialize message field [runtime]
    bufferOffset = _serializer.float64(obj.runtime, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FovisInfo
    let len;
    let data = new FovisInfo(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [change_reference_frame]
    data.change_reference_frame = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [fast_threshold]
    data.fast_threshold = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [num_total_detected_keypoints]
    data.num_total_detected_keypoints = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [num_detected_keypoints]
    data.num_detected_keypoints = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [num_total_keypoints]
    data.num_total_keypoints = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [num_keypoints]
    data.num_keypoints = _arrayDeserializer.int32(buffer, bufferOffset, null)
    // Deserialize message field [motion_estimate_status_code]
    data.motion_estimate_status_code = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [motion_estimate_status]
    data.motion_estimate_status = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [motion_estimate_valid]
    data.motion_estimate_valid = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [num_matches]
    data.num_matches = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [num_inliers]
    data.num_inliers = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [num_reprojection_failures]
    data.num_reprojection_failures = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [runtime]
    data.runtime = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    length += 4 * object.num_detected_keypoints.length;
    length += 4 * object.num_keypoints.length;
    length += object.motion_estimate_status.length;
    return length + 50;
  }

  static datatype() {
    // Returns string type for a message object
    return 'fovis_ros/FovisInfo';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2e964f4d41f3876e14c50795334bf34c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Internal information on the
    # fovis algorithm parameters
    # and results
    
    Header header
    
    # True if in the next run the reference 
    # frame will be changed. This is the case
    # when the number of inliers drops below
    # a threshold or the previous motion estimate
    # failed in last motion estimation.
    bool change_reference_frame
    
    # The threshold that is currently 
    # used for the FAST feature detector.
    int32 fast_threshold
    
    # total number of detected keypoints in raw image
    int32 num_total_detected_keypoints
    
    # same as above per pyramid level, starting at 0
    int32[] num_detected_keypoints
    
    # total number of keypoints after bucketing and
    # edge and depth filter
    int32 num_total_keypoints
    
    # same as above per pyramid level, starting at 0
    int32[] num_keypoints
    
    # info from motion estimator
    int32 motion_estimate_status_code
    string motion_estimate_status
    bool motion_estimate_valid
    int32 num_matches
    int32 num_inliers
    int32 num_reprojection_failures
    
    # runtime of last iteration in seconds
    float64 runtime
    
    
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
    # 0: no frame
    # 1: global frame
    string frame_id
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FovisInfo(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.change_reference_frame !== undefined) {
      resolved.change_reference_frame = msg.change_reference_frame;
    }
    else {
      resolved.change_reference_frame = false
    }

    if (msg.fast_threshold !== undefined) {
      resolved.fast_threshold = msg.fast_threshold;
    }
    else {
      resolved.fast_threshold = 0
    }

    if (msg.num_total_detected_keypoints !== undefined) {
      resolved.num_total_detected_keypoints = msg.num_total_detected_keypoints;
    }
    else {
      resolved.num_total_detected_keypoints = 0
    }

    if (msg.num_detected_keypoints !== undefined) {
      resolved.num_detected_keypoints = msg.num_detected_keypoints;
    }
    else {
      resolved.num_detected_keypoints = []
    }

    if (msg.num_total_keypoints !== undefined) {
      resolved.num_total_keypoints = msg.num_total_keypoints;
    }
    else {
      resolved.num_total_keypoints = 0
    }

    if (msg.num_keypoints !== undefined) {
      resolved.num_keypoints = msg.num_keypoints;
    }
    else {
      resolved.num_keypoints = []
    }

    if (msg.motion_estimate_status_code !== undefined) {
      resolved.motion_estimate_status_code = msg.motion_estimate_status_code;
    }
    else {
      resolved.motion_estimate_status_code = 0
    }

    if (msg.motion_estimate_status !== undefined) {
      resolved.motion_estimate_status = msg.motion_estimate_status;
    }
    else {
      resolved.motion_estimate_status = ''
    }

    if (msg.motion_estimate_valid !== undefined) {
      resolved.motion_estimate_valid = msg.motion_estimate_valid;
    }
    else {
      resolved.motion_estimate_valid = false
    }

    if (msg.num_matches !== undefined) {
      resolved.num_matches = msg.num_matches;
    }
    else {
      resolved.num_matches = 0
    }

    if (msg.num_inliers !== undefined) {
      resolved.num_inliers = msg.num_inliers;
    }
    else {
      resolved.num_inliers = 0
    }

    if (msg.num_reprojection_failures !== undefined) {
      resolved.num_reprojection_failures = msg.num_reprojection_failures;
    }
    else {
      resolved.num_reprojection_failures = 0
    }

    if (msg.runtime !== undefined) {
      resolved.runtime = msg.runtime;
    }
    else {
      resolved.runtime = 0.0
    }

    return resolved;
    }
};

module.exports = FovisInfo;
