import acconeer.exptool as et
from acconeer.exptool import a121

args = a121.ExampleArgumentParser().parse_args()
et.utils.config_logging(args)

client = a121.Client.open(**a121.get_client_args(args))

sensor_config = a121.SensorConfig(
    subsweeps=[
        a121.SubsweepConfig(
            start_point=5,
            step_length=2,
            num_points=5,
            profile=a121.Profile.PROFILE_1,
            hwaas=10,
        ),
        a121.SubsweepConfig(
            start_point=20,
            step_length=4,
            num_points=5,
            profile=a121.Profile.PROFILE_3,
            hwaas=20,
        ),
    ],
    sweeps_per_frame=1,
    frame_rate=1
)

client.setup_session(sensor_config)
client.start_session()

while True:
    result = client.get_next()
    print(result._frame)
    break
client.stop_session()
client.close()
