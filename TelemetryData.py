import struct
import ParticipantInfo

#Model class for Telemetry Packages
#Still a lot of data to read
class TelemetryData:
    def __init__(self, package):
        self.build_version = struct.unpack('H', package[0:2])[0]
        self.package_type = struct.unpack('B', package[2:3])[0] & 0x03
        self.sequence_number = (struct.unpack('B', package[2:3])[0] & 0xFC) << 2
        #Game states
        self.game_state = struct.unpack('B', package[3:4])[0] & 0x07
        self.session_state = (struct.unpack('B', package[3:4])[0] & 0xF8) << 4
        #Participant Info
        self.viewed_participant_index = struct.unpack('b', package[4:5])[0]
        self.num_participants = struct.unpack('b', package[5:6])[0]
        #Unfiltered input
        self.unfiltered_throttle = struct.unpack('B', package[6:7])[0]
        self.unfiltered_brake = struct.unpack('B', package[7:8])[0]
        self.unfiltered_steering = struct.unpack('b', package[8:9])[0]
        self.unfiltered_clutch = struct.unpack('B', package[9:10])[0]
        self.race_state_flags = struct.unpack('B', package[10:11])[0]
        #Event Information
        self.laps_in_event = struct.unpack('B', package[11:12])[0]
        #Timings
        self.best_lap_time = struct.unpack('f', package[12:16])[0]
        self.last_lap_time = struct.unpack('f', package[16:20])[0]
        self.current_time = struct.unpack('f', package[20:24])[0]
        self.split_time_ahead = struct.unpack('f', package[24:28])[0]
        self.split_time_behind = struct.unpack('f', package[28:32])[0]
        self.split_time = struct.unpack('f', package[32:36])[0]
        self.event_time_remaining = struct.unpack('f', package[36:40])[0]
        self.personal_fastest_lap_time = struct.unpack('f', package[40:44])[0]
        self.world_fastest_lap_time = struct.unpack('f', package[44:48])[0]
        self.current_sector1_time = struct.unpack('f', package[48:52])[0]
        self.current_sector2_time = struct.unpack('f', package[52:56])[0]
        self.current_sector3_time = struct.unpack('f', package[56:60])[0]
        self.fastest_sector1_time = struct.unpack('f', package[60:64])[0]
        self.fastest_sector2_time = struct.unpack('f', package[64:68])[0]
        self.fastest_sector3_time = struct.unpack('f', package[68:72])[0]
        self.personal_fastest_sector1_time = struct.unpack('f', package[72:76])[0]
        self.personal_fastest_sector2_time = struct.unpack('f', package[76:80])[0]
        self.personal_fastest_sector3_time = struct.unpack('f', package[80:84])[0]
        self.world_fastest_sector1_time = struct.unpack('f', package[84:88])[0]
        self.world_fastest_sector2_time = struct.unpack('f', package[88:92])[0]
        self.world_fastest_sector3_time = struct.unpack('f', package[92:96])[0]
        #Joy Pad
        self.joy_pad = struct.unpack('H', package[96:98])[0]
        #Flags
        self.highest_flag = struct.unpack('B', package[98:99])[0]
        #Pit info
        self.pit_mode_schedule = struct.unpack('B', package[99:100])[0]
        #Car State
        self.oil_temp_celsius = struct.unpack('h', package[100:102])[0]
        self.oil_pressure_kpa = struct.unpack('H', package[102:104])[0]
        self.water_temp_celsius = struct.unpack('h', package[104:106])[0]
        self.water_pressure_kpa = struct.unpack('H', package[106:108])[0]
        self.fuel_pressure_kpa = struct.unpack('H', package[108:110])[0]
        self.car_flags = struct.unpack('B', package[110:111])[0]
        self.fuel_capacity = struct.unpack('B', package[111:112])[0]
        self.brake = struct.unpack('B', package[112:113])[0]
        self.throttle = struct.unpack('B', package[113:114])[0]
        self.clutch = struct.unpack('B', package[114:115])[0]
        self.steering = struct.unpack('b', package[115:116])[0]
        self.fuel_level = struct.unpack('f', package[116:120])[0]
        self.speed = struct.unpack('f', package[120:124])[0]
        self.rpm = struct.unpack('H', package[124:126])[0]
        self.max_rpm = struct.unpack('H', package[126:128])[0]
        self.current_gear = struct.unpack('B', package[128:129])[0] & 0x0F
        self.num_gears = (struct.unpack('B', package[128:129])[0]  & 0xF0) << 4
        self.boost_amount = struct.unpack('B', package[129:130])[0]
        self.enforced_pit_stop_lap = struct.unpack('b', package[130:131])[0]
        self.crash_state = struct.unpack('B', package[131:132])[0]
        self.odometer_km = struct.unpack('f', package[132:136])[0]
        self.orientation = []
        self.orientation.append(struct.unpack('f', package[136:140])[0])
        self.orientation.append(struct.unpack('f', package[140:144])[0])
        self.orientation.append(struct.unpack('f', package[144:148])[0])
        self.local_velocity = []
        self.local_velocity.append(struct.unpack('f', package[148:152])[0])
        self.local_velocity.append(struct.unpack('f', package[152:156])[0])
        self.local_velocity.append(struct.unpack('f', package[156:160])[0])
        self.world_velocity = []
        self.world_velocity.append(struct.unpack('f', package[160:164])[0])
        self.world_velocity.append(struct.unpack('f', package[164:168])[0])
        self.world_velocity.append(struct.unpack('f', package[168:172])[0])
        self.angular_velocity = []
        self.angular_velocity.append(struct.unpack('f', package[172:176])[0])
        self.angular_velocity.append(struct.unpack('f', package[176:180])[0])
        self.angular_velocity.append(struct.unpack('f', package[180:184])[0])
        self.local_acceleration = []
        self.local_acceleration.append(struct.unpack('f', package[184:188])[0])
        self.local_acceleration.append(struct.unpack('f', package[188:192])[0])
        self.local_acceleration.append(struct.unpack('f', package[192:196])[0])
        self.world_acceleration = []
        self.world_acceleration.append(struct.unpack('f', package[196:200])[0])
        self.world_acceleration.append(struct.unpack('f', package[200:204])[0])
        self.world_acceleration.append(struct.unpack('f', package[204:208])[0])
        self.extents_center = []
        self.extents_center.append(struct.unpack('f', package[208:212])[0])
        self.extents_center.append(struct.unpack('f', package[212:216])[0])
        self.extents_center.append(struct.unpack('f', package[216:220])[0])
        #Wheels / Tyres
        self.tyre_flags = []
        self.tyre_flags.append(struct.unpack('B', package[220:221])[0])
        self.tyre_flags.append(struct.unpack('B', package[221:222])[0])
        self.tyre_flags.append(struct.unpack('B', package[222:223])[0])
        self.tyre_flags.append(struct.unpack('B', package[223:224])[0])
        self.terrain = []
        self.terrain.append(struct.unpack('B', package[224:225])[0])
        self.terrain.append(struct.unpack('B', package[225:226])[0])
        self.terrain.append(struct.unpack('B', package[226:227])[0])
        self.terrain.append(struct.unpack('B', package[227:228])[0])
        self.tyre_y = []
        self.tyre_y.append(struct.unpack('f', package[228:232])[0])
        self.tyre_y.append(struct.unpack('f', package[232:236])[0])
        self.tyre_y.append(struct.unpack('f', package[236:240])[0])
        self.tyre_y.append(struct.unpack('f', package[240:244])[0])
        self.tyre_rps = []
        self.tyre_rps.append(struct.unpack('f', package[244:248])[0])
        self.tyre_rps.append(struct.unpack('f', package[248:252])[0])
        self.tyre_rps.append(struct.unpack('f', package[252:256])[0])
        self.tyre_rps.append(struct.unpack('f', package[256:260])[0])
        self.tyre_slip_speed = []
        self.tyre_slip_speed.append(struct.unpack('f', package[260:264])[0])
        self.tyre_slip_speed.append(struct.unpack('f', package[264:268])[0])
        self.tyre_slip_speed.append(struct.unpack('f', package[268:272])[0])
        self.tyre_slip_speed.append(struct.unpack('f', package[272:276])[0])
        self.tyre_temp = []
        self.tyre_temp.append(struct.unpack('B', package[276:277])[0])
        self.tyre_temp.append(struct.unpack('B', package[277:278])[0])
        self.tyre_temp.append(struct.unpack('B', package[278:279])[0])
        self.tyre_temp.append(struct.unpack('B', package[279:280])[0])
        self.tyre_grip = []
        self.tyre_grip.append(struct.unpack('B', package[280:281])[0])
        self.tyre_grip.append(struct.unpack('B', package[281:282])[0])
        self.tyre_grip.append(struct.unpack('B', package[282:283])[0])
        self.tyre_grip.append(struct.unpack('B', package[283:284])[0])
        self.tyre_height_above_ground = []
        self.tyre_height_above_ground.append(struct.unpack('f', package[284:288])[0])
        self.tyre_height_above_ground.append(struct.unpack('f', package[288:292])[0])
        self.tyre_height_above_ground.append(struct.unpack('f', package[292:296])[0])
        self.tyre_height_above_ground.append(struct.unpack('f', package[296:300])[0])
        self.tyre_lateral_stiffness = []
        self.tyre_lateral_stiffness.append(struct.unpack('f', package[300:304])[0])
        self.tyre_lateral_stiffness.append(struct.unpack('f', package[304:308])[0])
        self.tyre_lateral_stiffness.append(struct.unpack('f', package[308:312])[0])
        self.tyre_lateral_stiffness.append(struct.unpack('f', package[312:316])[0])
        self.tyre_wear = []
        self.tyre_wear.append(struct.unpack('B', package[316:317])[0])
        self.tyre_wear.append(struct.unpack('B', package[317:318])[0])
        self.tyre_wear.append(struct.unpack('B', package[318:319])[0])
        self.tyre_wear.append(struct.unpack('B', package[319:320])[0])
        self.brake_damage = []
        self.brake_damage.append(struct.unpack('B', package[320:321])[0])
        self.brake_damage.append(struct.unpack('B', package[321:322])[0])
        self.brake_damage.append(struct.unpack('B', package[322:323])[0])
        self.brake_damage.append(struct.unpack('B', package[323:324])[0])
        self.suspension_damage = []
        self.suspension_damage.append(struct.unpack('B', package[324:325])[0])
        self.suspension_damage.append(struct.unpack('B', package[325:326])[0])
        self.suspension_damage.append(struct.unpack('B', package[326:327])[0])
        self.suspension_damage.append(struct.unpack('B', package[327:328])[0])
        self.brake_temp_celsius = []
        self.brake_temp_celsius.append(struct.unpack('h', package[328:330])[0])
        self.brake_temp_celsius.append(struct.unpack('h', package[330:332])[0])
        self.brake_temp_celsius.append(struct.unpack('h', package[332:334])[0])
        self.brake_temp_celsius.append(struct.unpack('h', package[334:336])[0])
        self.tyre_tread_temp = []
        self.tyre_tread_temp.append(struct.unpack('H', package[336:338])[0])
        self.tyre_tread_temp.append(struct.unpack('H', package[338:340])[0])
        self.tyre_tread_temp.append(struct.unpack('H', package[340:342])[0])
        self.tyre_tread_temp.append(struct.unpack('H', package[342:344])[0])
        self.tyre_layer_temp = []
        self.tyre_layer_temp.append(struct.unpack('H', package[344:346])[0])
        self.tyre_layer_temp.append(struct.unpack('H', package[346:348])[0])
        self.tyre_layer_temp.append(struct.unpack('H', package[348:350])[0])
        self.tyre_layer_temp.append(struct.unpack('H', package[350:352])[0])
        self.tyre_carcass_temp = []
        self.tyre_carcass_temp.append(struct.unpack('H', package[352:354])[0])
        self.tyre_carcass_temp.append(struct.unpack('H', package[354:356])[0])
        self.tyre_carcass_temp.append(struct.unpack('H', package[356:358])[0])
        self.tyre_carcass_temp.append(struct.unpack('H', package[358:360])[0])
        self.tyre_rim_temp = []
        self.tyre_rim_temp.append(struct.unpack('H', package[360:362])[0])
        self.tyre_rim_temp.append(struct.unpack('H', package[362:364])[0])
        self.tyre_rim_temp.append(struct.unpack('H', package[364:366])[0])
        self.tyre_rim_temp.append(struct.unpack('H', package[366:368])[0])
        self.tyre_internal_air_temp = []
        self.tyre_internal_air_temp.append(struct.unpack('H', package[368:370])[0])
        self.tyre_internal_air_temp.append(struct.unpack('H', package[370:372])[0])
        self.tyre_internal_air_temp.append(struct.unpack('H', package[372:374])[0])
        self.tyre_internal_air_temp.append(struct.unpack('H', package[374:376])[0])
        self.wheel_local_position_y = []
        self.wheel_local_position_y.append(struct.unpack('f', package[376:380])[0])
        self.wheel_local_position_y.append(struct.unpack('f', package[380:384])[0])
        self.wheel_local_position_y.append(struct.unpack('f', package[384:388])[0])
        self.wheel_local_position_y.append(struct.unpack('f', package[388:392])[0])
        self.ride_height = []
        self.ride_height.append(struct.unpack('f', package[392:396])[0])
        self.ride_height.append(struct.unpack('f', package[396:400])[0])
        self.ride_height.append(struct.unpack('f', package[400:404])[0])
        self.ride_height.append(struct.unpack('f', package[404:408])[0])
        self.suspension_travel = []
        self.suspension_travel.append(struct.unpack('f', package[408:412])[0])
        self.suspension_travel.append(struct.unpack('f', package[412:416])[0])
        self.suspension_travel.append(struct.unpack('f', package[416:420])[0])
        self.suspension_travel.append(struct.unpack('f', package[420:424])[0])
        self.suspension_velocity = []
        self.suspension_velocity.append(struct.unpack('f', package[424:428])[0])
        self.suspension_velocity.append(struct.unpack('f', package[428:432])[0])
        self.suspension_velocity.append(struct.unpack('f', package[432:436])[0])
        self.suspension_velocity.append(struct.unpack('f', package[436:440])[0])
        self.air_pressure = []
        self.air_pressure.append(struct.unpack('H', package[440:442])[0])
        self.air_pressure.append(struct.unpack('H', package[442:444])[0])
        self.air_pressure.append(struct.unpack('H', package[444:446])[0])
        self.air_pressure.append(struct.unpack('H', package[446:448])[0])
        #Extras
        self.engine_speed = struct.unpack('f', package[448:452])[0]
        self.engine_torque = struct.unpack('f', package[452:456])[0]
        #Car Damage
        self.aero_damage = struct.unpack('B', package[456:457])[0]
        self.engine_damage = struct.unpack('B', package[457:458])[0]
        #Weather
        self.ambient_temperature = struct.unpack('b', package[458:459])[0]
        self.track_temperature = struct.unpack('b', package[459:460])[0]
        self.rain_density = struct.unpack('B', package[460:461])[0]
        self.wind_speed = struct.unpack('b', package[461:462])[0]
        self.wind_direction_x = struct.unpack('b', package[462:463])[0]
        self.wind_direction_y = struct.unpack('b', package[463:464])[0]
        #Participant Info
        self.participant_info = []
        for x in range(0, 56):
            participant_pos = 464 + (16 * x)
            self.participant_info.append(ParticipantInfo.ParticipantInfo(package[participant_pos:(participant_pos + 16)]))
        self.track_lenght = struct.unpack('f', package[1360:1364])[0]
        self.wings = []
        self.wings.append(struct.unpack('B', package[1364:1365])[0])
        self.wings.append(struct.unpack('B', package[1365:1366])[0])
        self.d_pad = struct.unpack('B', package[1366:1367])[0]
        #self.padding = struct.unpack('B', package[1367:1368])[0]
