
"use strict";

let Digital = require('./Digital.js');
let Analog = require('./Analog.js');
let MasterboardDataMsg = require('./MasterboardDataMsg.js');
let ToolDataMsg = require('./ToolDataMsg.js');
let RobotStateRTMsg = require('./RobotStateRTMsg.js');
let IOStates = require('./IOStates.js');
let RobotModeDataMsg = require('./RobotModeDataMsg.js');

module.exports = {
  Digital: Digital,
  Analog: Analog,
  MasterboardDataMsg: MasterboardDataMsg,
  ToolDataMsg: ToolDataMsg,
  RobotStateRTMsg: RobotStateRTMsg,
  IOStates: IOStates,
  RobotModeDataMsg: RobotModeDataMsg,
};
