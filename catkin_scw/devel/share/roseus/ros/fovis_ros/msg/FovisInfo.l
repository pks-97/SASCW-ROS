;; Auto-generated. Do not edit!


(when (boundp 'fovis_ros::FovisInfo)
  (if (not (find-package "FOVIS_ROS"))
    (make-package "FOVIS_ROS"))
  (shadow 'FovisInfo (find-package "FOVIS_ROS")))
(unless (find-package "FOVIS_ROS::FOVISINFO")
  (make-package "FOVIS_ROS::FOVISINFO"))

(in-package "ROS")
;;//! \htmlinclude FovisInfo.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass fovis_ros::FovisInfo
  :super ros::object
  :slots (_header _change_reference_frame _fast_threshold _num_total_detected_keypoints _num_detected_keypoints _num_total_keypoints _num_keypoints _motion_estimate_status_code _motion_estimate_status _motion_estimate_valid _num_matches _num_inliers _num_reprojection_failures _runtime ))

(defmethod fovis_ros::FovisInfo
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:change_reference_frame __change_reference_frame) nil)
    ((:fast_threshold __fast_threshold) 0)
    ((:num_total_detected_keypoints __num_total_detected_keypoints) 0)
    ((:num_detected_keypoints __num_detected_keypoints) (make-array 0 :initial-element 0 :element-type :integer))
    ((:num_total_keypoints __num_total_keypoints) 0)
    ((:num_keypoints __num_keypoints) (make-array 0 :initial-element 0 :element-type :integer))
    ((:motion_estimate_status_code __motion_estimate_status_code) 0)
    ((:motion_estimate_status __motion_estimate_status) "")
    ((:motion_estimate_valid __motion_estimate_valid) nil)
    ((:num_matches __num_matches) 0)
    ((:num_inliers __num_inliers) 0)
    ((:num_reprojection_failures __num_reprojection_failures) 0)
    ((:runtime __runtime) 0.0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _change_reference_frame __change_reference_frame)
   (setq _fast_threshold (round __fast_threshold))
   (setq _num_total_detected_keypoints (round __num_total_detected_keypoints))
   (setq _num_detected_keypoints __num_detected_keypoints)
   (setq _num_total_keypoints (round __num_total_keypoints))
   (setq _num_keypoints __num_keypoints)
   (setq _motion_estimate_status_code (round __motion_estimate_status_code))
   (setq _motion_estimate_status (string __motion_estimate_status))
   (setq _motion_estimate_valid __motion_estimate_valid)
   (setq _num_matches (round __num_matches))
   (setq _num_inliers (round __num_inliers))
   (setq _num_reprojection_failures (round __num_reprojection_failures))
   (setq _runtime (float __runtime))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:change_reference_frame
   (&optional __change_reference_frame)
   (if __change_reference_frame (setq _change_reference_frame __change_reference_frame)) _change_reference_frame)
  (:fast_threshold
   (&optional __fast_threshold)
   (if __fast_threshold (setq _fast_threshold __fast_threshold)) _fast_threshold)
  (:num_total_detected_keypoints
   (&optional __num_total_detected_keypoints)
   (if __num_total_detected_keypoints (setq _num_total_detected_keypoints __num_total_detected_keypoints)) _num_total_detected_keypoints)
  (:num_detected_keypoints
   (&optional __num_detected_keypoints)
   (if __num_detected_keypoints (setq _num_detected_keypoints __num_detected_keypoints)) _num_detected_keypoints)
  (:num_total_keypoints
   (&optional __num_total_keypoints)
   (if __num_total_keypoints (setq _num_total_keypoints __num_total_keypoints)) _num_total_keypoints)
  (:num_keypoints
   (&optional __num_keypoints)
   (if __num_keypoints (setq _num_keypoints __num_keypoints)) _num_keypoints)
  (:motion_estimate_status_code
   (&optional __motion_estimate_status_code)
   (if __motion_estimate_status_code (setq _motion_estimate_status_code __motion_estimate_status_code)) _motion_estimate_status_code)
  (:motion_estimate_status
   (&optional __motion_estimate_status)
   (if __motion_estimate_status (setq _motion_estimate_status __motion_estimate_status)) _motion_estimate_status)
  (:motion_estimate_valid
   (&optional __motion_estimate_valid)
   (if __motion_estimate_valid (setq _motion_estimate_valid __motion_estimate_valid)) _motion_estimate_valid)
  (:num_matches
   (&optional __num_matches)
   (if __num_matches (setq _num_matches __num_matches)) _num_matches)
  (:num_inliers
   (&optional __num_inliers)
   (if __num_inliers (setq _num_inliers __num_inliers)) _num_inliers)
  (:num_reprojection_failures
   (&optional __num_reprojection_failures)
   (if __num_reprojection_failures (setq _num_reprojection_failures __num_reprojection_failures)) _num_reprojection_failures)
  (:runtime
   (&optional __runtime)
   (if __runtime (setq _runtime __runtime)) _runtime)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; bool _change_reference_frame
    1
    ;; int32 _fast_threshold
    4
    ;; int32 _num_total_detected_keypoints
    4
    ;; int32[] _num_detected_keypoints
    (* 4    (length _num_detected_keypoints)) 4
    ;; int32 _num_total_keypoints
    4
    ;; int32[] _num_keypoints
    (* 4    (length _num_keypoints)) 4
    ;; int32 _motion_estimate_status_code
    4
    ;; string _motion_estimate_status
    4 (length _motion_estimate_status)
    ;; bool _motion_estimate_valid
    1
    ;; int32 _num_matches
    4
    ;; int32 _num_inliers
    4
    ;; int32 _num_reprojection_failures
    4
    ;; float64 _runtime
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; bool _change_reference_frame
       (if _change_reference_frame (write-byte -1 s) (write-byte 0 s))
     ;; int32 _fast_threshold
       (write-long _fast_threshold s)
     ;; int32 _num_total_detected_keypoints
       (write-long _num_total_detected_keypoints s)
     ;; int32[] _num_detected_keypoints
     (write-long (length _num_detected_keypoints) s)
     (dotimes (i (length _num_detected_keypoints))
       (write-long (elt _num_detected_keypoints i) s)
       )
     ;; int32 _num_total_keypoints
       (write-long _num_total_keypoints s)
     ;; int32[] _num_keypoints
     (write-long (length _num_keypoints) s)
     (dotimes (i (length _num_keypoints))
       (write-long (elt _num_keypoints i) s)
       )
     ;; int32 _motion_estimate_status_code
       (write-long _motion_estimate_status_code s)
     ;; string _motion_estimate_status
       (write-long (length _motion_estimate_status) s) (princ _motion_estimate_status s)
     ;; bool _motion_estimate_valid
       (if _motion_estimate_valid (write-byte -1 s) (write-byte 0 s))
     ;; int32 _num_matches
       (write-long _num_matches s)
     ;; int32 _num_inliers
       (write-long _num_inliers s)
     ;; int32 _num_reprojection_failures
       (write-long _num_reprojection_failures s)
     ;; float64 _runtime
       (sys::poke _runtime (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; bool _change_reference_frame
     (setq _change_reference_frame (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int32 _fast_threshold
     (setq _fast_threshold (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _num_total_detected_keypoints
     (setq _num_total_detected_keypoints (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32[] _num_detected_keypoints
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _num_detected_keypoints (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _num_detected_keypoints i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32 _num_total_keypoints
     (setq _num_total_keypoints (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32[] _num_keypoints
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _num_keypoints (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _num_keypoints i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;; int32 _motion_estimate_status_code
     (setq _motion_estimate_status_code (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; string _motion_estimate_status
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _motion_estimate_status (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; bool _motion_estimate_valid
     (setq _motion_estimate_valid (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int32 _num_matches
     (setq _num_matches (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _num_inliers
     (setq _num_inliers (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _num_reprojection_failures
     (setq _num_reprojection_failures (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; float64 _runtime
     (setq _runtime (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get fovis_ros::FovisInfo :md5sum-) "2e964f4d41f3876e14c50795334bf34c")
(setf (get fovis_ros::FovisInfo :datatype-) "fovis_ros/FovisInfo")
(setf (get fovis_ros::FovisInfo :definition-)
      "# Internal information on the
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

")



(provide :fovis_ros/FovisInfo "2e964f4d41f3876e14c50795334bf34c")


