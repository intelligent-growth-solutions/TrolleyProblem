import multiprocessing
import frontend
import time
from mqttController import MqttController

if __name__ == "__main__":
    # Create a Pipe for communication with the UI process
    main_pipe, ui_pipe = multiprocessing.Pipe()

    # Start the Tkinter UI in a separate process
    ui_process = multiprocessing.Process(target=frontend.run_ui, args=(ui_pipe,))
    ui_process.start()

    # Wait for a short time to allow the UI process to update
    time.sleep(5)

    # Instantiate mqtt
    mqtt = MqttController()
    # Start the Tkinter UI in a separate process
    mqtt_process = multiprocessing.Process(target=mqtt.initialise, args=(main_pipe,))
    mqtt_process.start()

    # Close the pipe to signal the end of communication
    #main_pipe.close()

    # Wait for the UI process to finish
    #ui_process.join()


#redundant test function
# def plot_points_from_input(pipe):
#     pipe.send([(25, 25)])
#     print("Point sent to UI")
#     time.sleep(1)
#     pipe.send([(25, 25),
#               (50, 50)])
#     time.sleep(1)
#     pipe.send([(25, 25),
#               (50, 50),
#               (75, 75)])
#     for i in range(10):
#         pipe.send([(25, 25)])
#         time.sleep(0.5)
#         pipe.send([(50, 50)])
#         time.sleep(0.5)
#         pipe.send([(75, 75)])
#         time.sleep(0.5)