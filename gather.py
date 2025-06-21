from acconeer.exptool import a121

client = a121.Client.open()

print("Server Info:")
print(client.server_info)

sensor_config = a121.SensorConfig()
sensor_config.start_point = 60
sensor_config.step_length = 8
sensor_config.num_points = 271
sensor_config.sweeps_per_frame = 8
sensor_config.hwaas = 16
sensor_config.frame_rate = 20
sensor_config.prf = (6500000, 18.5, 23.1)
client.setup_session(sensor_config)

client.start_session()

while True:
    result = client.get_next()
    print(result._frame)
    break

client.close()
